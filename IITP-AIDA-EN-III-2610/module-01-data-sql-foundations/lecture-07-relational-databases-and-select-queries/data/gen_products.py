#!/usr/bin/env python3
"""One-off generator — fixed seed 261007, 100 product rows for lecture 07."""
import csv
import random
from datetime import date, timedelta

random.seed(261007)

PREFIXES = {
    "KRT": ("kurta", ["Cotton Kurta", "Printed Kurti", "Straight Kurta", "Festival Kurta", "Linen Kurta"]),
    "TEE": ("tee", ["Round Neck Tee", "Graphic Tee", "Polo T-Shirt"]),
    "DUP": ("dupatta", ["Silk Dupatta", "Cotton Dupatta"]),
    "SAR": ("saree", ["Silk Saree", "Cotton Saree", "Zari Silk Saree"]),
    "JNS": ("jeans", ["Slim Fit Jeans", "Men's Denim Jeans"]),
    "SHO": ("shoes", ["Running Shoes", "Casual Sneakers"]),
    "BAG": ("bag", ["Canvas Backpack", "Laptop Sling Bag"]),
}

SHOPS = ["SHOP-A"] * 62 + ["SHOP-B"] * 38
random.shuffle(SHOPS)

rows = []
used_codes = set()

# Anchor rows from pre-read (ids 1-5)
anchors = [
    (1, "KRT-0412-RD", "Cotton Kurta Red", 499, "SHOP-A", "kurta", "2025-03-08"),
    (2, "KRT-0891-BL", "Linen Kurta Blue", 650, "SHOP-A", "kurta", "2025-03-15"),
    (3, "TOP-2201-WH", "Cotton Top White", 299, "SHOP-B", "top", "2025-02-20"),
    (4, "KRT-1104-GR", "Festival Kurta Green", 799, "SHOP-A", "kurta", "2025-04-02"),
    (5, "DUP-3300-GL", "Silk Dupatta Gold", 450, "SHOP-A", "dupatta", "2025-03-22"),
]
for a in anchors:
    rows.append(
        {
            "product_id": a[0],
            "product_code": a[1],
            "title": a[2],
            "price_rupees": a[3],
            "shop_code": a[4],
            "category": a[5],
            "listed_date": a[6],
        }
    )
    used_codes.add(a[1])

march_start = date(2025, 3, 1)
april_end = date(2025, 4, 30)

null_price_ids = {28, 41, 67, 88}  # four SHOP-A blanks

for pid in range(6, 101):
    shop = SHOPS[pid - 6]
    pre = random.choice(list(PREFIXES.keys()))
    cat, titles = PREFIXES[pre]
    num = random.randint(100, 4999)
    col = random.choice(["RD", "BL", "WH", "GN", "BK", "YL"])
    code = f"{pre}-{num:04d}-{col}"
    while code in used_codes:
        num += 1
        code = f"{pre}-{num:04d}-{col}"
    used_codes.add(code)
    title = random.choice(titles)
    if pre == "KRT" and random.random() < 0.3:
        title = title + " " + random.choice(["Red", "Blue", "Green", "Gold"])
    if pid in (15, 22, 55):
        price = 499  # tied prices
    elif pid == 12:
        price = 49
    elif pid == 13:
        price = 4999
    elif pid in null_price_ids and shop == "SHOP-A":
        price = None
    else:
        price = random.choice([149, 199, 249, 299, 349, 399, 449, 499, 549, 599, 649, 699, 749, 799, 899, 999, 1299])
    if pid % 7 == 0 and shop == "SHOP-A":
        listed = march_start + timedelta(days=random.randint(0, 30))
    else:
        listed = march_start + timedelta(days=random.randint(-20, 59))
        if listed > april_end:
            listed = april_end - timedelta(days=random.randint(0, 5))
    rows.append(
        {
            "product_id": pid,
            "product_code": code,
            "title": title,
            "price_rupees": price,
            "shop_code": shop,
            "category": cat if code != "TOP-2201-WH" else "top",
            "listed_date": listed.isoformat(),
        }
    )

rows.sort(key=lambda r: r["product_id"])

base = __file__.replace("gen_products.py", "")
csv_path = base + "shop_a_products.csv"
sql_path = base + "shop_a_products.sql"

with open(csv_path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
        fieldnames=["product_id", "product_code", "title", "price_rupees", "shop_code", "category", "listed_date"],
    )
    w.writeheader()
    for r in rows:
        out = dict(r)
        if out["price_rupees"] is None:
            out["price_rupees"] = ""
        w.writerow(out)

lines = [
    "DROP TABLE IF EXISTS shop_a_products;",
    "CREATE TABLE shop_a_products (",
    "  product_id INT PRIMARY KEY,",
    "  product_code VARCHAR(20) NOT NULL,",
    "  title VARCHAR(80) NOT NULL,",
    "  price_rupees INT NULL,",
    "  shop_code VARCHAR(10) NOT NULL,",
    "  category VARCHAR(20) NOT NULL,",
    "  listed_date DATE NOT NULL",
    ");",
    "",
]
for r in rows:
    pr = "NULL" if r["price_rupees"] is None else str(r["price_rupees"])
    title = r["title"].replace("'", "''")
    lines.append(
        f"INSERT INTO shop_a_products VALUES ({r['product_id']}, '{r['product_code']}', "
        f"'{title}', {pr}, '{r['shop_code']}', '{r['category']}', '{r['listed_date']}');"
    )

with open(sql_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

shop_a = sum(1 for r in rows if r["shop_code"] == "SHOP-A")
nulls = sum(1 for r in rows if r["price_rupees"] is None)
print(len(rows), "rows", shop_a, "SHOP-A", nulls, "null prices")