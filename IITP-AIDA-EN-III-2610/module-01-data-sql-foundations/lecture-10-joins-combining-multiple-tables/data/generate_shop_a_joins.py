#!/usr/bin/env python3
"""One-off generator, fixed seed 261010. Writes four related Seller A tables (CSV + one SQL file).

Edge cases planned on purpose:
  * 120 order rows; product_id repeats (popular items appear many times)
  * 3 orders point to retired product ids 41 and 42 (no row in the catalog)
  * 4 guest orders with a blank buyer_id
  * 6 catalog products that were never ordered
  * 5 buyers who never ordered
  * 1 category (Jacket) with no products yet
"""
import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(261010)
HERE = Path(__file__).resolve().parent

categories = [
    (1, "Kurta"), (2, "Tee"), (3, "Dupatta"), (4, "Saree"),
    (5, "Jeans"), (6, "Shoes"), (7, "Bag"), (8, "Jacket"),
]

catalog = [
    (1, "Cotton Kurta Red", 1, 499), (2, "Linen Kurta Blue", 1, 650),
    (3, "Festival Kurta Green", 1, 799), (4, "Printed Kurti Yellow", 1, 549),
    (5, "Straight Kurta Black", 1, 599), (6, "Round Neck Tee White", 2, 299),
    (7, "Graphic Tee Black", 2, 349), (8, "Polo T-Shirt Green", 2, 449),
    (9, "Silk Dupatta Gold", 3, 450), (10, "Cotton Dupatta Pink", 3, 275),
    (11, "Zari Silk Saree Maroon", 4, 1899), (12, "Cotton Saree Blue", 4, 999),
    (13, "Slim Fit Jeans Blue", 5, 899), (14, "Straight Jeans Black", 5, 949),
    (15, "Casual Sneakers Black", 6, 799), (16, "Running Shoes White", 6, 1199),
    (17, "Canvas Backpack Navy", 7, 1299), (18, "Laptop Sling Bag Grey", 7, 1099),
    (19, "Linen Kurta Beige", 1, 699), (20, "Festival Kurta Orange", 1, 849),
    (21, "Striped Tee Navy", 2, 379), (22, "Printed Dupatta Red", 3, 325),
    (23, "Silk Saree Green", 4, 2499), (24, "Denim Jeans Grey", 5, 999),
    (25, "Trail Sneakers Blue", 6, 1399), (26, "Mini Backpack Pink", 7, 899),
    (27, "Cotton Kurta White", 1, 479), (28, "Oversized Tee Cream", 2, 399),
    (29, "Block Print Dupatta Blue", 3, 375), (30, "Tote Bag Beige", 7, 599),
]
UNSOLD = {12, 18, 23, 26, 28, 30}          # catalog rows with no orders
sold_ids = [p[0] for p in catalog if p[0] not in UNSOLD]

cities = ["PNQ", "BLR", "MUM", "DEL", "HYD"]
first = ["Ananya", "Priya", "Karthik", "Meera", "Rohan", "Sneha", "Vikram", "Divya", "Arjun",
         "Kavya", "Imran", "Neha", "Suresh", "Pooja", "Farah", "Nikhil", "Lakshmi", "Harsh"]
last = ["Rao", "Das", "Menon", "Iyer", "Shah", "Nair", "Patel", "Khan", "Reddy", "Joshi",
        "Singh", "Gupta"]
buyers = []
used = set()
bid = 1
while bid <= 36:
    nm = f"{random.choice(first)} {random.choice(last)}"
    if nm in used:
        continue
    used.add(nm)
    buyers.append((bid, nm, random.choice(cities)))
    bid += 1
NO_ORDER_BUYERS = {9, 17, 24, 31, 35}
active_buyers = [b[0] for b in buyers if b[0] not in NO_ORDER_BUYERS]

# product weights: first few products are bestsellers so the key repeats a lot
weights = {pid: 1 for pid in sold_ids}
for pid, w in {1: 9, 2: 7, 6: 6, 3: 5, 15: 4, 13: 4, 9: 3, 17: 3}.items():
    weights[pid] = w

ORPHAN_ROWS = {23: 41, 58: 41, 97: 42}      # order_id -> retired product id
GUEST_ROWS = {12, 44, 71, 109}              # order_id with blank buyer_id

orders = []
start = date(2026, 2, 1)
for oid in range(1, 121):
    if oid in ORPHAN_ROWS:
        pid = ORPHAN_ROWS[oid]
    else:
        pid = random.choices(sold_ids, weights=[weights[p] for p in sold_ids])[0]
    buyer = None if oid in GUEST_ROWS else random.choice(active_buyers)
    qty = random.choices([1, 2, 3], weights=[6, 3, 1])[0]
    odate = start + timedelta(days=(oid * 40) // 120 + random.randint(0, 1))
    orders.append((oid, "SHOP-A", pid, buyer, qty, odate.isoformat()))

# make sure every sold product appears at least once (swap a row of a busy product)
from collections import Counter
for pid in sold_ids:
    if all(o[2] != pid for o in orders):
        cnt = Counter(o[2] for o in orders)
        slot = next(i for i, o in enumerate(orders)
                    if o[2] not in (41, 42) and cnt[o[2]] >= 4 and i > 5)
        o = orders[slot]
        orders[slot] = (o[0], o[1], pid, o[3], o[4], o[5])

# make sure every active buyer ordered at least once
seen = {o[3] for o in orders if o[3] is not None}
missing = [b for b in active_buyers if b not in seen]
for b in missing:
    bc = Counter(o[3] for o in orders if o[3] is not None)
    slot = next(i for i, o in enumerate(orders)
                if o[3] is not None and bc[o[3]] >= 4 and o[2] not in (41, 42))
    o = orders[slot]
    orders[slot] = (o[0], o[1], o[2], b, o[4], o[5])


def write_csv(name, header, rows):
    with open(HERE / name, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in rows:
            w.writerow(["" if v is None else v for v in r])


write_csv("shop_a_categories.csv", ["category_id", "category_name"], categories)
write_csv("shop_a_catalog.csv", ["product_id", "title", "category_id", "price_rupees"], catalog)
write_csv("shop_a_buyers.csv", ["buyer_id", "buyer_name", "city_code"], buyers)
write_csv("shop_a_orders.csv",
          ["order_id", "shop_code", "product_id", "buyer_id", "qty", "order_date"], orders)


def lit(v):
    if v is None:
        return "NULL"
    if isinstance(v, int):
        return str(v)
    return "'" + str(v).replace("'", "''") + "'"


ddl = {
    "shop_a_categories": """CREATE TABLE shop_a_categories (
  category_id INT PRIMARY KEY,
  category_name VARCHAR(20) NOT NULL
);""",
    "shop_a_catalog": """CREATE TABLE shop_a_catalog (
  product_id INT PRIMARY KEY,
  title VARCHAR(40) NOT NULL,
  category_id INT NOT NULL,
  price_rupees INT NOT NULL
);""",
    "shop_a_buyers": """CREATE TABLE shop_a_buyers (
  buyer_id INT PRIMARY KEY,
  buyer_name VARCHAR(40) NOT NULL,
  city_code CHAR(3) NOT NULL
);""",
    "shop_a_orders": """CREATE TABLE shop_a_orders (
  order_id INT PRIMARY KEY,
  shop_code VARCHAR(10) NOT NULL,
  product_id INT NOT NULL,
  buyer_id INT NULL,
  qty INT NOT NULL,
  order_date DATE NOT NULL
);""",
}
data = {
    "shop_a_categories": categories, "shop_a_catalog": catalog,
    "shop_a_buyers": buyers, "shop_a_orders": orders,
}
parts = ["-- Seller A join practice tables, invented for teaching (SQLite or MySQL 8.0)."]
for t in ["shop_a_categories", "shop_a_catalog", "shop_a_buyers", "shop_a_orders"]:
    parts.append(f"DROP TABLE IF EXISTS {t};")
    parts.append(ddl[t])
    for r in data[t]:
        parts.append(f"INSERT INTO {t} VALUES ({', '.join(lit(v) for v in r)});")
    parts.append("")
(HERE / "shop_a_joins.sql").write_text("\n".join(parts), encoding="utf-8")
print("orders", len(orders), "catalog", len(catalog), "buyers", len(buyers), "categories", len(categories))
