#!/usr/bin/env python3
"""Draw the six lecture charts from the SAME tables the SQL runs on (mentor tool, not for learners).

Run from this folder:  /tmp/lecvenv/bin/python3 make_charts.py
"""
import sqlite3
import subprocess
import tempfile
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
SQL_FILE = HERE.parent / "data" / "shop_a_joins.sql"

BLUE, GREEN, AMBER, PURPLE, RED, GREY = "#2563eb", "#16a34a", "#d97706", "#7c3aed", "#dc2626", "#94a3b8"

db = sqlite3.connect(":memory:")
db.executescript(SQL_FILE.read_text(encoding="utf-8"))


def one(sql):
    return db.execute(sql).fetchone()[0]


def rows(sql):
    return db.execute(sql).fetchall()


JOIN = "shop_a_orders AS o {kind} JOIN shop_a_catalog AS p ON p.product_id = o.product_id"
n_orders = one("SELECT COUNT(*) FROM shop_a_orders")
inner = one("SELECT COUNT(*) FROM " + JOIN.format(kind="INNER"))
left = one("SELECT COUNT(*) FROM " + JOIN.format(kind="LEFT"))
right = one("SELECT COUNT(*) FROM " + JOIN.format(kind="RIGHT"))
full = one("SELECT COUNT(*) FROM " + JOIN.format(kind="FULL OUTER"))
orph = left - inner
unsold = right - inner
assert (n_orders, inner, left, right, full) == (120, 117, 120, 123, 126)


def save(fig, name):
    fig.tight_layout()
    fig.savefig(HERE / name, dpi=200)
    plt.close(fig)


def label_bars(ax, bars, fmt="{:.0f}", dy=1):
    for b in bars:
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + dy, fmt.format(b.get_height()),
                ha="center", va="bottom", fontsize=11, fontweight="bold")


# 1 orders matched vs missing
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(["Order rows", "Matched to a\ncatalog row", "No catalog row\n(dropped by INNER JOIN)"],
              [n_orders, inner, orph], color=[BLUE, GREEN, RED])
label_bars(ax, bars, dy=1.5)
ax.set_ylabel("Rows")
ax.set_ylim(0, 140)
ax.set_title("Seller A SHOP-A: INNER JOIN of orders to catalog loses 3 of 120 orders")
save(fig, "01_orders_matched_vs_missing.png")

# 2 rows by join type (stacked)
fig, ax = plt.subplots(figsize=(9, 5))
names = ["INNER", "LEFT", "RIGHT", "FULL OUTER"]
matched = [inner] * 4
extra_orders = [0, orph, 0, orph]
extra_products = [0, 0, unsold, unsold]
ax.bar(names, matched, color=GREEN, label="Matched pairs (117)")
ax.bar(names, extra_orders, bottom=matched, color=RED, label="Orders with no product (3)")
bottom2 = [m + e for m, e in zip(matched, extra_orders)]
ax.bar(names, extra_products, bottom=bottom2, color=AMBER, label="Products with no order (6)")
for i, tot in enumerate([inner, left, right, full]):
    ax.text(i, tot + 1.5, str(tot), ha="center", fontsize=12, fontweight="bold")
ax.set_ylim(0, 165)
ax.set_ylabel("Rows returned")
ax.set_title("Seller A SHOP-A: rows returned by each join type (orders and catalog)")
ax.legend(loc="upper left", fontsize=9, ncol=3)
save(fig, "02_rows_by_join_type.png")

# 3 unmatched rows by side
guest = one("SELECT COUNT(*) FROM shop_a_orders WHERE buyer_id IS NULL")
quiet_buyers = one("SELECT COUNT(*) FROM shop_a_buyers b LEFT JOIN shop_a_orders o ON o.buyer_id=b.buyer_id WHERE o.order_id IS NULL")
labels = ["Orders with no product", "Products with no order", "Orders with no buyer id (guests)", "Buyers with no order"]
vals = [orph, unsold, guest, quiet_buyers]
assert vals == [3, 6, 4, 5]
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.barh(labels[::-1], vals[::-1], color=[PURPLE, AMBER, BLUE, RED][::-1])
for b in bars:
    ax.text(b.get_width() + 0.1, b.get_y() + b.get_height() / 2, f"{b.get_width():.0f}", va="center",
            fontsize=12, fontweight="bold")
ax.set_xlim(0, 7.5)
ax.set_xlabel("Unmatched rows found with LEFT JOIN ... IS NULL")
ax.set_title("Seller A SHOP-A: unmatched rows on each side")
save(fig, "03_unmatched_rows_by_side.png")

# 4 orders per product (top 8)
top = rows("SELECT p.product_id, COUNT(o.order_id) n FROM shop_a_catalog p JOIN shop_a_orders o "
           "ON o.product_id=p.product_id GROUP BY p.product_id ORDER BY n DESC, p.product_id LIMIT 8")
assert top[0] == (1, 22)
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar([f"Product {p}" for p, _ in top], [n for _, n in top],
              color=[AMBER] + [BLUE] * 7)
label_bars(ax, bars, dy=0.3)
ax.set_ylabel("Order rows for that product_id")
ax.set_ylim(0, 26)
ax.set_title("Seller A SHOP-A: one catalog row meets many order rows (product 1 gives 22)")
plt.setp(ax.get_xticklabels(), fontsize=9)
save(fig, "04_orders_per_product.png")

# 5 orders per category with Jacket
cat = rows("SELECT c.category_name, COUNT(o.order_id) n FROM shop_a_categories c "
           "LEFT JOIN shop_a_catalog p ON p.category_id=c.category_id "
           "LEFT JOIN shop_a_orders o ON o.product_id=p.product_id "
           "GROUP BY c.category_name ORDER BY n DESC, c.category_name")
assert len(cat) == 8 and cat[-1] == ("Jacket", 0) and sum(n for _, n in cat) == 117
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar([c for c, _ in cat], [n for _, n in cat], color=[BLUE] * 7 + [RED])
label_bars(ax, bars, dy=0.6)
ax.set_ylabel("Orders (COUNT of order_id)")
ax.set_ylim(0, 52)
ax.set_title("Seller A SHOP-A: LEFT JOIN keeps Jacket with 0 orders")
save(fig, "05_orders_per_category_with_jacket.png")

# 6 inner vs left report rows
inner3 = one("SELECT COUNT(*) FROM shop_a_orders o JOIN shop_a_catalog p ON p.product_id=o.product_id "
             "JOIN shop_a_buyers b ON b.buyer_id=o.buyer_id")
left3 = one("SELECT COUNT(*) FROM shop_a_orders o LEFT JOIN shop_a_catalog p ON p.product_id=o.product_id "
            "LEFT JOIN shop_a_buyers b ON b.buyer_id=o.buyer_id")
assert (inner3, left3) == (113, 120)
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(["Order desk\ncount", "Three-table\nINNER JOIN", "Three-table LEFT JOIN\nfrom orders"],
              [n_orders, inner3, left3], color=[GREY, RED, GREEN])
label_bars(ax, bars, dy=1.5)
ax.set_ylabel("Rows in the Monday report")
ax.set_ylim(0, 140)
ax.set_title("Seller A SHOP-A: INNER JOIN loses 7 orders, LEFT JOIN from orders loses none")
save(fig, "06_inner_vs_left_report_rows.png")
print("charts written")
