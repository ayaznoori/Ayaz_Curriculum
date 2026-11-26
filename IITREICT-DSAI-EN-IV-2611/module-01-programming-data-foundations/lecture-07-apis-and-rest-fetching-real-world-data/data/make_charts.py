#!/usr/bin/env python3
import json
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "images"
IMG.mkdir(parents=True, exist_ok=True)

data = json.loads((Path(__file__).parent / "bus_departures.json").read_text())["departures"]

def save_bar(labels, values, title, fname, ylabel):
    plt.figure(figsize=(9, 4.5), dpi=200)
    plt.bar(labels, values, color="#2563eb")
    plt.title(title, fontsize=14)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(IMG / fname)
    plt.close()

st04 = sorted([d for d in data if d["stop_id"] == "ST04"], key=lambda x: (x["eta_min"], x["trip_id"]))[:5]
save_bar(
    [d["trip_id"] for d in st04],
    [d["eta_min"] for d in st04],
    "ETA minutes for five Koramangala departures (invented)",
    "01_st04_eta_bar.png",
    "Minutes until bus",
)

status5 = Counter(d["status"] for d in st04)
save_bar(
    list(status5.keys()),
    list(status5.values()),
    "Status mix in the Koramangala sample of five",
    "02_st04_status_bar.png",
    "Bus count",
)

all_status = Counter(d["status"] for d in data)
save_bar(
    list(all_status.keys()),
    list(all_status.values()),
    "Status mix across 120 invented departures",
    "03_all_status_bar.png",
    "Row count",
)

save_bar(
    ["200 ok", "401 no key", "404 bad stop"],
    [3, 1, 1],
    "Status codes used in today's notebook checks",
    "04_status_codes_bar.png",
    "Times shown",
)

usable = [d for d in st04 if d["status"] != "cancelled"]
save_bar(
    ["raw rows", "after drop cancelled"],
    [len(st04), len(usable)],
    "Rows kept after removing cancelled buses",
    "05_usable_rows_bar.png",
    "Row count",
)

routes = Counter(d["route_name"] for d in data).most_common(5)
save_bar(
    [r[0] for r in routes],
    [r[1] for r in routes],
    "Top five route names in 120 departures",
    "06_top_routes_bar.png",
    "Departure count",
)

print("wrote charts to", IMG)