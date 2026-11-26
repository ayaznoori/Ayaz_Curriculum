#!/usr/bin/env python3
"""Run every ```sql block in lecture-script.md on SQLite and compare (or fill) its **Output** block.

Usage (from this folder):
  python3 data/run_lecture_queries.py --check lecture-script.md   # exit 1 on any mismatch
  python3 data/run_lecture_queries.py --fill  lecture-script.md   # replace '@@' placeholders with real output

Data: data/shop_a_products.sql and data/fest_coupons.sql (loaded into an in-memory database).
Output style: boxed table, left-aligned, NULL shown as NULL, errors as 'Error: <message>'.
"""
import sqlite3
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def connect():
    con = sqlite3.connect(":memory:")
    for name in ("shop_a_products.sql", "fest_coupons.sql"):
        con.executescript((HERE / name).read_text(encoding="utf-8"))
    return con


def table(header, rows):
    cells = [[("NULL" if v is None else str(v)) for v in r] for r in rows]
    widths = [max([len(h)] + [len(r[i]) for r in cells]) for i, h in enumerate(header)]
    line = "+" + "+".join("-" * (w + 2) for w in widths) + "+"

    def row(vals):
        return "| " + " | ".join(v.ljust(w) for v, w in zip(vals, widths)) + " |"

    out = [line, row(header), line] + [row(r) for r in cells] + [line]
    return "\n".join(out)


def split_statements(sql):
    stmts, cur = [], ""
    for ln in sql.splitlines():
        cur += ln + "\n"
        if sqlite3.complete_statement(cur):
            stmts.append(cur.strip())
            cur = ""
    if cur.strip():
        stmts.append(cur.strip())
    return stmts


def run_block(con, sql):
    parts = []
    for stmt in split_statements(sql):
        try:
            cur = con.execute(stmt)
            header = [d[0] for d in cur.description]
            rows = cur.fetchall()
            parts.append(table(header, rows) if rows else "Empty set")
        except sqlite3.Error as e:
            parts.append(f"Error: {e}")
    return "\n\n".join(parts)


def sql_blocks(lines):
    """Yield (sql_text, out_start, out_end) with out_* = line indexes of the Output fence body."""
    i, n = 0, len(lines)
    while i < n:
        if lines[i].startswith("```sql"):
            j = i + 1
            while not lines[j].startswith("```"):
                j += 1
            sql = "\n".join(lines[i + 1 : j])
            k = j + 1
            while k < n and k < j + 6 and "**Output**" not in lines[k]:
                k += 1
            if k < n and "**Output**" in lines[k] and k < j + 6:
                s = k + 1
                while lines[s].strip() == "":
                    s += 1
                assert lines[s].startswith("```"), f"no output fence after line {k + 1}"
                e = s + 1
                while not lines[e].startswith("```"):
                    e += 1
                yield sql, s + 1, e
                i = e
            else:
                i = j
        i += 1


def main(argv):
    if len(argv) != 3 or argv[1] not in ("--check", "--fill"):
        print(__doc__)
        return 2
    path = Path(argv[2])
    lines = path.read_text(encoding="utf-8").split("\n")
    con = connect()
    bad = ok = 0
    edits = []
    for sql, s, e in sql_blocks(lines):
        want = run_block(con, sql)
        have = "\n".join(lines[s:e])
        if argv[1] == "--fill":
            if have.strip() == "@@":
                edits.append((s, e, want.split("\n")))
            continue
        if have.rstrip() == want.rstrip():
            ok += 1
        else:
            bad += 1
            print(f"MISMATCH output at line {s + 1}\n--- pasted\n{have}\n--- real\n{want}\n")
    if argv[1] == "--fill":
        for s, e, new in reversed(edits):
            lines[s:e] = new
        path.write_text("\n".join(lines), encoding="utf-8")
        print(f"filled {len(edits)} output blocks")
        return 0
    print(f"SQL blocks: {ok} match, {bad} mismatch")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
