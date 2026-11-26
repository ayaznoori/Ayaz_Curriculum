#!/usr/bin/env python3
"""Run lecture code blocks in cumulative namespace; print each block output."""
from __future__ import annotations

BLOCKS: list[tuple[str, str]] = []


def run(label: str, code: str, globs: dict) -> None:
    print("\n" + "=" * 60)
    print(label)
    print("=" * 60)
    exec(code, globs)


def main() -> None:
    g: dict = {}
    run(
        "T1 Example",
        """
lunch_line = "  Dal Fry  "
evening_line = "Jeera Rice"
dash = " + "
full_board = lunch_line + dash + evening_line
print(full_board[0], full_board[-1])
print(len(full_board), len(lunch_line))
""",
        g,
    )
    run(
        "T1 Ext1",
        """
print(lunch_line[0], lunch_line[-1])
print(lunch_line[4:7])
""",
        g,
    )
    run(
        "T1 Ext2 combine",
        """
board_line = lunch_line.strip() + " | " + evening_line
print(board_line)
print(board_line.index("Dal"))
""",
        g,
    )
    run(
        "T2 Example",
        """
messy = "  paneer  butter  MASALA  "
print([messy.strip(), messy.lower()])
print([messy.upper(), messy.title()])
print([messy])
""",
        g,
    )
    run(
        "T2 Ext chain",
        """
tidy = messy.strip().replace("  ", " ").lower().title()
print(tidy, len(messy), len(tidy))
""",
        g,
    )
    run(
        "T2 Ext replace",
        """
with_code = "  rajma  curry  (raj-012-veg)  "
print(with_code.strip().replace("  ", " "))
""",
        g,
    )
    run(
        "T3 Example",
        """
item_code = "DAL-007-VEG"
print(item_code[0])
print(item_code[:3], item_code[4:7], item_code[8:])
print(item_code[-3:])
""",
        g,
    )
    run(
        "T3 Ext messy",
        """
messy_code = " dal - 007 - veg "
print(messy_code[:3], messy_code[4:8], messy_code[9:])
print(len(messy_code))
""",
        g,
    )
    run(
        "T3 Ext fixed",
        """
fixed = messy_code.strip().upper().replace(" - ", "-")
print(fixed)
print(fixed[:3], fixed[4:7], fixed[8:])
""",
        g,
    )
    run(
        "T4 Example",
        """
raw_lines = [
    "  jeera RICE  (jee-007-veg) ₹65 ",
    "  PANEER  butter  MASALA  (pan-044-veg) ₹85  ",
    "    fruit   bowl   (fru-088-veg) ₹55   ",
    "",
    "Masala Dosa (dos-015-veg) ₹55",
]
cleaned = []
for line in raw_lines:
    if line.strip() == "":
        continue
    name = line.strip().split("(")[0]
    cleaned.append(name.strip().replace("  ", " ").title())
print(len(cleaned), cleaned)
""",
        g,
    )
    run(
        "T4 Ext code extract",
        """
codes = []
for line in raw_lines:
    if "(" not in line:
        continue
    start = line.index("(") + 1
    end = line.index(")")
    codes.append(line[start:end].strip().upper())
print(codes)
""",
        g,
    )
    run(
        "Closing",
        """
def tidy_line(raw):
    if raw.strip() == "":
        return ""
    name = raw.strip().split("(")[0].strip().replace("  ", " ")
    return name.title()

sample = raw_lines[1]
before = len(raw_lines)
after = sum(1 for line in raw_lines if line.strip() != "")
print([tidy_line(sample), len(sample), len(tidy_line(sample))])
print(before, after, len(cleaned))
""",
        g,
    )


if __name__ == "__main__":
    main()