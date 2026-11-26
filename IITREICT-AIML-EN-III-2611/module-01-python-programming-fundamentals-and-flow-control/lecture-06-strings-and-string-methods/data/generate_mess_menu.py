#!/usr/bin/env python3
"""Generate mess_menu_lines.csv (120 rows, fixed seed) for lecture-06."""
import csv
import random

random.seed(261106)
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
BASE = [
    "Dal Fry", "Rajma Curry", "Paneer Butter Masala", "Veg Biryani", "Jeera Rice",
    "Chapati", "Butter Naan", "Raita", "Green Salad", "Fruit Bowl",
    "Masala Dosa", "Idli Sambhar", "Upma", "Poha", "Paratha",
]
SLOTS = ["BREAKFAST", "LUNCH", "SNACKS", "DINNER"]
rows = []
for i in range(1, 121):
    dish = random.choice(BASE)
    roll = random.randint(1, 4)
    tag = random.choice(["VEG", "NV"])
    core = f"{dish[:3].upper()}-{i:03d}-{tag}"
    pad_l = random.randint(0, 3)
    pad_r = random.randint(0, 2)
    messy_core = core
    if random.random() < 0.55:
        messy_core = core.lower()
    if random.random() < 0.4:
        messy_core = messy_core.replace("-", " - ")
    line = " " * pad_l + f"  {dish}  ({messy_core}) ₹{random.choice([45, 55, 65, 75, 85, 99])}  " + " " * pad_r
    if i == 7:
        line = "   jeera RICE  (jee-007-veg) ₹65 "
    if i == 22:
        line = ""
    if i == 44:
        line = "  PANEER  butter  MASALA  (pan-044-veg) ₹85  "
    if i == 60:
        line = "MASOOR DAL (mas-060-veg) ₹45"
    if i == 88:
        line = "    fruit   bowl   (fru-088-veg) ₹55   "
    day = DAYS[(i - 1) % 7]
    slot = SLOTS[(i - 1) % 4]
    rows.append((f"M{i:03d}", day, slot, line))

out = (
    "/Users/masai/Documents/AIML courses./IITREICT-AIML-EN-III-2611/"
    "module-01-python-programming-fundamentals-and-flow-control/"
    "lecture-06-strings-and-string-methods/data/mess_menu_lines.csv"
)
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["line_id", "meal_day", "meal_slot", "raw_line"])
    w.writerows(rows)
print("wrote", len(rows), "rows to", out)