#!/usr/bin/env python3
"""Run lecture code blocks from lecture-06 working directory."""
import csv
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
DATA = "data"

print("=== T1 read header ===")
import csv as csv_mod
with open(f"{DATA}/morning_slots.csv", newline="", encoding="utf-8") as f:
    rows = list(csv_mod.reader(f))
print(rows[0])
print(len(rows) - 1, rows[1][0], rows[1][3])

print("=== T1 DictReader NORTH count ===")
north = 0
with open(f"{DATA}/morning_slots.csv", newline="", encoding="utf-8") as f:
    for row in csv_mod.DictReader(f):
        if row["hub_code"] == "NORTH":
            north += 1
with open(f"{DATA}/morning_slots.csv", newline="", encoding="utf-8") as f:
    dr = list(csv_mod.DictReader(f))
print(north, dr[0]["slot_id"], dr[0]["item_name"])

print("=== T1 write hub export ===")
export = []
with open(f"{DATA}/morning_slots.csv", newline="", encoding="utf-8") as f:
    for r in csv_mod.DictReader(f):
        if r["hub_code"] == "EAST" and r["boxes_packed"].strip():
            export.append({"slot_id": r["slot_id"], "item_name": r["item_name"], "boxes_packed": r["boxes_packed"]})
with open(f"{DATA}/east_export.csv", "w", newline="", encoding="utf-8") as g:
    w = csv_mod.DictWriter(g, fieldnames=["slot_id", "item_name", "boxes_packed"])
    w.writeheader()
    w.writerows(export)
    print(len(export), export[0]["slot_id"])

print("=== T2 json.load ===")
with open(f"{DATA}/hub_rules.json", encoding="utf-8") as f:
    rules = json.load(f)
print(rules["schema_version"], rules["hubs"]["NORTH"]["lead"], rules["hubs"]["NORTH"]["temp_range"]["max_c"])

print("=== T2 nested list ===")
sample = rules["sample_slots"]
print(len(sample), sample[0]["slot_id"], sample[1]["boxes_packed"])

print("=== T2 json.loads string ===")
snippet = '{"hub_code":"NORTH","temp_c":6.1,"ok":true}'
row = json.loads(snippet)
print(row["hub_code"], type(row["temp_c"]), row["ok"])

print("=== T2 dict keys same as JSON ===")
print(list(rules["hubs"]["SOUTH"]["zones"]), type(rules["required_columns"]))

print("=== T3 validation counts ===")
required = rules["required_columns"]
min_c = rules["hubs"]["WEST"]["temp_range"]["min_c"]
max_c = rules["hubs"]["WEST"]["temp_range"]["max_c"]
valid_hubs = set(rules["hubs"].keys())
missing_cols = []
type_errors = 0
range_errors = 0
hub_errors = 0
empty_boxes = 0
with open(f"{DATA}/morning_slots.csv", newline="", encoding="utf-8") as f:
    for row in csv_mod.DictReader(f):
        if not row["boxes_packed"].strip():
            empty_boxes += 1
        try:
            t = float(row["temp_c"])
            if t < min_c or t > max_c:
                range_errors += 1
        except ValueError:
            type_errors += 1
        if row["hub_code"] not in valid_hubs:
            hub_errors += 1
with open(f"{DATA}/morning_slots.csv", newline="", encoding="utf-8") as f:
    header = next(csv_mod.reader(f))
extra = [c for c in required if c not in header]
print(len(header), len(extra), empty_boxes, type_errors, range_errors, hub_errors)

print("=== T4 fix and write ===")

def norm_date(s):
    s = s.strip()
    if len(s) == 10 and s[2] == "-" and s[5] == "-":
        d, m, y = s.split("-")
        return f"{y}-{m}-{d}"
    return s

fixed = 0
clean = []
with open(f"{DATA}/morning_slots.csv", newline="", encoding="utf-8") as f:
    for row in csv_mod.DictReader(f):
        boxes = row["boxes_packed"].strip() or "0"
        try:
            temp = float(row["temp_c"])
        except ValueError:
            continue
        if row["hub_code"] not in valid_hubs:
            continue
        if temp < min_c or temp > max_c:
            continue
        clean.append(
            {
                "slot_id": row["slot_id"],
                "hub_code": row["hub_code"],
                "item_name": row["item_name"],
                "boxes_packed": int(float(boxes)),
                "temp_c": temp,
                "packed_on": norm_date(row["packed_on"]),
            }
        )
        fixed += 1
with open(f"{DATA}/clean_slots.csv", "w", newline="", encoding="utf-8") as g:
    w = csv_mod.DictWriter(
        g,
        fieldnames=["slot_id", "hub_code", "item_name", "boxes_packed", "temp_c", "packed_on"],
    )
    w.writeheader()
    w.writerows(clean)
    print(fixed, clean[0]["packed_on"], len(clean))

print("=== closing verify ===")
with open(f"{DATA}/clean_slots.csv", newline="", encoding="utf-8") as f:
    n = sum(1 for _ in csv_mod.DictReader(f))
print(n)