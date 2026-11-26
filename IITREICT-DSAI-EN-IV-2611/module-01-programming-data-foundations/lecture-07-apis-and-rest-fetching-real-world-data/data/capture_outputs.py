#!/usr/bin/env python3
"""Mirror lecture notebook cells (route_get + httpbin) for pasted outputs."""
import os
import requests
from mock_bus_api import VALID_KEY, route_get

os.chdir(os.path.dirname(os.path.abspath(__file__)))

API_KEY = VALID_KEY
BASE = "http://127.0.0.1:18765"


def show_get(url, headers=None, params=None):
    code, body = route_get(url.replace(BASE, ""), headers, params)
    print("status", code)
    if body.get("departures"):
        print("count", body["count"], "stop", body.get("stop_name", ""))
    elif "error" in body:
        print(body)
    else:
        print("json keys", sorted(body.keys()))


print("=== T1 health ===")
show_get(BASE + "/v1/health")

print("\n=== T1 no key ===")
show_get(BASE + "/v1/stops/ST04/departures")

print("\n=== T2 GET with params ===")
path = "/v1/stops/ST04/departures"
params = {"limit": 5}
code, body = route_get(path, {"X-Bus-Key": API_KEY}, params)
full_url = BASE + path + "?limit=5"
print("url", full_url)
print("status", code)
print("count", body["count"], "stop", body["stop_name"])
first = body["departures"][0]
print(first["trip_id"], first["route_name"], first["eta_min"], first["status"])

print("\n=== T3 env key ===")
import os as _os

_os.environ["BUS_API_KEY"] = API_KEY
key = _os.environ.get("BUS_API_KEY", "")
code3, body3 = route_get(path, {"X-Bus-Key": key}, {"limit": 3})
print("status", code3, "rows", body3["count"])

print("\n=== T4 dataset ===")
usable = []
for item in body3["departures"]:
    if item["status"] != "cancelled":
        usable.append(
            {"trip": item["trip_id"], "route": item["route_name"], "eta": item["eta_min"]}
        )
print("usable", len(usable))
for row in usable:
    print(row)

delayed = [row for row in usable if row["eta"] >= 10]
print("delayed_or_far", len(delayed))

print("\n=== httpbin status demo ===")
r = requests.get("https://httpbin.org/status/200", timeout=15)
print("200 demo", r.status_code)
r2 = requests.get("https://httpbin.org/status/401", timeout=15)
print("401 demo", r2.status_code)

print("\n=== ST99 ===")
code99, body99 = route_get(
    "/v1/stops/ST99/departures", {"X-Bus-Key": API_KEY}, {"limit": 5}
)
print("status", code99, body99)

all5 = body["departures"]
print("sample5 on_time", sum(1 for x in all5 if x["status"] == "on_time"))
print("sample5 cancelled", sum(1 for x in all5 if x["status"] == "cancelled"))