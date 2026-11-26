#!/usr/bin/env python3
"""Generate 120 invented bus departure rows (seed 261107). Run once to refresh CSV/JSON."""
import csv
import json
import random
from pathlib import Path

SEED = 261107
random.seed(SEED)

STOPS = [
    ("ST01", "MG Road"),
    ("ST02", "Indiranagar"),
    ("ST03", "Whitefield"),
    ("ST04", "Koramangala"),
    ("ST05", "Electronic City"),
    ("ST06", "Hebbal"),
    ("ST07", "Jayanagar"),
    ("ST08", "Yelahanka"),
    ("ST09", "Banashankari"),
    ("ST10", "Marathahalli"),
    ("ST11", "Peenya"),
    ("ST12", "Silk Board"),
]

ROUTES = [
    ("R101", "500A"),
    ("R102", "335E"),
    ("R103", "201"),
    ("R104", "V-500"),
    ("R105", "KIA-14"),
    ("R106", "356"),
    ("R107", "401"),
    ("R108", "MF-1"),
    ("R109", "500K"),
    ("R110", "303"),
]

STATUS_POOL = ["on_time"] * 70 + ["delayed"] * 35 + ["cancelled"] * 15

rows = []
for i in range(1, 121):
    stop_id, stop_name = random.choice(STOPS)
    route_id, route_name = random.choice(ROUTES)
    status = random.choice(STATUS_POOL)
    eta_min = 0 if i in (17, 44, 88) else random.randint(1, 42)
    if i in (5, 29, 61, 92, 103, 111, 118, 120):
        status = "cancelled"
        eta_min = random.randint(8, 30)
    delay_min = random.randint(3, 18) if status == "delayed" else 0
    rows.append(
        {
            "trip_id": f"T{i:03d}",
            "stop_id": stop_id,
            "stop_name": stop_name,
            "route_id": route_id,
            "route_name": route_name,
            "eta_min": eta_min,
            "status": status,
            "delay_min": delay_min,
        }
    )

here = Path(__file__).resolve().parent
with (here / "bus_departures.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)

with (here / "bus_departures.json").open("w", encoding="utf-8") as f:
    json.dump({"departures": rows, "count": len(rows)}, f, indent=2)

print(len(rows), "rows written")