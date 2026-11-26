#!/usr/bin/env python3
import csv
import json
import os
from collections import Counter

import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
IMG = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(DATA, "morning_slots.csv"), newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

hub_counts = Counter(r["hub_code"] for r in rows)
fig, ax = plt.subplots(figsize=(9, 4.5), dpi=200)
codes = sorted(hub_counts.keys())
ax.bar(codes, [hub_counts[c] for c in codes], color="#2563eb")
ax.set_title("Morning slot rows per hub code in morning_slots.csv")
ax.set_xlabel("Hub code")
ax.set_ylabel("Row count")
plt.xticks(rotation=20, ha="right")
plt.tight_layout()
fig.savefig(os.path.join(IMG, "01_rows_by_hub_code.png"))
plt.close()

empties_by_hub = Counter()
for r in rows:
    if not r["boxes_packed"].strip():
        empties_by_hub[r["hub_code"]] += 1
fig, ax = plt.subplots(figsize=(9, 4.5), dpi=200)
hubs = ["NORTH", "SOUTH", "EAST", "WEST"]
ax.bar(hubs, [empties_by_hub.get(h, 0) for h in hubs], color="#dc2626")
ax.set_title("Rows with blank boxes_packed per valid hub")
ax.set_xlabel("Hub code")
ax.set_ylabel("Blank box count")
plt.tight_layout()
fig.savefig(os.path.join(IMG, "02_blank_boxes_by_hub.png"))
plt.close()

temps = []
for r in rows:
    try:
        temps.append(float(r["temp_c"]))
    except ValueError:
        pass
fig, ax = plt.subplots(figsize=(9, 4.5), dpi=200)
ax.hist(temps, bins=12, color="#16a34a", edgecolor="white")
ax.axvline(2, color="#b45309", linestyle="--", linewidth=1.5, label="Min 2 C")
ax.axvline(8, color="#b45309", linestyle="--", linewidth=1.5, label="Max 8 C")
ax.set_title("Histogram of numeric temp_c values before cleaning")
ax.set_xlabel("Temperature (C)")
ax.set_ylabel("Row count")
ax.legend()
plt.tight_layout()
fig.savefig(os.path.join(IMG, "03_temp_histogram.png"))
plt.close()

with open(os.path.join(DATA, "hub_rules.json"), encoding="utf-8") as f:
    rules = json.load(f)
valid = set(rules["hubs"])
min_c, max_c = 2.0, 8.0
empty_boxes = type_errors = range_errors = hub_errors = 0
for r in rows:
    if not r["boxes_packed"].strip():
        empty_boxes += 1
    try:
        t = float(r["temp_c"])
        if t < min_c or t > max_c:
            range_errors += 1
    except ValueError:
        type_errors += 1
    if r["hub_code"] not in valid:
        hub_errors += 1
labels = ["blank boxes", "bad temp text", "temp out of range", "bad hub"]
vals = [empty_boxes, type_errors, range_errors, hub_errors]
fig, ax = plt.subplots(figsize=(9, 4.5), dpi=200)
ax.barh(labels, vals, color=["#7c3aed", "#d97706", "#2563eb", "#dc2626"])
ax.set_title("Validation issue counts in morning_slots.csv")
ax.set_xlabel("Count")
plt.tight_layout()
fig.savefig(os.path.join(IMG, "04_validation_issue_counts.png"))
plt.close()

with open(os.path.join(DATA, "clean_slots.csv"), newline="", encoding="utf-8") as f:
    clean = list(csv.DictReader(f))
clean_hub = Counter(r["hub_code"] for r in clean)
fig, ax = plt.subplots(figsize=(9, 4.5), dpi=200)
ax.bar(sorted(clean_hub.keys()), [clean_hub[h] for h in sorted(clean_hub)], color="#15803d")
ax.set_title("Clean rows per hub in clean_slots.csv")
ax.set_xlabel("Hub code")
ax.set_ylabel("Row count")
plt.tight_layout()
fig.savefig(os.path.join(IMG, "05_clean_rows_by_hub.png"))
plt.close()

zone_counts = Counter()
for hub, info in rules["hubs"].items():
    for z in info["zones"]:
        zone_counts[z] += 1
fig, ax = plt.subplots(figsize=(9, 4.5), dpi=200)
ax.bar(sorted(zone_counts.keys()), [zone_counts[z] for z in sorted(zone_counts)], color="#0891b2")
ax.set_title("Zone tags listed under each hub in hub_rules.json")
ax.set_xlabel("Zone name")
ax.set_ylabel("Hubs that list this zone")
plt.tight_layout()
fig.savefig(os.path.join(IMG, "06_zone_tags_in_rules.png"))
plt.close()

print("saved 6 charts to", IMG)