#!/usr/bin/env python3
"""Run cumulative Colab-style blocks for lecture output capture."""
import os
import sys
import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.getcwd())

import requests
from mock_bus_api import VALID_KEY, boot_background, HOST, PORT

BASE = f"http://{HOST}:{PORT}"
API_KEY = VALID_KEY

print("=== Block 0: boot server ===")
boot_background()
time.sleep(0.4)
print("mock bus API ready")

print("\n=== Topic 1 Example: health check ===")
r = requests.get(BASE + "/v1/health")
print("status", r.status_code)
print("json keys", sorted(r.json().keys()))

print("\n=== Topic 1 Extending: bad path ===")
r2 = requests.get(BASE + "/v1/stops/ST04/departures")
print("status", r2.status_code)
print(r2.json())

print("\n=== Topic 2 Example: GET with key ===")
headers = {"X-Bus-Key": API_KEY}
url = BASE + "/v1/stops/ST04/departures"
params = {"limit": 5}
r3 = requests.get(url, headers=headers, params=params)
print("url", r3.url)
print("status", r3.status_code)
body = r3.json()
print("count", body["count"], "stop", body["stop_name"])

print("\n=== Topic 2 Extending: inspect first row ===")
first = body["departures"][0]
print(first["trip_id"], first["route_name"], first["eta_min"], first["status"])

print("\n=== Topic 3 Example: no key ===")
r4 = requests.get(BASE + "/v1/stops/ST04/departures", params={"limit": 3})
print("status", r4.status_code, r4.json()["error"])

print("\n=== Topic 3 Extending: env-style key ===")
import os as _os

_os.environ["BUS_API_KEY"] = API_KEY
key = _os.environ.get("BUS_API_KEY", "")
r5 = requests.get(
    BASE + "/v1/stops/ST04/departures",
    headers={"X-Bus-Key": key},
    params={"limit": 3},
)
print("status", r5.status_code, "rows", r5.json()["count"])

print("\n=== Topic 4 Example: list of dicts ===")
rows = r5.json()["departures"]
usable = []
for item in rows:
    if item["status"] != "cancelled":
        usable.append(
            {
                "trip": item["trip_id"],
                "route": item["route_name"],
                "eta": item["eta_min"],
            }
        )
print("usable", len(usable))
for row in usable:
    print(row)

print("\n=== Topic 4 Extending: loop filter delayed ===")
delayed = [row for row in usable if row["eta"] >= 10]
print("delayed_or_far", len(delayed))

print("\n=== Closing: ST99 404 ===")
r6 = requests.get(
    BASE + "/v1/stops/ST99/departures",
    headers={"X-Bus-Key": API_KEY},
    params={"limit": 5},
)
print("status", r6.status_code, r6.json())

print("\n=== Closing stats ===")
r7 = requests.get(
    BASE + "/v1/stops/ST04/departures",
    headers={"X-Bus-Key": API_KEY},
    params={"limit": 5},
)
all_rows = r7.json()["departures"]
on_time = sum(1 for x in all_rows if x["status"] == "on_time")
cancelled = sum(1 for x in all_rows if x["status"] == "cancelled")
print("sample5 on_time", on_time, "cancelled", cancelled)