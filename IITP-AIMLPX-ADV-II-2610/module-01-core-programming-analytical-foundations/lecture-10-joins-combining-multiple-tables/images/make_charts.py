"""Draw the lecture charts from the same SQLite queries used in lecture-script.md.

Run (needs matplotlib): python3 make_charts.py
"""
import sqlite3
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE = Path(__file__).parent
DATA = HERE.parent / "data"
sys.path.insert(0, str(DATA))
from run_lecture_queries import QUERIES, connect  # noqa: E402

BLUE, GREEN, AMBER, RED, PURPLE, GREY = "#2563eb", "#16a34a", "#d97706", "#dc2626", "#7c3aed", "#94a3b8"
DPI = 200
con = connect()


def rows(name):
    return con.execute(QUERIES[name]).fetchall()


def save(fig, name):
    fig.tight_layout()
    fig.savefig(HERE / name, dpi=DPI)
    plt.close(fig)
    print("saved", name)


def chart_row_counts(name):
    kinds = ["INNER", "LEFT", "RIGHT", "FULL OUTER"]
    res = [rows(q)[0] for q in ("t1_inner_counts", "t1_left_counts", "t1_right_counts", "t1_full_counts")]
    pairs = rows("t1_inner_counts")[0][0]
    only_p = [r[0] - r[2] if k in ("LEFT", "FULL OUTER") else 0 for r, k in zip(res, kinds)]
    only_o = [r[0] - r[1] if k in ("RIGHT", "FULL OUTER") else 0 for r, k in zip(res, kinds)]
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(kinds, [pairs] * 4, color=BLUE, label=f"matched pairs ({pairs})")
    ax.bar(kinds, only_p, bottom=[pairs] * 4, color=GREEN, label="products with no order")
    ax.bar(kinds, only_o, bottom=[pairs + a for a in only_p], color=AMBER, label="orders with no product")
    for i, r in enumerate(res):
        ax.text(i, r[0] + 1.2, str(r[0]), ha="center", fontweight="bold")
    ax.set_ylim(100, 132)
    ax.set_ylabel("rows returned (axis starts at 100)")
    ax.set_title("Rows returned by each join type (products joined to orders)")
    ax.legend(loc="upper left", fontsize=9)
    save(fig, name)


def chart_orders_per_product(name):
    data = con.execute(
        "SELECT p.product_id, COUNT(o.order_id) FROM seller_a_products p "
        "LEFT JOIN seller_a_orders o ON p.product_id = o.product_id GROUP BY p.product_id ORDER BY p.product_id"
    ).fetchall()
    ids = [d[0] for d in data]
    cnt = [d[1] for d in data]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar([str(i) for i in ids], cnt, color=[RED if c == 0 else BLUE for c in cnt])
    for i, c in enumerate(cnt):
        if c == 0:
            ax.text(i, 0.4, "0", ha="center", color=RED, fontweight="bold")
    ax.set_xlabel("product_id")
    ax.set_ylabel("orders")
    ax.set_title(f"Orders per product: {sum(1 for c in cnt if c == 0)} red products have no order")
    save(fig, name)


def chart_count_styles(name):
    data = rows("t2_count_styles")
    labels = [f"product {d[0]}" for d in data]
    fig, ax = plt.subplots(figsize=(8, 5))
    x = range(len(data))
    w = 0.38
    b1 = ax.bar([i - w / 2 for i in x], [d[1] for d in data], w, color=AMBER, label="COUNT(*)")
    b2 = ax.bar([i + w / 2 for i in x], [d[2] for d in data], w, color=BLUE, label="COUNT(o.order_id)")
    for bars in (b1, b2):
        for b in bars:
            ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.3, str(int(b.get_height())), ha="center", fontweight="bold")
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels)
    ax.set_ylabel("count")
    ax.set_ylim(0, 20)
    ax.set_title("After LEFT JOIN: row count vs real orders")
    ax.legend()
    save(fig, name)


def chart_join_steps(name):
    n_orders = con.execute("SELECT COUNT(*) FROM seller_a_orders").fetchone()[0]
    inner_p = rows("t1_inner_counts")[0][0]
    inner3 = rows("t3_three_inner_count")[0][0]
    left3 = rows("t3_three_left_count")[0][0]
    labels = ["orders\nalone", "+ products\n(INNER)", "+ buyers\n(INNER)", "+ buyers\n(LEFT)"]
    vals = [n_orders, inner_p, inner3, left3]
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(labels, vals, color=[GREY, BLUE, RED, GREEN])
    for i, v in enumerate(vals):
        ax.text(i, v + 1.5, str(v), ha="center", fontweight="bold")
    ax.set_ylim(0, 140)
    ax.set_ylabel("rows")
    ax.set_title("Order rows left after each join in the three-table query")
    save(fig, name)


def chart_schema(name):
    fig, ax = plt.subplots(figsize=(10, 5.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    def box(x, y, w, h, title, cols, color):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04", fc="#f8fafc", ec=color, lw=2.5))
        ax.add_patch(FancyBboxPatch((x, y + h - 0.6), w, 0.6, boxstyle="round,pad=0.04", fc=color, ec=color))
        ax.text(x + w / 2, y + h - 0.3, title, ha="center", va="center", color="white", fontweight="bold", fontsize=11)
        for i, c in enumerate(cols):
            ax.text(x + 0.2, y + h - 1.0 - 0.45 * i, c, va="center", fontsize=10, family="monospace")

    box(0.2, 0.9, 3.0, 4.6, "seller_a_products", ["product_id  (key)", "product_code", "title", "category", "price_rupees"], GREEN)
    box(3.8, 0.9, 2.9, 4.6, "seller_a_orders", ["order_id  (key)", "buyer_id", "product_id", "quantity", "order_date"], BLUE)
    box(7.2, 0.9, 2.6, 4.6, "seller_a_buyers", ["buyer_id  (key)", "buyer_name", "city"], AMBER)
    ax.annotate("", xy=(3.15, 2.85), xytext=(3.85, 2.85), arrowprops=dict(arrowstyle="<->", lw=2.5, color=PURPLE))
    ax.text(3.5, 3.1, "product_id", ha="center", fontsize=9, color=PURPLE, fontweight="bold")
    ax.annotate("", xy=(7.25, 3.3), xytext=(6.65, 3.3), arrowprops=dict(arrowstyle="<->", lw=2.5, color=PURPLE))
    ax.text(6.95, 3.55, "buyer_id", ha="center", fontsize=9, color=PURPLE, fontweight="bold")
    ax.text(5.0, 0.35, "One product row, many order rows.  One buyer row, many order rows.", ha="center", fontsize=10)
    ax.set_title("Seller A schema: three tables and two join keys", fontsize=13)
    save(fig, name)


def chart_city_revenue(name):
    inner = dict(rows("t3_city_inner"))
    left = dict(rows("close_city_left"))
    order = sorted(left, key=lambda c: (-left[c], str(c)))
    labels = [c if c is not None else "no city\n(guest)" for c in order]
    fig, ax = plt.subplots(figsize=(10, 5.4))
    x = range(len(order))
    w = 0.38
    ax.bar([i - w / 2 for i in x], [inner.get(c, 0) for c in order], w, color=RED, label=f"INNER buyers (total {sum(inner.values()):,})")
    ax.bar([i + w / 2 for i in x], [left[c] for c in order], w, color=GREEN, label=f"LEFT buyers (total {sum(left.values()):,})")
    ax.text(order.index(None) - w / 2, 900, "missing", ha="center", color=RED, fontsize=9, fontweight="bold")
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("revenue (rupees)")
    ax.set_title("Revenue by city: the INNER report loses the guest orders")
    ax.legend()
    save(fig, name)


if __name__ == "__main__":
    chart_row_counts("01_row_counts_by_join_type.png")
    chart_orders_per_product("02_orders_per_product.png")
    chart_count_styles("03_count_star_vs_real_orders.png")
    chart_join_steps("04_rows_after_each_join.png")
    chart_schema("05_seller_a_schema.png")
    chart_city_revenue("06_city_revenue_inner_vs_left.png")
