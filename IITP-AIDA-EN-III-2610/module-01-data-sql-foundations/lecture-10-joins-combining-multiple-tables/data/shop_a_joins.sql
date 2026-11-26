-- Seller A join practice tables, invented for teaching (SQLite or MySQL 8.0).
DROP TABLE IF EXISTS shop_a_categories;
CREATE TABLE shop_a_categories (
  category_id INT PRIMARY KEY,
  category_name VARCHAR(20) NOT NULL
);
INSERT INTO shop_a_categories VALUES (1, 'Kurta');
INSERT INTO shop_a_categories VALUES (2, 'Tee');
INSERT INTO shop_a_categories VALUES (3, 'Dupatta');
INSERT INTO shop_a_categories VALUES (4, 'Saree');
INSERT INTO shop_a_categories VALUES (5, 'Jeans');
INSERT INTO shop_a_categories VALUES (6, 'Shoes');
INSERT INTO shop_a_categories VALUES (7, 'Bag');
INSERT INTO shop_a_categories VALUES (8, 'Jacket');

DROP TABLE IF EXISTS shop_a_catalog;
CREATE TABLE shop_a_catalog (
  product_id INT PRIMARY KEY,
  title VARCHAR(40) NOT NULL,
  category_id INT NOT NULL,
  price_rupees INT NOT NULL
);
INSERT INTO shop_a_catalog VALUES (1, 'Cotton Kurta Red', 1, 499);
INSERT INTO shop_a_catalog VALUES (2, 'Linen Kurta Blue', 1, 650);
INSERT INTO shop_a_catalog VALUES (3, 'Festival Kurta Green', 1, 799);
INSERT INTO shop_a_catalog VALUES (4, 'Printed Kurti Yellow', 1, 549);
INSERT INTO shop_a_catalog VALUES (5, 'Straight Kurta Black', 1, 599);
INSERT INTO shop_a_catalog VALUES (6, 'Round Neck Tee White', 2, 299);
INSERT INTO shop_a_catalog VALUES (7, 'Graphic Tee Black', 2, 349);
INSERT INTO shop_a_catalog VALUES (8, 'Polo T-Shirt Green', 2, 449);
INSERT INTO shop_a_catalog VALUES (9, 'Silk Dupatta Gold', 3, 450);
INSERT INTO shop_a_catalog VALUES (10, 'Cotton Dupatta Pink', 3, 275);
INSERT INTO shop_a_catalog VALUES (11, 'Zari Silk Saree Maroon', 4, 1899);
INSERT INTO shop_a_catalog VALUES (12, 'Cotton Saree Blue', 4, 999);
INSERT INTO shop_a_catalog VALUES (13, 'Slim Fit Jeans Blue', 5, 899);
INSERT INTO shop_a_catalog VALUES (14, 'Straight Jeans Black', 5, 949);
INSERT INTO shop_a_catalog VALUES (15, 'Casual Sneakers Black', 6, 799);
INSERT INTO shop_a_catalog VALUES (16, 'Running Shoes White', 6, 1199);
INSERT INTO shop_a_catalog VALUES (17, 'Canvas Backpack Navy', 7, 1299);
INSERT INTO shop_a_catalog VALUES (18, 'Laptop Sling Bag Grey', 7, 1099);
INSERT INTO shop_a_catalog VALUES (19, 'Linen Kurta Beige', 1, 699);
INSERT INTO shop_a_catalog VALUES (20, 'Festival Kurta Orange', 1, 849);
INSERT INTO shop_a_catalog VALUES (21, 'Striped Tee Navy', 2, 379);
INSERT INTO shop_a_catalog VALUES (22, 'Printed Dupatta Red', 3, 325);
INSERT INTO shop_a_catalog VALUES (23, 'Silk Saree Green', 4, 2499);
INSERT INTO shop_a_catalog VALUES (24, 'Denim Jeans Grey', 5, 999);
INSERT INTO shop_a_catalog VALUES (25, 'Trail Sneakers Blue', 6, 1399);
INSERT INTO shop_a_catalog VALUES (26, 'Mini Backpack Pink', 7, 899);
INSERT INTO shop_a_catalog VALUES (27, 'Cotton Kurta White', 1, 479);
INSERT INTO shop_a_catalog VALUES (28, 'Oversized Tee Cream', 2, 399);
INSERT INTO shop_a_catalog VALUES (29, 'Block Print Dupatta Blue', 3, 375);
INSERT INTO shop_a_catalog VALUES (30, 'Tote Bag Beige', 7, 599);

DROP TABLE IF EXISTS shop_a_buyers;
CREATE TABLE shop_a_buyers (
  buyer_id INT PRIMARY KEY,
  buyer_name VARCHAR(40) NOT NULL,
  city_code CHAR(3) NOT NULL
);
INSERT INTO shop_a_buyers VALUES (1, 'Lakshmi Menon', 'MUM');
INSERT INTO shop_a_buyers VALUES (2, 'Lakshmi Khan', 'DEL');
INSERT INTO shop_a_buyers VALUES (3, 'Sneha Reddy', 'BLR');
INSERT INTO shop_a_buyers VALUES (4, 'Suresh Shah', 'BLR');
INSERT INTO shop_a_buyers VALUES (5, 'Nikhil Patel', 'HYD');
INSERT INTO shop_a_buyers VALUES (6, 'Rohan Shah', 'PNQ');
INSERT INTO shop_a_buyers VALUES (7, 'Harsh Shah', 'PNQ');
INSERT INTO shop_a_buyers VALUES (8, 'Priya Das', 'PNQ');
INSERT INTO shop_a_buyers VALUES (9, 'Lakshmi Das', 'PNQ');
INSERT INTO shop_a_buyers VALUES (10, 'Nikhil Singh', 'BLR');
INSERT INTO shop_a_buyers VALUES (11, 'Arjun Khan', 'MUM');
INSERT INTO shop_a_buyers VALUES (12, 'Kavya Singh', 'MUM');
INSERT INTO shop_a_buyers VALUES (13, 'Divya Rao', 'DEL');
INSERT INTO shop_a_buyers VALUES (14, 'Arjun Patel', 'BLR');
INSERT INTO shop_a_buyers VALUES (15, 'Sneha Joshi', 'MUM');
INSERT INTO shop_a_buyers VALUES (16, 'Pooja Shah', 'BLR');
INSERT INTO shop_a_buyers VALUES (17, 'Ananya Shah', 'DEL');
INSERT INTO shop_a_buyers VALUES (18, 'Sneha Nair', 'BLR');
INSERT INTO shop_a_buyers VALUES (19, 'Pooja Singh', 'DEL');
INSERT INTO shop_a_buyers VALUES (20, 'Meera Joshi', 'BLR');
INSERT INTO shop_a_buyers VALUES (21, 'Arjun Singh', 'MUM');
INSERT INTO shop_a_buyers VALUES (22, 'Ananya Menon', 'MUM');
INSERT INTO shop_a_buyers VALUES (23, 'Ananya Gupta', 'MUM');
INSERT INTO shop_a_buyers VALUES (24, 'Priya Nair', 'DEL');
INSERT INTO shop_a_buyers VALUES (25, 'Ananya Singh', 'HYD');
INSERT INTO shop_a_buyers VALUES (26, 'Kavya Menon', 'BLR');
INSERT INTO shop_a_buyers VALUES (27, 'Pooja Das', 'BLR');
INSERT INTO shop_a_buyers VALUES (28, 'Ananya Iyer', 'BLR');
INSERT INTO shop_a_buyers VALUES (29, 'Imran Patel', 'DEL');
INSERT INTO shop_a_buyers VALUES (30, 'Farah Shah', 'BLR');
INSERT INTO shop_a_buyers VALUES (31, 'Sneha Patel', 'PNQ');
INSERT INTO shop_a_buyers VALUES (32, 'Sneha Iyer', 'MUM');
INSERT INTO shop_a_buyers VALUES (33, 'Meera Iyer', 'PNQ');
INSERT INTO shop_a_buyers VALUES (34, 'Arjun Menon', 'DEL');
INSERT INTO shop_a_buyers VALUES (35, 'Suresh Iyer', 'DEL');
INSERT INTO shop_a_buyers VALUES (36, 'Ananya Patel', 'MUM');

DROP TABLE IF EXISTS shop_a_orders;
CREATE TABLE shop_a_orders (
  order_id INT PRIMARY KEY,
  shop_code VARCHAR(10) NOT NULL,
  product_id INT NOT NULL,
  buyer_id INT NULL,
  qty INT NOT NULL,
  order_date DATE NOT NULL
);
INSERT INTO shop_a_orders VALUES (1, 'SHOP-A', 3, 26, 1, '2026-02-02');
INSERT INTO shop_a_orders VALUES (2, 'SHOP-A', 16, 30, 1, '2026-02-01');
INSERT INTO shop_a_orders VALUES (3, 'SHOP-A', 20, 14, 3, '2026-02-03');
INSERT INTO shop_a_orders VALUES (4, 'SHOP-A', 27, 1, 1, '2026-02-02');
INSERT INTO shop_a_orders VALUES (5, 'SHOP-A', 9, 28, 2, '2026-02-03');
INSERT INTO shop_a_orders VALUES (6, 'SHOP-A', 9, 12, 2, '2026-02-03');
INSERT INTO shop_a_orders VALUES (7, 'SHOP-A', 5, 12, 1, '2026-02-04');
INSERT INTO shop_a_orders VALUES (8, 'SHOP-A', 19, 27, 2, '2026-02-03');
INSERT INTO shop_a_orders VALUES (9, 'SHOP-A', 21, 18, 2, '2026-02-04');
INSERT INTO shop_a_orders VALUES (10, 'SHOP-A', 6, 27, 1, '2026-02-05');
INSERT INTO shop_a_orders VALUES (11, 'SHOP-A', 13, 8, 3, '2026-02-05');
INSERT INTO shop_a_orders VALUES (12, 'SHOP-A', 13, NULL, 1, '2026-02-06');
INSERT INTO shop_a_orders VALUES (13, 'SHOP-A', 4, 27, 2, '2026-02-06');
INSERT INTO shop_a_orders VALUES (14, 'SHOP-A', 13, 12, 1, '2026-02-05');
INSERT INTO shop_a_orders VALUES (15, 'SHOP-A', 1, 15, 1, '2026-02-07');
INSERT INTO shop_a_orders VALUES (16, 'SHOP-A', 22, 25, 1, '2026-02-07');
INSERT INTO shop_a_orders VALUES (17, 'SHOP-A', 1, 1, 3, '2026-02-07');
INSERT INTO shop_a_orders VALUES (18, 'SHOP-A', 1, 36, 1, '2026-02-08');
INSERT INTO shop_a_orders VALUES (19, 'SHOP-A', 13, 36, 1, '2026-02-07');
INSERT INTO shop_a_orders VALUES (20, 'SHOP-A', 6, 5, 1, '2026-02-07');
INSERT INTO shop_a_orders VALUES (21, 'SHOP-A', 1, 14, 3, '2026-02-08');
INSERT INTO shop_a_orders VALUES (22, 'SHOP-A', 15, 16, 1, '2026-02-08');
INSERT INTO shop_a_orders VALUES (23, 'SHOP-A', 41, 14, 2, '2026-02-09');
INSERT INTO shop_a_orders VALUES (24, 'SHOP-A', 14, 18, 1, '2026-02-10');
INSERT INTO shop_a_orders VALUES (25, 'SHOP-A', 24, 10, 2, '2026-02-10');
INSERT INTO shop_a_orders VALUES (26, 'SHOP-A', 2, 6, 3, '2026-02-09');
INSERT INTO shop_a_orders VALUES (27, 'SHOP-A', 11, 18, 2, '2026-02-11');
INSERT INTO shop_a_orders VALUES (28, 'SHOP-A', 13, 4, 2, '2026-02-10');
INSERT INTO shop_a_orders VALUES (29, 'SHOP-A', 3, 33, 2, '2026-02-11');
INSERT INTO shop_a_orders VALUES (30, 'SHOP-A', 1, 33, 3, '2026-02-11');
INSERT INTO shop_a_orders VALUES (31, 'SHOP-A', 13, 21, 1, '2026-02-11');
INSERT INTO shop_a_orders VALUES (32, 'SHOP-A', 13, 32, 1, '2026-02-12');
INSERT INTO shop_a_orders VALUES (33, 'SHOP-A', 3, 28, 2, '2026-02-13');
INSERT INTO shop_a_orders VALUES (34, 'SHOP-A', 9, 3, 1, '2026-02-13');
INSERT INTO shop_a_orders VALUES (35, 'SHOP-A', 6, 30, 1, '2026-02-13');
INSERT INTO shop_a_orders VALUES (36, 'SHOP-A', 15, 27, 1, '2026-02-14');
INSERT INTO shop_a_orders VALUES (37, 'SHOP-A', 1, 25, 1, '2026-02-13');
INSERT INTO shop_a_orders VALUES (38, 'SHOP-A', 29, 26, 2, '2026-02-13');
INSERT INTO shop_a_orders VALUES (39, 'SHOP-A', 1, 19, 3, '2026-02-14');
INSERT INTO shop_a_orders VALUES (40, 'SHOP-A', 3, 29, 1, '2026-02-14');
INSERT INTO shop_a_orders VALUES (41, 'SHOP-A', 15, 19, 1, '2026-02-14');
INSERT INTO shop_a_orders VALUES (42, 'SHOP-A', 2, 3, 1, '2026-02-16');
INSERT INTO shop_a_orders VALUES (43, 'SHOP-A', 17, 18, 1, '2026-02-15');
INSERT INTO shop_a_orders VALUES (44, 'SHOP-A', 10, NULL, 1, '2026-02-16');
INSERT INTO shop_a_orders VALUES (45, 'SHOP-A', 15, 10, 2, '2026-02-17');
INSERT INTO shop_a_orders VALUES (46, 'SHOP-A', 15, 10, 1, '2026-02-17');
INSERT INTO shop_a_orders VALUES (47, 'SHOP-A', 1, 11, 1, '2026-02-16');
INSERT INTO shop_a_orders VALUES (48, 'SHOP-A', 15, 7, 2, '2026-02-18');
INSERT INTO shop_a_orders VALUES (49, 'SHOP-A', 1, 14, 1, '2026-02-18');
INSERT INTO shop_a_orders VALUES (50, 'SHOP-A', 2, 36, 1, '2026-02-18');
INSERT INTO shop_a_orders VALUES (51, 'SHOP-A', 9, 13, 1, '2026-02-19');
INSERT INTO shop_a_orders VALUES (52, 'SHOP-A', 1, 21, 1, '2026-02-19');
INSERT INTO shop_a_orders VALUES (53, 'SHOP-A', 13, 20, 2, '2026-02-18');
INSERT INTO shop_a_orders VALUES (54, 'SHOP-A', 17, 20, 1, '2026-02-20');
INSERT INTO shop_a_orders VALUES (55, 'SHOP-A', 2, 23, 2, '2026-02-19');
INSERT INTO shop_a_orders VALUES (56, 'SHOP-A', 11, 6, 2, '2026-02-20');
INSERT INTO shop_a_orders VALUES (57, 'SHOP-A', 17, 36, 2, '2026-02-20');
INSERT INTO shop_a_orders VALUES (58, 'SHOP-A', 41, 36, 1, '2026-02-21');
INSERT INTO shop_a_orders VALUES (59, 'SHOP-A', 17, 12, 1, '2026-02-21');
INSERT INTO shop_a_orders VALUES (60, 'SHOP-A', 20, 3, 2, '2026-02-21');
INSERT INTO shop_a_orders VALUES (61, 'SHOP-A', 14, 4, 1, '2026-02-21');
INSERT INTO shop_a_orders VALUES (62, 'SHOP-A', 11, 34, 1, '2026-02-22');
INSERT INTO shop_a_orders VALUES (63, 'SHOP-A', 17, 4, 1, '2026-02-22');
INSERT INTO shop_a_orders VALUES (64, 'SHOP-A', 15, 12, 2, '2026-02-22');
INSERT INTO shop_a_orders VALUES (65, 'SHOP-A', 2, 7, 1, '2026-02-23');
INSERT INTO shop_a_orders VALUES (66, 'SHOP-A', 13, 11, 1, '2026-02-24');
INSERT INTO shop_a_orders VALUES (67, 'SHOP-A', 15, 29, 1, '2026-02-23');
INSERT INTO shop_a_orders VALUES (68, 'SHOP-A', 15, 32, 1, '2026-02-23');
INSERT INTO shop_a_orders VALUES (69, 'SHOP-A', 1, 29, 1, '2026-02-24');
INSERT INTO shop_a_orders VALUES (70, 'SHOP-A', 25, 4, 1, '2026-02-24');
INSERT INTO shop_a_orders VALUES (71, 'SHOP-A', 8, NULL, 1, '2026-02-24');
INSERT INTO shop_a_orders VALUES (72, 'SHOP-A', 24, 10, 2, '2026-02-25');
INSERT INTO shop_a_orders VALUES (73, 'SHOP-A', 1, 13, 1, '2026-02-26');
INSERT INTO shop_a_orders VALUES (74, 'SHOP-A', 8, 4, 1, '2026-02-25');
INSERT INTO shop_a_orders VALUES (75, 'SHOP-A', 6, 8, 2, '2026-02-27');
INSERT INTO shop_a_orders VALUES (76, 'SHOP-A', 14, 13, 1, '2026-02-26');
INSERT INTO shop_a_orders VALUES (77, 'SHOP-A', 3, 3, 1, '2026-02-26');
INSERT INTO shop_a_orders VALUES (78, 'SHOP-A', 15, 20, 1, '2026-02-28');
INSERT INTO shop_a_orders VALUES (79, 'SHOP-A', 17, 5, 3, '2026-02-27');
INSERT INTO shop_a_orders VALUES (80, 'SHOP-A', 13, 10, 1, '2026-02-28');
INSERT INTO shop_a_orders VALUES (81, 'SHOP-A', 1, 16, 3, '2026-02-28');
INSERT INTO shop_a_orders VALUES (82, 'SHOP-A', 9, 33, 3, '2026-03-01');
INSERT INTO shop_a_orders VALUES (83, 'SHOP-A', 1, 7, 2, '2026-03-01');
INSERT INTO shop_a_orders VALUES (84, 'SHOP-A', 1, 26, 2, '2026-03-02');
INSERT INTO shop_a_orders VALUES (85, 'SHOP-A', 13, 10, 2, '2026-03-02');
INSERT INTO shop_a_orders VALUES (86, 'SHOP-A', 1, 36, 1, '2026-03-01');
INSERT INTO shop_a_orders VALUES (87, 'SHOP-A', 6, 16, 1, '2026-03-02');
INSERT INTO shop_a_orders VALUES (88, 'SHOP-A', 1, 21, 3, '2026-03-03');
INSERT INTO shop_a_orders VALUES (89, 'SHOP-A', 3, 18, 1, '2026-03-02');
INSERT INTO shop_a_orders VALUES (90, 'SHOP-A', 3, 22, 1, '2026-03-04');
INSERT INTO shop_a_orders VALUES (91, 'SHOP-A', 15, 25, 1, '2026-03-03');
INSERT INTO shop_a_orders VALUES (92, 'SHOP-A', 7, 25, 3, '2026-03-03');
INSERT INTO shop_a_orders VALUES (93, 'SHOP-A', 13, 28, 1, '2026-03-04');
INSERT INTO shop_a_orders VALUES (94, 'SHOP-A', 6, 29, 1, '2026-03-05');
INSERT INTO shop_a_orders VALUES (95, 'SHOP-A', 1, 14, 1, '2026-03-04');
INSERT INTO shop_a_orders VALUES (96, 'SHOP-A', 10, 13, 2, '2026-03-06');
INSERT INTO shop_a_orders VALUES (97, 'SHOP-A', 42, 1, 1, '2026-03-05');
INSERT INTO shop_a_orders VALUES (98, 'SHOP-A', 15, 26, 1, '2026-03-06');
INSERT INTO shop_a_orders VALUES (99, 'SHOP-A', 2, 32, 2, '2026-03-07');
INSERT INTO shop_a_orders VALUES (100, 'SHOP-A', 9, 4, 1, '2026-03-07');
INSERT INTO shop_a_orders VALUES (101, 'SHOP-A', 3, 18, 1, '2026-03-06');
INSERT INTO shop_a_orders VALUES (102, 'SHOP-A', 15, 20, 1, '2026-03-08');
INSERT INTO shop_a_orders VALUES (103, 'SHOP-A', 1, 8, 1, '2026-03-08');
INSERT INTO shop_a_orders VALUES (104, 'SHOP-A', 9, 33, 1, '2026-03-08');
INSERT INTO shop_a_orders VALUES (105, 'SHOP-A', 13, 2, 1, '2026-03-08');
INSERT INTO shop_a_orders VALUES (106, 'SHOP-A', 3, 30, 1, '2026-03-09');
INSERT INTO shop_a_orders VALUES (107, 'SHOP-A', 13, 13, 3, '2026-03-08');
INSERT INTO shop_a_orders VALUES (108, 'SHOP-A', 6, 4, 1, '2026-03-10');
INSERT INTO shop_a_orders VALUES (109, 'SHOP-A', 6, NULL, 2, '2026-03-09');
INSERT INTO shop_a_orders VALUES (110, 'SHOP-A', 2, 10, 2, '2026-03-10');
INSERT INTO shop_a_orders VALUES (111, 'SHOP-A', 3, 8, 1, '2026-03-11');
INSERT INTO shop_a_orders VALUES (112, 'SHOP-A', 1, 4, 1, '2026-03-11');
INSERT INTO shop_a_orders VALUES (113, 'SHOP-A', 11, 10, 1, '2026-03-11');
INSERT INTO shop_a_orders VALUES (114, 'SHOP-A', 6, 12, 1, '2026-03-11');
INSERT INTO shop_a_orders VALUES (115, 'SHOP-A', 1, 33, 1, '2026-03-11');
INSERT INTO shop_a_orders VALUES (116, 'SHOP-A', 1, 6, 1, '2026-03-11');
INSERT INTO shop_a_orders VALUES (117, 'SHOP-A', 9, 11, 2, '2026-03-12');
INSERT INTO shop_a_orders VALUES (118, 'SHOP-A', 16, 21, 1, '2026-03-13');
INSERT INTO shop_a_orders VALUES (119, 'SHOP-A', 6, 21, 1, '2026-03-13');
INSERT INTO shop_a_orders VALUES (120, 'SHOP-A', 14, 32, 2, '2026-03-13');
