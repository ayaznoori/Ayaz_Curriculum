"""Generate 120 campus snack order rows (seed 261204). Run once to refresh SQL/CSV."""
import csv
import random
from datetime import date, timedelta

random.seed(261204)
BASE = "/Users/masai/Documents/AIML courses./IITREICT-AIML-EN-III-2611/module-02-sql-for-data-analysis/lecture-01-databases-and-the-sql-landscape-select-basics/data"

SNACKS = [
    ("samosa", 25),
    ("kachori", 30),
    ("masala chai", 15),
    ("filter coffee", 20),
    ("vada pav", 35),
    ("veg sandwich", 45),
    ("mango juice", 40),
    ("butter cookie", 12),
    ("namkeen mix", 28),
    ("veg muffin", 38),
]
BLOCKS = ["BLOCK-A", "BLOCK-B", "BLOCK-C"]
START = date(2025, 11, 1)

rows = []
for order_id in range(1, 121):
    snack_name, unit_price = random.choice(SNACKS)
    # planned edge: smallest qty 1, largest 8; price repeats for DISTINCT demos
    if order_id == 1:
        qty, snack_name, unit_price = 1, "samosa", 25
    elif order_id == 2:
        qty, snack_name, unit_price = 8, "veg muffin", 38
    elif order_id == 3:
        qty, snack_name, unit_price = 2, "samosa", 25
    elif order_id == 7:
        qty, snack_name, unit_price = 5, "masala chai", 15
    elif order_id == 50:
        qty, snack_name, unit_price = 4, "kachori", 30
    else:
        qty = random.randint(1, 5)
    block_code = BLOCKS[(order_id + qty) % 3]
    order_date = START + timedelta(days=(order_id * 2) % 24)
    rows.append((order_id, snack_name, qty, unit_price, block_code, order_date.isoformat()))

csv_path = f"{BASE}/campus_snack_orders.csv"
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["order_id", "snack_name", "qty", "unit_price_rupees", "block_code", "order_date"])
    w.writerows(rows)

sql_path = f"{BASE}/campus_snack_orders.sql"
with open(sql_path, "w", encoding="utf-8") as f:
    f.write("DROP TABLE IF EXISTS campus_snack_orders;\n")
    f.write(
        "CREATE TABLE campus_snack_orders (\n"
        "  order_id INTEGER PRIMARY KEY,\n"
        "  snack_name TEXT NOT NULL,\n"
        "  qty INTEGER NOT NULL,\n"
        "  unit_price_rupees INTEGER NOT NULL,\n"
        "  block_code TEXT NOT NULL,\n"
        "  order_date TEXT NOT NULL\n"
        ");\n"
    )
    for r in rows:
        f.write(
            "INSERT INTO campus_snack_orders VALUES "
            f"({r[0]}, '{r[1]}', {r[2]}, {r[3]}, '{r[4]}', '{r[5]}');\n"
        )

print(len(rows), "rows written")