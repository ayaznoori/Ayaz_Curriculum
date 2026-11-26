#!/usr/bin/env python3
"""Charts from mess_menu_lines.csv (same numbers as lecture code)."""
import csv
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT.parent / "data" / "mess_menu_lines.csv"
plt.rcParams.update({"font.size": 10})


def load():
    rows = []
    with open(DATA, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append(r)
    return rows


def save(fig, name: str) -> None:
    path = ROOT / name
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("wrote", path)


def chart01_length_hist(rows):
    lens = [len(r["raw_line"]) for r in rows if r["raw_line"].strip()]
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.hist(lens, bins=18, color="#2563eb", edgecolor="white")
    ax.set_xlabel("Characters in raw_line (non-empty rows)")
    ax.set_ylabel("Row count")
    ax.set_title("Length of messy menu lines before cleanup (120 invented rows)")
    save(fig, "01_raw_line_lengths.png")


def chart02_leading_spaces(rows):
    counts = Counter()
    for r in rows:
        raw = r["raw_line"]
        lead = len(raw) - len(raw.lstrip(" "))
        counts[lead] += 1
    xs = sorted(counts)
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.bar(xs, [counts[x] for x in xs], color="#16a34a")
    ax.set_xlabel("Leading space count")
    ax.set_ylabel("Menu lines")
    ax.set_title("How many lines start with extra spaces")
    save(fig, "02_leading_spaces.png")


def chart03_slot_counts(rows):
    c = Counter(r["meal_slot"] for r in rows)
    fig, ax = plt.subplots(figsize=(9, 4.5))
    labels = list(c.keys())
    ax.bar(labels, [c[k] for k in labels], color="#d97706")
    ax.set_ylabel("Lines per slot")
    ax.set_title("Menu lines by meal slot in the full file")
    save(fig, "03_meal_slot_counts.png")


def chart04_empty_and_clean(rows):
    empty = sum(1 for r in rows if r["raw_line"].strip() == "")
    nonempty = len(rows) - empty
    fig, ax = plt.subplots(figsize=(6, 4.5))
    ax.bar(["non-empty", "empty"], [nonempty, empty], color=["#7c3aed", "#dc2626"])
    ax.set_ylabel("Row count")
    ax.set_title("Empty raw_line rows in mess_menu_lines.csv")
    save(fig, "04_empty_lines.png")


def chart05_day_counts(rows):
    c = Counter(r["meal_day"] for r in rows)
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.bar(days, [c[d] for d in days], color="#0891b2")
    ax.set_ylabel("Lines per day")
    ax.set_title("Menu lines spread across the week")
    save(fig, "05_lines_per_day.png")


def chart06_tidy_lengths(rows):
    def tidy(raw: str) -> str:
        if raw.strip() == "":
            return ""
        name = raw.strip().split("(")[0].strip().replace("  ", " ")
        return name.title()

    before = [len(r["raw_line"]) for r in rows if r["raw_line"].strip()]
    after = [len(tidy(r["raw_line"])) for r in rows if r["raw_line"].strip()]
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.scatter(before, after, alpha=0.55, color="#be123c")
    ax.plot([0, max(before)], [0, max(before)], ls="--", color="#94a3b8")
    ax.set_xlabel("Raw line length")
    ax.set_ylabel("Tidy dish name length")
    ax.set_title("Shorter dish names after strip and title on the full file")
    save(fig, "06_raw_vs_tidy_length.png")


def main():
    rows = load()
    assert len(rows) == 120
    chart01_length_hist(rows)
    chart02_leading_spaces(rows)
    chart03_slot_counts(rows)
    chart04_empty_and_clean(rows)
    chart05_day_counts(rows)
    chart06_tidy_lengths(rows)


if __name__ == "__main__":
    main()