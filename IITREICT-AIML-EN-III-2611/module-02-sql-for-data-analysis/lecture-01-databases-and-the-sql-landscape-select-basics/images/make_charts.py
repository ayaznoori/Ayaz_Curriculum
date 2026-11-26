"""Charts from campus_snack_orders.csv — same numbers as SQL (dpi 200)."""
import csv
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
DATA = BASE.parent / "data" / "campus_snack_orders.csv"
OUT = BASE

rows = []
with open(DATA, newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        rows.append(r)

blocks = Counter(r["block_code"] for r in rows)
snacks = Counter(r["snack_name"] for r in rows)
prices = [int(r["unit_price_rupees"]) for r in rows]

plt.rcParams.update({"font.size": 10})

fig, ax = plt.subplots(figsize=(9, 4.5), dpi=200)
ax.bar(blocks.keys(), blocks.values(), color=["#2563eb", "#16a34a", "#d97706"])
ax.set_title("Campus snack order rows by block code (120 rows)")
ax.set_ylabel("Order count")
ax.set_xlabel("Block code")
for i, (k, v) in enumerate(blocks.items()):
    ax.text(i, v + 1, str(v), ha="center")
plt.tight_layout()
fig.savefig(OUT / "01_orders_by_block.png")
plt.close(fig)

fig, ax = plt.subplots(figsize=(9, 4.5), dpi=200)
top = snacks.most_common(10)
labels = [t[0] for t in top]
vals = [t[1] for t in top]
ax.barh(labels[::-1], vals[::-1], color="#7c3aed")
ax.set_title("Order row count by snack name (ties possible)")
ax.set_xlabel("Rows in table")
plt.tight_layout()
fig.savefig(OUT / "02_snack_name_counts.png")
plt.close(fig)

fig, ax = plt.subplots(figsize=(9, 4.5), dpi=200)
ax.hist(prices, bins=sorted(set(prices)), color="#0d9488", edgecolor="white")
ax.set_title("Unit price in rupees across 120 snack orders")
ax.set_xlabel("unit_price_rupees")
ax.set_ylabel("Order rows")
plt.tight_layout()
fig.savefig(OUT / "03_unit_price_hist.png")
plt.close(fig)

line_totals = [int(r["qty"]) * int(r["unit_price_rupees"]) for r in rows[:30]]
fig, ax = plt.subplots(figsize=(9, 4.5), dpi=200)
ax.plot(range(1, 31), line_totals, marker="o", markersize=4, color="#dc2626")
ax.set_title("Line total (qty × unit price) for order_id 1 to 30")
ax.set_xlabel("order_id")
ax.set_ylabel("line_total (rupees)")
plt.tight_layout()
fig.savefig(OUT / "04_line_total_first30.png")
plt.close(fig)

distinct_snack_count = len(snacks)
fig, ax = plt.subplots(figsize=(6, 4.5), dpi=200)
ax.bar(
    ["Total rows", "Distinct snack names", "Distinct blocks"],
    [len(rows), distinct_snack_count, len(blocks)],
    color=["#1d4ed8", "#16a34a", "#d97706"],
)
ax.set_title("Table size vs DISTINCT snack names")
ax.set_ylabel("Count")
for i, v in enumerate([len(rows), distinct_snack_count, len(blocks)]):
    ax.text(i, v + 2, str(v), ha="center")
plt.tight_layout()
fig.savefig(OUT / "05_rows_vs_distinct.png")
plt.close(fig)

fig, ax = plt.subplots(figsize=(9, 4.5), dpi=200)
qtys = [int(r["qty"]) for r in rows]
ax.hist(qtys, bins=range(1, 10), color="#f59e0b", edgecolor="white", align="left")
ax.set_title("Quantity per order row (1 to 8)")
ax.set_xlabel("qty")
ax.set_ylabel("Order rows")
plt.tight_layout()
fig.savefig(OUT / "06_qty_distribution.png")
plt.close(fig)

print("wrote 6 charts")