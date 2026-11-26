#!/usr/bin/env python3
"""Draw the six lecture charts from the same queries the lecture runs (SQLite, data/*.sql)."""
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "data"))
from run_lecture_queries import connect  # noqa: E402

con = connect()
W = "shop_code = 'SHOP-A' AND listed_date BETWEEN '2025-03-01' AND '2025-03-31'"
BLUE, GREEN, AMBER, PURPLE, RED, GREY = "#2563eb", "#16a34a", "#d97706", "#7c3aed", "#dc2626", "#94a3b8"


def q(sql):
    return con.execute(sql).fetchall()


def save(fig, name):
    fig.tight_layout()
    fig.savefig(HERE / name, dpi=200)
    plt.close(fig)


# 01 funnel: rows and groups left after each stage
rows_in = q("SELECT COUNT(*) FROM shop_a_products")[0][0]
rows_where, groups = q(f"SELECT COUNT(*), COUNT(DISTINCT category) FROM shop_a_products WHERE {W}")[0]
after_having = len(q(f"SELECT category FROM shop_a_products WHERE {W} GROUP BY category HAVING SUM(price_rupees) >= 1000"))
after_limit = len(q(f"SELECT category FROM shop_a_products WHERE {W} GROUP BY category HAVING SUM(price_rupees) >= 1000 ORDER BY SUM(price_rupees) DESC LIMIT 3"))
labels = ["1st FROM\n(rows)", "2nd WHERE\n(rows)", "3rd GROUP BY\n(groups)", "4th HAVING\n(groups)", "7th LIMIT, after\nSELECT and ORDER BY (rows)"]
vals = [rows_in, rows_where, groups, after_having, after_limit]
fig, ax = plt.subplots(figsize=(9, 4.6))
bars = ax.barh(labels[::-1], vals[::-1], color=[GREEN, AMBER, PURPLE, BLUE, RED][::-1])
for b, v in zip(bars, vals[::-1]):
    ax.text(v + 1.5, b.get_y() + b.get_height() / 2, str(v), va="center", fontsize=12, fontweight="bold")
ax.set_xlim(0, max(vals) * 1.12)
ax.set_xlabel("Rows or groups left after the stage")
ax.set_title("What is left after each running stage")
save(fig, "01_running_order_funnel.png")

# 02 March totals per category with the 1000 cutoff
cat = q(f"SELECT category, SUM(price_rupees) FROM shop_a_products WHERE {W} GROUP BY category ORDER BY SUM(price_rupees) DESC, category")
fig, ax = plt.subplots(figsize=(9, 4.8))
colors = [BLUE if v >= 1000 else GREY for _, v in cat]
bars = ax.bar([c for c, _ in cat], [v for _, v in cat], color=colors)
for b, (_, v) in zip(bars, cat):
    ax.text(b.get_x() + b.get_width() / 2, v + 140, f"{v:,}", ha="center", fontsize=11)
ax.axhline(1000, color=RED, linestyle="--")
ax.text(len(cat) - 0.5, 1100, "cutoff 1000", color=RED, ha="right", fontsize=11)
ax.set_ylabel("Total price (rupees)")
ax.set_ylim(0, max(v for _, v in cat) * 1.15)
ax.set_title("SHOP-A, March 2025: total price per category")
save(fig, "02_march_category_totals.png")

# 03 all months vs March only
allm = dict(q("SELECT category, SUM(price_rupees) FROM shop_a_products WHERE shop_code = 'SHOP-A' GROUP BY category"))
mar = dict(q(f"SELECT category, SUM(price_rupees) FROM shop_a_products WHERE {W} GROUP BY category"))
order = [c for c, _ in sorted(allm.items(), key=lambda kv: (-kv[1], kv[0]))]
fig, ax = plt.subplots(figsize=(9, 4.8))
x = range(len(order))
ax.bar([i - 0.2 for i in x], [allm[c] for c in order], 0.4, color=RED, label="Draft: all months")
ax.bar([i + 0.2 for i in x], [mar[c] for c in order], 0.4, color=GREEN, label="Question: March only")
for i, c in enumerate(order):
    ax.text(i - 0.2, allm[c] + 100, f"{allm[c]:,}", ha="center", fontsize=9)
    ax.text(i + 0.2, mar[c] + 100, f"{mar[c]:,}", ha="center", fontsize=9)
ax.set_xticks(list(x))
ax.set_xticklabels(order)
ax.set_ylabel("Total price (rupees)")
ax.set_ylim(0, max(allm.values()) * 1.15)
ax.legend()
ax.set_title("SHOP-A totals: draft without a March filter vs the question")
save(fig, "03_draft_vs_march_totals.png")

# 04 COUNT(*) vs COUNT(price_rupees)
cnt = q(f"SELECT category, COUNT(*), COUNT(price_rupees) FROM shop_a_products WHERE {W} GROUP BY category ORDER BY SUM(price_rupees) DESC, category")
fig, ax = plt.subplots(figsize=(9, 4.8))
x = range(len(cnt))
ax.bar([i - 0.2 for i in x], [r[1] for r in cnt], 0.4, color=GREEN, label="COUNT(*)")
ax.bar([i + 0.2 for i in x], [r[2] for r in cnt], 0.4, color=AMBER, label="COUNT(price_rupees)")
for i, r in enumerate(cnt):
    ax.text(i - 0.2, r[1] + 0.15, str(r[1]), ha="center", fontsize=10)
    ax.text(i + 0.2, r[2] + 0.15, str(r[2]), ha="center", fontsize=10)
ax.set_xticks(list(x))
ax.set_xticklabels([r[0] for r in cnt])
ax.set_ylabel("Products counted")
ax.set_ylim(0, max(r[1] for r in cnt) * 1.2)
ax.legend()
ax.set_title("SHOP-A, March 2025: the two counts differ only for bag")
save(fig, "04_bag_count_check.png")

# 05 four lowest stall-days with at least 5 slips
low = q("SELECT stall_name, coupon_day, SUM(amount_rs) FROM fest_coupons WHERE stall_name IS NOT NULL AND coupon_day <> 'Sun' GROUP BY stall_name, coupon_day HAVING COUNT(*) >= 5 ORDER BY SUM(amount_rs) ASC, stall_name LIMIT 4")
fig, ax = plt.subplots(figsize=(9, 4.4))
names = [f"{s} {d}" for s, d, _ in low]
bars = ax.barh(names[::-1], [v for *_, v in low][::-1], color=PURPLE)
for b, (*_, v) in zip(bars, low[::-1]):
    ax.text(v + 8, b.get_y() + b.get_height() / 2, str(v), va="center", fontsize=12, fontweight="bold")
ax.set_xlim(0, max(v for *_, v in low) * 1.15)
ax.set_xlabel("Day total (rupees)")
ax.set_title("Four lowest stall-day totals with at least 5 slips (Fri and Sat)")
save(fig, "05_weakest_stall_days.png")

# 06 closing: slide vs checked
rows_draft = q("SELECT COUNT(*) FROM shop_a_products WHERE shop_code = 'SHOP-A'")[0][0]
kurta_all = allm["kurta"]
kurta_mar = mar["kurta"]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(9, 4.6))
for ax, vals, title, fmt in ((a1, (rows_draft, rows_where), "Rows behind the totals", "{}"), (a2, (kurta_all, kurta_mar), "Kurta total (rupees)", "{:,}")):
    bars = ax.bar(["Unchecked\nslide", "Checked\nquery"], vals, color=[RED, GREEN])
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + max(vals) * 0.02, fmt.format(v), ha="center", fontsize=12, fontweight="bold")
    ax.set_ylim(0, max(vals) * 1.15)
    ax.set_title(title)
save(fig, "06_closing_slide_vs_checked.png")
print("charts saved")
