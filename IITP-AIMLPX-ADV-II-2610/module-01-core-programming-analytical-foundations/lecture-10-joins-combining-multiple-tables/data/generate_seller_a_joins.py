"""Build the Seller A join tables (invented for teaching). Fixed seed, three tables.

Writes seller_a_products.csv, seller_a_buyers.csv, seller_a_orders.csv and seller_a_joins.sql.
Run: python3 generate_seller_a_joins.py
"""
import csv
import random
from pathlib import Path

HERE = Path(__file__).parent
rng = random.Random(2610)

PRODUCTS = [
    (1, "KRT-0412-RD", "Cotton Kurta Red", "kurta", 499),
    (2, "KRT-0891-BL", "Linen Kurta Blue", "kurta", 650),
    (3, "KRT-1104-GR", "Festival Kurta Green", "kurta", 799),
    (4, "KRT-1153-YL", "Festival Kurta Yellow", "kurta", 749),
    (5, "KRT-1320-WH", "Chikankari Kurta White", "kurta", 1199),
    (6, "KRT-1402-MR", "Maroon Silk Kurta", "kurta", 1499),
    (7, "DUP-3300-GL", "Silk Dupatta Gold", "dupatta", 450),
    (8, "DUP-4228-YL", "Cotton Dupatta Yellow", "dupatta", 249),
    (9, "DUP-4410-PK", "Net Dupatta Pink", "dupatta", 349),
    (10, "DUP-4502-BL", "Block Print Dupatta", "dupatta", 399),
    (11, "TOP-2201-WH", "Cotton Top White", "top", 299),
    (12, "TOP-2250-BK", "Cotton Top Black", "top", 329),
    (13, "TOP-2318-RD", "Ruffle Top Red", "top", 549),
    (14, "TOP-2390-GR", "Linen Top Green", "top", 599),
    (15, "JNS-0688-BL", "Straight Jeans Blue", "jeans", 899),
    (16, "JNS-0780-BK", "Slim Fit Jeans Black", "jeans", 1299),
    (17, "JNS-4736-GY", "Slim Fit Jeans Grey", "jeans", 999),
    (18, "JNS-5120-LB", "Wide Leg Jeans", "jeans", 1099),
    (19, "BAG-1670-BL", "Canvas Backpack", "bag", 1299),
    (20, "BAG-1702-TN", "Tote Bag Tan", "bag", 699),
    (21, "BAG-1788-BK", "Sling Bag Black", "bag", 799),
    (22, "BAG-1811-GR", "Laptop Sleeve Grey", "bag", 499),
    (23, "SHO-0789-BK", "Casual Sneakers Black", "shoes", 799),
    (24, "SHO-1519-WH", "Running Shoes White", "shoes", 1199),
    (25, "SHO-1620-BR", "Leather Sandals Brown", "shoes", 899),
    (26, "SHO-1702-RD", "Kolhapuri Chappal Red", "shoes", 649),
    (27, "SHO-1811-GL", "Gold Juttis", "shoes", 549),
    (28, "KRT-1555-OR", "Orange Anarkali Kurta", "kurta", 1799),
    (29, "DUP-4620-GR", "Georgette Dupatta Green", "dupatta", 299),
    (30, "TOP-2455-LV", "Lavender Crop Top", "top", 449),
]
NEVER_ORDERED = {6, 14, 21, 27, 30}
DELISTED = [31, 31, 31, 32]  # four orders point to products no longer in the catalog

FIRST = ["Ananya", "Priya", "Karthik", "Meera", "Neha", "Dev", "Rohan", "Pooja", "Rahul",
         "Divya", "Arjun", "Sneha", "Vikram", "Isha", "Kabir", "Tara", "Aditya", "Nisha"]
LAST = ["Rao", "Das", "Menon", "Iyer", "Chawla", "Shah", "Nair", "Singh", "Patel", "Khan"]
CITIES = ["Pune", "Bengaluru", "Mumbai", "Delhi", "Chennai", "Hyderabad", "Kolkata", "Ahmedabad"]
NO_ORDER_BUYERS = {5, 12, 20, 33}


def build():
    buyers, seen = [], set()
    while len(buyers) < 36:
        name = f"{rng.choice(FIRST)} {rng.choice(LAST)}"
        if name in seen:
            continue
        seen.add(name)
        buyers.append((len(buyers) + 1, name, CITIES[len(buyers) % len(CITIES)]))

    ordered = [p[0] for p in PRODUCTS if p[0] not in NEVER_ORDERED]  # 25 products
    pids = list(ordered)                       # every ordered product at least once
    pids += [1] * 11                           # product 1 is the best seller (12 orders)
    pids += [2] * 5 + [7] * 4 + [11] * 3
    while len(pids) < 116:
        pids.append(rng.choice(ordered))
    pids += DELISTED
    rng.shuffle(pids)

    active_buyers = [b[0] for b in buyers if b[0] not in NO_ORDER_BUYERS]
    guest_slots = set(rng.sample([i for i, p in enumerate(pids) if p < 31], 5))
    orders = []
    for i, pid in enumerate(pids):
        buyer = "" if i in guest_slots else rng.choice(active_buyers)
        day = rng.randint(0, 41)
        month, dom = (2, 1 + day) if day < 28 else (3, day - 27)
        orders.append((1001 + i, buyer, pid, rng.randint(1, 3), f"2026-{month:02d}-{dom:02d}"))
    return buyers, orders


def write_csv(name, header, rows):
    with (HERE / name).open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def q(v):
    if v == "":
        return "NULL"
    return str(v) if isinstance(v, int) else "'" + str(v).replace("'", "''") + "'"


def write_sql(buyers, orders):
    out = [
        "DROP TABLE IF EXISTS seller_a_orders;",
        "DROP TABLE IF EXISTS seller_a_products;",
        "DROP TABLE IF EXISTS seller_a_buyers;",
        "CREATE TABLE seller_a_products (\n  product_id INT PRIMARY KEY,\n  product_code VARCHAR(20) NOT NULL,\n"
        "  title VARCHAR(40) NOT NULL,\n  category VARCHAR(10) NOT NULL,\n  price_rupees INT NOT NULL\n);",
        "CREATE TABLE seller_a_buyers (\n  buyer_id INT PRIMARY KEY,\n  buyer_name VARCHAR(40) NOT NULL,\n"
        "  city VARCHAR(20) NOT NULL\n);",
        "CREATE TABLE seller_a_orders (\n  order_id INT PRIMARY KEY,\n  buyer_id INT NULL,\n  product_id INT NOT NULL,\n"
        "  quantity INT NOT NULL,\n  order_date DATE NOT NULL\n);",
        "",
    ]
    for tbl, rows in (("seller_a_products", PRODUCTS), ("seller_a_buyers", buyers), ("seller_a_orders", orders)):
        for r in rows:
            out.append(f"INSERT INTO {tbl} VALUES ({', '.join(q(v) for v in r)});")
        out.append("")
    (HERE / "seller_a_joins.sql").write_text("\n".join(out), encoding="utf-8")


if __name__ == "__main__":
    buyers, orders = build()
    write_csv("seller_a_products.csv", ["product_id", "product_code", "title", "category", "price_rupees"], PRODUCTS)
    write_csv("seller_a_buyers.csv", ["buyer_id", "buyer_name", "city"], buyers)
    write_csv("seller_a_orders.csv", ["order_id", "buyer_id", "product_id", "quantity", "order_date"], orders)
    write_sql(buyers, orders)
    print(len(PRODUCTS), len(buyers), len(orders))
