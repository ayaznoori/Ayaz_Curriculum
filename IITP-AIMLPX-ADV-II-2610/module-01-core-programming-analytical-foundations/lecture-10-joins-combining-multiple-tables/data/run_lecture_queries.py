"""Run every lecture query in SQLite and print the exact table output used in lecture-script.md.

Run: python3 run_lecture_queries.py            (all queries)
     python3 run_lecture_queries.py t1_left    (one query by name)
Needs SQLite 3.39 or later for RIGHT JOIN and FULL OUTER JOIN.
"""
import sqlite3
import sys
from pathlib import Path

HERE = Path(__file__).parent

QUERIES = {
    "t1_inner_sample": """SELECT o.order_id, o.product_id, p.title, p.price_rupees
FROM seller_a_orders AS o
INNER JOIN seller_a_products AS p ON o.product_id = p.product_id
WHERE o.order_id BETWEEN 1001 AND 1005
ORDER BY o.order_id;""",
    "t1_ambiguous": """SELECT order_id, product_id, title
FROM seller_a_orders AS o
INNER JOIN seller_a_products AS p ON o.product_id = p.product_id
WHERE o.order_id = 1001;""",
    "t1_inner_counts": """SELECT COUNT(*) AS rows_returned, COUNT(p.product_id) AS with_product,
  COUNT(o.order_id) AS with_order
FROM seller_a_products AS p
INNER JOIN seller_a_orders AS o ON p.product_id = o.product_id;""",
    "t1_left_counts": """SELECT COUNT(*) AS rows_returned, COUNT(p.product_id) AS with_product,
  COUNT(o.order_id) AS with_order
FROM seller_a_products AS p
LEFT JOIN seller_a_orders AS o ON p.product_id = o.product_id;""",
    "t1_right_counts": """SELECT COUNT(*) AS rows_returned, COUNT(p.product_id) AS with_product,
  COUNT(o.order_id) AS with_order
FROM seller_a_products AS p
RIGHT JOIN seller_a_orders AS o ON p.product_id = o.product_id;""",
    "t1_full_counts": """SELECT COUNT(*) AS rows_returned, COUNT(p.product_id) AS with_product,
  COUNT(o.order_id) AS with_order
FROM seller_a_products AS p
FULL OUTER JOIN seller_a_orders AS o ON p.product_id = o.product_id;""",
    "t2_anti_products": """SELECT p.product_id, p.product_code, p.title
FROM seller_a_products AS p
LEFT JOIN seller_a_orders AS o ON p.product_id = o.product_id
WHERE o.order_id IS NULL
ORDER BY p.product_id;""",
    "t2_anti_orders": """SELECT o.order_id, o.product_id, o.quantity
FROM seller_a_orders AS o
LEFT JOIN seller_a_products AS p ON o.product_id = p.product_id
WHERE p.product_id IS NULL
ORDER BY o.order_id;""",
    "t2_equals_null": """SELECT COUNT(*) AS rows_found
FROM seller_a_products AS p
LEFT JOIN seller_a_orders AS o ON p.product_id = o.product_id
WHERE o.order_id = NULL;""",
    "t2_count_styles": """SELECT p.product_id, COUNT(*) AS joined_rows, COUNT(o.order_id) AS real_orders
FROM seller_a_products AS p
LEFT JOIN seller_a_orders AS o ON p.product_id = o.product_id
WHERE p.product_id IN (1, 2, 6)
GROUP BY p.product_id
ORDER BY p.product_id;""",
    "t2_orders_left": """SELECT COUNT(*) AS rows_returned, COUNT(p.product_id) AS with_product
FROM seller_a_orders AS o
LEFT JOIN seller_a_products AS p ON o.product_id = p.product_id;""",
    "t3_three_sample": """SELECT o.order_id, b.buyer_name, b.city, p.title
FROM seller_a_orders AS o
INNER JOIN seller_a_products AS p ON o.product_id = p.product_id
INNER JOIN seller_a_buyers AS b ON o.buyer_id = b.buyer_id
WHERE o.order_id BETWEEN 1001 AND 1005
ORDER BY o.order_id;""",
    "t3_three_inner_count": """SELECT COUNT(*) AS rows_returned
FROM seller_a_orders AS o
INNER JOIN seller_a_products AS p ON o.product_id = p.product_id
INNER JOIN seller_a_buyers AS b ON o.buyer_id = b.buyer_id;""",
    "t3_three_left_count": """SELECT COUNT(*) AS rows_returned, COUNT(b.buyer_id) AS with_buyer
FROM seller_a_orders AS o
INNER JOIN seller_a_products AS p ON o.product_id = p.product_id
LEFT JOIN seller_a_buyers AS b ON o.buyer_id = b.buyer_id;""",
    "t3_city_inner": """SELECT b.city, SUM(o.quantity * p.price_rupees) AS revenue_rs
FROM seller_a_orders AS o
INNER JOIN seller_a_products AS p ON o.product_id = p.product_id
INNER JOIN seller_a_buyers AS b ON o.buyer_id = b.buyer_id
GROUP BY b.city
ORDER BY revenue_rs DESC, b.city ASC;""",
    "t4_stock_left": """SELECT p.category, COUNT(DISTINCT p.product_id) AS products,
  COUNT(o.order_id) AS orders
FROM seller_a_products AS p
LEFT JOIN seller_a_orders AS o ON p.product_id = o.product_id
GROUP BY p.category
ORDER BY p.category;""",
    "t4_stock_inner": """SELECT p.category, COUNT(DISTINCT p.product_id) AS products,
  COUNT(o.order_id) AS orders
FROM seller_a_products AS p
INNER JOIN seller_a_orders AS o ON p.product_id = o.product_id
GROUP BY p.category
ORDER BY p.category;""",
    "t4_audit_full": """SELECT p.product_id AS catalog_id, p.title, o.order_id, o.product_id AS order_product_id
FROM seller_a_products AS p
FULL OUTER JOIN seller_a_orders AS o ON p.product_id = o.product_id
WHERE p.product_id IS NULL OR o.order_id IS NULL
ORDER BY p.product_id, o.order_id;""",
    "t4_kurta_city": """SELECT b.city, SUM(o.quantity * p.price_rupees) AS kurta_revenue_rs
FROM seller_a_orders AS o
INNER JOIN seller_a_products AS p ON o.product_id = p.product_id
INNER JOIN seller_a_buyers AS b ON o.buyer_id = b.buyer_id
WHERE p.category = 'kurta'
GROUP BY b.city
ORDER BY kurta_revenue_rs DESC, b.city ASC;""",
    "close_city_left": """SELECT b.city, SUM(o.quantity * p.price_rupees) AS revenue_rs
FROM seller_a_orders AS o
INNER JOIN seller_a_products AS p ON o.product_id = p.product_id
LEFT JOIN seller_a_buyers AS b ON o.buyer_id = b.buyer_id
GROUP BY b.city
ORDER BY revenue_rs DESC, b.city ASC;""",
}


def connect():
    con = sqlite3.connect(":memory:")
    con.executescript((HERE / "seller_a_joins.sql").read_text(encoding="utf-8"))
    return con


def cell(v):
    return "NULL" if v is None else str(v)


def table(headers, rows):
    cells = [[cell(v) for v in r] for r in rows]
    widths = [max(len(h), *(len(r[i]) for r in cells)) for i, h in enumerate(headers)]
    rule = "+" + "+".join("-" * (w + 2) for w in widths) + "+"
    def line(vals):
        return "| " + " | ".join(v.ljust(w) for v, w in zip(vals, widths)) + " |"
    return "\n".join([rule, line(headers), rule, *(line(r) for r in cells), rule])


def run(con, sql):
    try:
        cur = con.execute(sql)
    except sqlite3.Error as e:
        return f"Error: {e}"
    return table([d[0] for d in cur.description], cur.fetchall())


if __name__ == "__main__":
    con = connect()
    names = sys.argv[1:] or list(QUERIES)
    for n in names:
        print(f"-- {n}")
        print(run(con, QUERIES[n]))
        print()
