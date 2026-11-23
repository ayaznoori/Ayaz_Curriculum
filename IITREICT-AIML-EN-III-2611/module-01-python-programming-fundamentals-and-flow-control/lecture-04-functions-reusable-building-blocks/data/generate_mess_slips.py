#!/usr/bin/env python3
"""Generate mess_slips.csv (120 rows, fixed seed) for lecture-04."""
import csv
import random

random.seed(261104)
STUDENTS = ["Rahul", "Priya", "Dev", "Anya", "Kiran", "Meera", "Arjun", "Neha", "Isha", "Vikram"]
MODES = ["single", "double"]
rows = []
for i in range(1, 121):
    sid = f"J{i:03d}"
    student = random.choice(STUDENTS)
    pages = random.randint(1, 60)
    if pages == 1:
        pages = 2
    mode = random.choices(MODES, weights=[62, 38])[0]
  # edge: smallest 2, largest 60, ties, one zero-page handled as 2 min
    if i == 5:
        pages = 2
    if i == 42:
        pages = 60
    if i == 77:
        pages = 12
        mode = "single"
        student = "Rahul"
    if i == 88:
        pages = 25
        mode = "double"
        student = "Priya"
    if i == 99:
        pages = 8
        mode = "single"
        student = "Dev"
    rows.append((sid, student, pages, mode))

path = "/Users/masai/Documents/AIML courses./IITREICT-DSAI-EN-IV-2611/module-01-programming-data-foundations/lecture-04-functions-reusable-building-blocks/data/mess_slips.csv"
with open(path, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["job_id", "student", "pages", "side_mode"])
    w.writerows(rows)
print("wrote", len(rows), "rows to", path)