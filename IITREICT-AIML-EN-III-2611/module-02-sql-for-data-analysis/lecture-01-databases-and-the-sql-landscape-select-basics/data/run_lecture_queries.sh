#!/bin/bash
DB="/tmp/campus_snack_orders_261204.db"
SQL="/Users/masai/Documents/AIML courses./IITREICT-AIML-EN-III-2611/module-02-sql-for-data-analysis/lecture-01-databases-and-the-sql-landscape-select-basics/data/campus_snack_orders.sql"
rm -f "$DB"
sqlite3 "$DB" < "$SQL"

run() {
  echo "===== $1 ====="
  sqlite3 -header -column "$DB" "$2"
  echo
}

run "count" "SELECT COUNT(*) AS row_count FROM campus_snack_orders;"
run "pragma" "PRAGMA table_info(campus_snack_orders);"
run "select_two_cols" "SELECT snack_name, qty FROM campus_snack_orders ORDER BY order_id LIMIT 6;"
run "select_four_cols" "SELECT order_id, snack_name, block_code, unit_price_rupees FROM campus_snack_orders ORDER BY order_id LIMIT 6;"
run "distinct_snacks" "SELECT DISTINCT snack_name FROM campus_snack_orders ORDER BY snack_name, order_id;"
run "distinct_blocks" "SELECT DISTINCT block_code FROM campus_snack_orders ORDER BY block_code;"
run "expression_line_total" "SELECT order_id, snack_name, qty, unit_price_rupees, qty * unit_price_rupees AS line_total FROM campus_snack_orders ORDER BY order_id LIMIT 6;"
run "expression_gst" "SELECT order_id, unit_price_rupees, unit_price_rupees + 5 AS price_with_packing FROM campus_snack_orders ORDER BY order_id LIMIT 5;"
run "read_orders_first10" "SELECT order_id, snack_name, qty, unit_price_rupees, block_code, order_date FROM campus_snack_orders ORDER BY order_id LIMIT 10;"
run "closing_read" "SELECT order_id, snack_name, qty, unit_price_rupees, qty * unit_price_rupees AS line_total FROM campus_snack_orders ORDER BY order_id LIMIT 8;"