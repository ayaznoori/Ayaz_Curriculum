#!/usr/bin/env python3
"""Mentor helper: run every ```sql block in lecture-script.md against SQLite and compare
with the pasted **Output** block.

Usage (from this folder):
  python3 run_lecture_queries.py --check   # exit 1 if any pasted output differs
  python3 run_lecture_queries.py --fill    # rewrite the Output blocks from a fresh run

Learners do NOT use this file. It only keeps the script honest.
Needs the sqlite3 command line tool (version 3.39 or later for RIGHT and FULL OUTER JOIN).
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE.parent / "lecture-script.md"
SQL_FILE = HERE / "shop_a_joins.sql"


def run_sql(query: str) -> str:
    with tempfile.TemporaryDirectory() as tmp:
        db = Path(tmp) / "lec10.db"
        subprocess.run(["sqlite3", str(db)], stdin=open(SQL_FILE), check=True)
        done = subprocess.run(
            ["sqlite3", "-cmd", ".mode table", "-cmd", ".nullvalue NULL", str(db)],
            input=query, capture_output=True, text=True,
        )
    return (done.stdout + done.stderr).rstrip("\n")


def main(mode: str) -> int:
    text = SCRIPT.read_text(encoding="utf-8")
    pattern = re.compile(
        r"(```sql\n(?P<q>.*?)\n```\n\n\*\*Output\*\*\n\n```\n)(?P<out>.*?)(\n```)", re.S
    )
    bad = 0
    count = 0

    def repl(m):
        nonlocal bad, count
        count += 1
        got = run_sql(m.group("q"))
        if got != m.group("out").rstrip("\n"):
            bad += 1
            if mode == "check":
                print(f"MISMATCH in block {count}:\n{m.group('q')[:120]}\n--- got\n{got}\n--- pasted\n{m.group('out')}")
        return m.group(1) + got + m.group(4)

    new = pattern.sub(repl, text)
    if mode == "fill":
        SCRIPT.write_text(new, encoding="utf-8")
        print(f"filled {count} sql blocks ({bad} changed)")
        return 0
    print(f"checked {count} sql blocks, {bad} mismatches")
    return 1 if bad else 0


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("--check", "--fill"):
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1][2:]))
