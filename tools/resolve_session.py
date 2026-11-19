#!/usr/bin/env python3
"""Resolve a session by title against course curriculum CSVs.

Usage:
  python3 tools/resolve_session.py "Session Title"
  python3 tools/resolve_session.py "Session Title" --course IITP-AIMLPX-ADV-II-2610
  python3 tools/resolve_session.py "Session Title" --json

Exit 0: unique match. Exit 1: no match. Exit 2: ambiguous (multiple courses).
"""
from __future__ import annotations

import argparse
import csv
import difflib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COURSES = ROOT / "courses"

TITLE_KEYS = ("Session Title", "session title", "title", "Session Name")
MODULE_KEYS = ("Module ( as per website )", "Module", "module name", "module")
TOPICS_KEYS = ("Topics", "topics")
LO_STMT_KEYS = ("LO_Statement", "learning objectives", "objectives")
LO_ID_KEYS = ("LO_ID", "lo_id")


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def pick(row: dict, keys: tuple[str, ...]) -> str:
    lower = {norm(k): v for k, v in row.items() if k}
    for key in keys:
        if norm(key) in lower and (lower[norm(key)] or "").strip():
            return (lower[norm(key)] or "").strip()
    return ""


def split_los(text: str) -> list[str]:
    parts = [x.strip() for x in re.split(r"[;\n]", text or "") if x.strip()]
    return parts


def read_curriculum(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def score_title(want: str, got: str) -> float:
    want, got = norm(want), norm(got)
    if not got:
        return -1.0
    if want == got:
        return 1.0
    if want in got or got in want:
        return 0.85
    return difflib.SequenceMatcher(None, want, got).ratio()


def find_in_csv(path: Path, title: str) -> tuple[dict | None, float]:
    rows = read_curriculum(path)
    best_row, best_score = None, -1.0
    for row in rows:
        t = pick(row, TITLE_KEYS)
        if not t:
            continue
        sc = score_title(title, t)
        if sc > best_score:
            best_score, best_row = sc, row
    if best_row is None or best_score < 0.6:
        return None, best_score
    return best_row, best_score


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("session_title")
    ap.add_argument("--course", help="Batch code folder under courses/")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.course:
        csv_path = COURSES / args.course / "curriculum.csv"
        if not csv_path.is_file():
            print(f"No curriculum at {csv_path}", file=sys.stderr)
            return 1
        row, score = find_in_csv(csv_path, args.session_title)
        if row is None:
            print(f"No session match in {args.course} (best score {score:.2f})", file=sys.stderr)
            return 1
        matches = [(args.course, row, score, str(csv_path))]
    else:
        matches = []
        for course_dir in sorted(COURSES.iterdir()) if COURSES.is_dir() else []:
            if not course_dir.is_dir():
                continue
            csv_path = course_dir / "curriculum.csv"
            if not csv_path.is_file():
                continue
            row, score = find_in_csv(csv_path, args.session_title)
            if row is not None:
                matches.append((course_dir.name, row, score, str(csv_path)))

        good = [m for m in matches if m[2] >= 0.85]
        if len(good) == 1:
            matches = good
        elif len(good) > 1:
            names = ", ".join(m[0] for m in good)
            print(f"Ambiguous title across courses: {names}. Pass --course.", file=sys.stderr)
            return 2
        elif len(matches) == 1:
            pass
        elif not matches:
            print("No session match in any course curriculum.", file=sys.stderr)
            return 1
        else:
            top = max(matches, key=lambda m: m[2])
            if top[2] < 0.92:
                print("Multiple weak matches; pass --course.", file=sys.stderr)
                for code, row, sc, _ in sorted(matches, key=lambda m: -m[2])[:5]:
                    print(f"  {code}: {pick(row, TITLE_KEYS)!r} ({sc:.2f})", file=sys.stderr)
                return 2
            matches = [top]

    course, row, score, csv_path = matches[0]
    session = pick(row, TITLE_KEYS)
    module = pick(row, MODULE_KEYS)
    topics = pick(row, TOPICS_KEYS)
    lo_stmt = pick(row, LO_STMT_KEYS)
    lo_ids = pick(row, LO_ID_KEYS)
    los = split_los(lo_stmt)

    payload = {
        "course_code": course,
        "curriculum_csv": csv_path,
        "session_title": session,
        "module_name": module,
        "topics_semicolon": topics,
        "learning_objectives_semicolon": lo_stmt,
        "learning_objectives_list": los,
        "lo_ids": lo_ids,
        "match_score": round(score, 3),
        "preread_output_dir": str(ROOT / "courses" / course / "prereads"),
        "lecture_output_dir": str(ROOT / "courses" / course / "lecture-scripts"),
    }

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        for k, v in payload.items():
            if k != "learning_objectives_list":
                print(f"{k}: {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())