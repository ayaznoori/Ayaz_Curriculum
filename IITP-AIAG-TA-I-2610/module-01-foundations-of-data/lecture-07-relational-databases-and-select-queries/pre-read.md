## <span style="color:#2F7DDE">Relational Databases and SELECT Queries</span>

### <span style="color:#2F7DDE">Mental Map</span>

```mermaid
%%{init: {'flowchart': {'nodeSpacing': 45, 'rankSpacing': 55, 'padding': 20}}}%%
flowchart TB
  CUR["<b>Current Session</b><br/>Relational Databases and SELECT Queries"]
  Q["<b>The Big Question</b><br/><i>How does a desk pull the right product rows from a 100-row grid without opening every cell?</i>"]
  CV["<b>Course use case</b><br/>Return title and price columns for Seller A shop SHOP-A from a 100-row product table"]
  RL["<b>Real-world example</b><br/>The railway reservation counter shows only trains that match your cities and travel dates"]

  CUR ==> Q
  Q ==>|&nbsp;Used in the course&nbsp;| CV
  Q ==>|&nbsp;Seen in real life&nbsp;| RL

  classDef currSes fill:#ef6c00,stroke:#e65100,color:#ffffff,stroke-width:3px
  classDef ask fill:#1565c0,stroke:#0d47a1,color:#ffffff,stroke-width:3px
  classDef val fill:#2e7d32,stroke:#1b5e20,color:#ffffff,stroke-width:3px

  class CUR currSes
  class Q ask
  class CV,RL val

  linkStyle default stroke-width:3px
```

---

### <span style="color:#2F7DDE">What You'll Learn</span>

Have you ever wondered how Seller A’s desk shows kurtas under ₹600 from a 100-row sheet?

By the end of this session, you will be able to:

- <span style="color:#D9660B">**Identify**</span> table, row, and column roles in Seller A’s SHOP-A grid.
- <span style="color:#D9660B">**Describe**</span> how schema labels name each field in `seller_product_codes.csv`.
- <span style="color:#D9660B">**Apply**</span> a ₹499 price cutoff on SHOP-A rows for the review screen.
- <span style="color:#D9660B">**Use**</span> AND and OR with brackets for kurtas priced ₹400 to ₹800.
- <span style="color:#D9660B">**Check**</span> a KRT- code pattern and a March listed date on one run.
- <span style="color:#D9660B">**Plan**</span> a sort with category A to Z and price high to low together.

> <span style="color:#2F7DDE">**Topics you will meet:**</span> Tables rows and schema; SELECT; WHERE; AND OR and NOT.
>
> IN LIKE and date range (BETWEEN); ORDER BY.
>
> Join the session to learn each of these in detail.

---

### <span style="color:#2F7DDE">Why You Are Learning This Topic</span>

Seller A opens Monday’s 100-row export after a festival weekend.

You need titles and prices for SHOP-A only.

Blank prices appear on four rows. Codes like KRT-0412-RD need pattern checks.

The manager wants March listings first, then top price per category.

A **relational database** means data stored in tables with named columns and one row per record.

In this course you will ask that table for named columns instead of scrolling by hand.

> <span style="color:#2F7DDE">**Think about it:**</span> What breaks if you hide the wrong rows when two filters disagree?

---

### <span style="color:#2F7DDE">The Seller A Stock Desk Puzzle</span>

Five sample rows sit on Seller A’s desk screen.

| product_code | title | price_rupees | shop_code | listed_date |
|:------------:|:------|:------------:|:---------:|:-----------:|
| KRT-0412-RD | Cotton Kurta Red | 499 | SHOP-A | 2025-03-08 |
| KRT-0891-BL | Linen Kurta Blue | 650 | SHOP-A | 2025-03-15 |
| TOP-2201-WH | Cotton Top White | 299 | SHOP-B | 2025-02-20 |
| KRT-1104-GR | Festival Kurta Green | 799 | SHOP-A | 2025-04-02 |
| DUP-3300-GL | Silk Dupatta Gold | 450 | SHOP-A | 2025-03-22 |

<span style="color:#D9660B">**What you want to happen:**</span>

- Show only `title` and `price_rupees` for SHOP-A.
- Keep March 2025 kurtas priced ₹400 to ₹800.
- Sort those rows by falling price, then product code.

> <span style="color:#D9660B">**Wonder about this:**</span>
>
> - How would you hide TOP-2201-WH while keeping SHOP-A rows?
> - Why might KRT-1104-GR vanish under a March date rule?

---

### <span style="color:#2F7DDE">Think It Through</span>

There is no wrong first try. Keep your guesses for the session.

**1. Which two columns would you show if the cashier needs names and prices only?**
Hint: Picture the narrow strip on the review tablet.

**2. Which rows stay when you demand shop code SHOP-A and a kurta title?**
Hint: Read each title, not only the code prefix.

**3. How would you line up March SHOP-A kurtas with the highest price on top?**
Hint: Lock the date window first, then flip price order.

---

### <span style="color:#2F7DDE">One Question to Carry Into the Session</span>

> <span style="color:#2F7DDE">**How do you ask a product table for Seller A rows in order without copying the sheet?**</span>
>
> Which single filter would you try first on the five-row sample above?

---

### <span style="color:#2F7DDE">Set Up Before the Session</span>

> <span style="color:#2F7DDE">**Do this before the session starts.**</span> You will run queries in a desktop database tool, not in Colab. SQLite or MySQL Workbench (not Colab).