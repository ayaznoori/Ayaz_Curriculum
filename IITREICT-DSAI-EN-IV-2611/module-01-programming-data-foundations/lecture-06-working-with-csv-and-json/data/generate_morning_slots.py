#!/usr/bin/env python3
"""Generate morning_slots.csv (120 rows) and hub_rules.json for lecture-06."""
import csv
import json
import random
from datetime import date, timedelta

random.seed(261106)
BASE = "/Users/masai/Documents/AIML courses./IITREICT-DSAI-EN-IV-2611/module-01-programming-data-foundations/lecture-06-working-with-csv-and-json/data"

ITEMS = [
    "Tomato 500g",
    "Milk 1L",
    "Curd 400g",
    "Paneer 200g",
    "Onion 1kg",
    "Banana dozen",
    "Bread loaf",
    "Eggs 6 pack",
]
HUBS = ["NORTH", "SOUTH", "EAST", "WEST"]
start = date(2026, 3, 10)

rows = []
for i in range(1, 121):
    slot_id = f"SL{i:04d}"
    hub = random.choice(HUBS)
    item = random.choice(ITEMS)
    boxes = random.randint(1, 40)
    temp = round(random.uniform(2.5, 7.5), 1)
    packed = start + timedelta(days=i % 14)
    packed_on = packed.isoformat()
    rows.append([slot_id, hub, item, boxes, temp, packed_on])

# Edge cases (fixed indices)
edge_boxes = {7: "", 15: "", 22: "", 31: "", 44: ""}
edge_temp_text = {12: "warm", 56: "NA", 89: ""}
edge_temp_range = {33: 9.5, 67: 1.2}
edge_dates = {18: "18-03-2026", 41: "15-03-2026", 95: "20-03-2026"}
edge_hub = {100: "WESTX"}

for idx, val in edge_boxes.items():
    rows[idx - 1][3] = val
for idx, val in edge_temp_text.items():
    rows[idx - 1][4] = val
for idx, val in edge_temp_range.items():
    rows[idx - 1][4] = val
for idx, val in edge_dates.items():
    rows[idx - 1][5] = val
for idx, val in edge_hub.items():
    rows[idx - 1][1] = val

csv_path = f"{BASE}/morning_slots.csv"
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["slot_id", "hub_code", "item_name", "boxes_packed", "temp_c", "packed_on"])
    w.writerows(rows)

rules = {
    "schema_version": 2,
    "required_columns": [
        "slot_id",
        "hub_code",
        "item_name",
        "boxes_packed",
        "temp_c",
        "packed_on",
    ],
    "hubs": {
        "NORTH": {
            "zones": ["veg", "dairy"],
            "temp_range": {"min_c": 2.0, "max_c": 8.0},
            "lead": "Meera",
        },
        "SOUTH": {
            "zones": ["veg", "bakery"],
            "temp_range": {"min_c": 2.0, "max_c": 8.0},
            "lead": "Rohan",
        },
        "EAST": {
            "zones": ["dairy", "frozen"],
            "temp_range": {"min_c": 2.0, "max_c": 8.0},
            "lead": "Sita",
        },
        "WEST": {
            "zones": ["veg", "frozen"],
            "temp_range": {"min_c": 2.0, "max_c": 8.0},
            "lead": "Vijay",
        },
    },
    "sample_slots": [
        {"slot_id": "SL0001", "item_name": "Milk 1L", "boxes_packed": 12},
        {"slot_id": "SL0002", "item_name": "Tomato 500g", "boxes_packed": 30},
    ],
}

json_path = f"{BASE}/hub_rules.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(rules, f, indent=2)

print("wrote", len(rows), "rows to", csv_path)
print("wrote hub_rules.json")