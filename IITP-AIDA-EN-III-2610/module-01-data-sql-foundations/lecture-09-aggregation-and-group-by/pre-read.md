## <span style="color:#2F7DDE">Aggregation and GROUP BY</span>

### <span style="color:#2F7DDE">Mental Map</span>

```mermaid
%%{init: {'flowchart': {'nodeSpacing': 45, 'rankSpacing': 55, 'padding': 20}}}%%
flowchart TB
  CUR["<b>Current Session</b><br/>Aggregation and GROUP BY"]
  Q["<b>The Big Question</b><br/><i>How does a fest booth turn 200 coupon lines into one fair stall scoreboard?</i>"]
  CV["<b>Course use case</b><br/>Sum order amounts per delivery city from 120 rows in Workbench"]
  RL["<b>Real-world example</b><br/>A campus fest coupon booth prints stall totals at midnight"]

  CUR ==> Q
  Q ==>|&nbsp;Used in the course&nbsp;| CV
  Q ==>|&nbsp;Seen in real life&nbsp;| RL

  classDef currSes fill:#ffe0b2,stroke:#ef6c00,color:#4e342e,stroke-width:3px
  classDef ask fill:#e3f2fd,stroke:#1565c0,color:#0d47a1,stroke-width:3px
  classDef val fill:#e8f5e9,stroke:#2e7d32,color:#1b5e20

  class CUR currSes
  class Q ask
  class CV,RL val

  linkStyle default stroke-width:3px
```

---

### <span style="color:#2F7DDE">What You'll Learn</span>

Have you ever wondered how the fest desk ranks stalls without reading each coupon slip?

By the end of this session, you will be able to:

- <span style="color:#D9660B">**Calculate**</span> sum, average, high and low amounts for stall Chilli Bites in the coupon log.
- <span style="color:#D9660B">**Differentiate**</span> three count styles when row 14 leaves the stall name blank.
- <span style="color:#D9660B">**Apply**</span> one summary row per stall across five coupons in the sample log.
- <span style="color:#D9660B">**Determine**</span> which stall groups stay when the board cutoff is 400 rupees.
- <span style="color:#D9660B">**Compare**</span> a Friday row filter with a filter on stall totals over 400 rupees.
- <span style="color:#D9660B">**Trace**</span> clause run order and spot the extra column that breaks stall totals.

> <span style="color:#2F7DDE">**Topics you will meet:**</span> COUNT SUM AVG MIN and MAX; COUNT variations; GROUP BY; HAVING.
>
> WHERE vs HAVING; Fixing GROUP BY errors; The order a query's clauses run in.
>
> Join the session to learn each in detail.

---

### <span style="color:#2F7DDE">Why You Are Learning This Topic</span>

Friday night at the campus fest, volunteers tear coupon slips at six food stalls.
Each slip records stall name, rupee amount, and day.
The coordinator cannot add 200 lines in a head count.
She needs one total per stall, then only stalls above a sales target.
An **aggregation** means squashing matching rows into one number, such as a stall total.
You will run that stall summary on shop tables here.
The session shows which filter hits single rows and which hits stall groups.

> <span style="color:#2F7DDE">**Think about it:**</span> Should Friday-only coupons be dropped before or after the stall totals are added?

---

### <span style="color:#2F7DDE">The Fest Coupon Booth Puzzle</span>

Each row below is one torn fest coupon.

| Coupon code | Stall | Amount (Rs) | Day |
|:-----------:|:-----:|:-----------:|:---:|
| C-101 | Chilli Bites | 120 | Fri |
| C-102 | Chilli Bites | 150 | Fri |
| C-103 | Frost Cone | 80 | Fri |
| C-104 | Frost Cone | 90 | Fri |
| C-105 | Chilli Bites | 200 | Sat |

<span style="color:#D9660B">**What you want to happen:**</span>

- One rupee total for Chilli Bites and one for Frost Cone.
- Only stall groups with at least 400 rupees combined.
- Drop Saturday rows first, then build the scoreboard.

> <span style="color:#D9660B">**Wonder about this:**</span>
>
> - Does Chilli Bites reach 400 rupees if Saturday row C-105 is ignored?
> - Why might coupon code and stall name in one report break stall totals?

---

### <span style="color:#2F7DDE">Think It Through</span>

There is no wrong first try. Keep your guesses for the session.

**1. Count Chilli Bites rows in the table. What rupee sum do they make?**
Hint: Scan the stall column before you think about Friday or Saturday.

**2. Frost Cone shows 80 and 90 rupees. Does a 400 rupee cutoff keep that stall?**
Hint: Add the two amounts before you compare to 400.

**3. You want Friday-only totals, then stalls above 400 rupees. Which step comes first?**
Hint: Row pick by day comes before judging stall groups.

---

### <span style="color:#2F7DDE">One Question to Carry Into the Session</span>

> <span style="color:#2F7DDE">**When a fest report fails, is the row filter wrong, the group filter wrong, or a column unsquashed?**</span>
>
> Bring one guess about which clause runs before stall totals are added.