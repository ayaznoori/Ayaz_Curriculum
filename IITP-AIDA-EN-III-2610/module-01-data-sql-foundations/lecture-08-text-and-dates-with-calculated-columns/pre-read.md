## <span style="color:#2F7DDE">Text and Dates with Calculated Columns</span>

### <span style="color:#2F7DDE">Mental Map</span>

```mermaid
%%{init: {'flowchart': {'nodeSpacing': 45, 'rankSpacing': 55, 'padding': 20}}}%%
flowchart TB
  CUR["<b>Current Session</b><br/>Text and Dates with Calculated Columns"]
  Q["<b>The Big Question</b><br/><i>How can one report line build a tidy name, a day count, and a fine from raw columns?</i>"]
  CV["<b>Course use case</b><br/>Shape 120 Seller A order rows with ship dates and blank delivery fields"]
  RL["<b>Real-world example</b><br/>The college library desk stamps return dates on borrowing cards"]

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

Have you ever wondered how the library slip shows a late fee without hand copying dates?

By the end of this session, you will be able to:

- <span style="color:#D9660B">**Identify**</span> the month on card B-104 from its due date in the register.
- <span style="color:#D9660B">**Apply**</span> a text clean-up to `  ananya rao  ` on card B-101 before printing.
- <span style="color:#D9660B">**Calculate**</span> overdue days between due and return for card B-101 in February.
- <span style="color:#D9660B">**Determine**</span> a ₹8 late fee from 4 days at ₹2 per day on card B-103.
- <span style="color:#D9660B">**Demonstrate**</span> fee 8.00 rupees with two decimals on slip B-103.
- <span style="color:#D9660B">**Check**</span> which cards still lack a return date, such as B-102 on the shelf list.

> <span style="color:#2F7DDE">**Topics you will meet:**</span> Text functions; Date parts; Date difference; Calculated columns; ROUND and CAST; Missing values (IS NULL).
>
> Join the session to learn each of these in detail.

---

### <span style="color:#2F7DDE">Why You Are Learning This Topic</span>

You return a novel on Thursday. The clerk types your name from the card.

Extra spaces hide in the saved name. The screen needs a neat title case line.

Due date and today’s stamp sit on one row. Days late must show without counting.

The fine is days late times ₹2. That total prints beside your card number.

Books still out need a short list. The clerk keeps only rows with an empty return date.

A **calculated column** means a new value built from other fields in the same row.

You will build columns when you clean Seller A shipment rows in a database tool.

> <span style="color:#2F7DDE">**Think about it:**</span> What breaks if the clerk copies dates by hand?

---

### <span style="color:#2F7DDE">The Library Desk Puzzle</span>

The register lists four loans from this week.

| Card | Borrower (as stored) | Due date | Return date |
|:----:|:---------------------|:--------:|:-----------:|
| B-101 | `  ananya rao  ` | 2026-02-01 | 2026-02-05 |
| B-102 | `PRIYA DAS` | 2026-02-10 | |
| B-103 | `karthik menon` | 2026-02-08 | 2026-02-12 |
| B-104 | `Meera Iyer` | 2026-03-01 | 2026-02-28 |

<span style="color:#D9660B">**What you want to happen:**</span>

- Card B-101 prints borrower Ananya Rao from messy stored text.
- Card B-103 shows 4 overdue days and an ₹8 fine on the slip.
- The shelf list shows only cards with no return date, including B-102.

> <span style="color:#D9660B">**Wonder about this:**</span>
>
> - How would you split one due date into year, month, and day?
> - How would you spot missing return dates without reading every row?

---

### <span style="color:#2F7DDE">Think It Through</span>

There is no wrong first try. Keep your guesses for the session.

**1. Card B-104 was due 2026-03-01 but returned 2026-02-28. What sign might the day gap show?**
Hint: See which date comes first on the calendar.

**2. Card B-101 stores `  ananya rao  ` with edge spaces. What fixes run before print?**
Hint: Think about text edges and letter size.

**3. Card B-102 has an empty return date. How might you list only books still out?**
Hint: Ask which rows lack a return value.

---

### <span style="color:#2F7DDE">One Question to Carry Into the Session</span>

> <span style="color:#2F7DDE">**How do text steps and date steps chain in one query to make a fine column?**</span>
>
> Will the same pattern work on 120 Seller A orders with missing delivery dates?