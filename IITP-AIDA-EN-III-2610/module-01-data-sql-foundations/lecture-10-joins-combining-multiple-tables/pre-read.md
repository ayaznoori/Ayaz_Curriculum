## <span style="color:#2F7DDE">Joins: Combining Multiple Tables</span>

### <span style="color:#2F7DDE">Mental Map</span>

```mermaid
%%{init: {'flowchart': {'nodeSpacing': 45, 'rankSpacing': 55, 'padding': 20}}}%%
flowchart TB
  CUR["<b>Current Session</b><br/>Joins: Combining Multiple Tables"]
  Q["<b>The Big Question</b><br/><i>How do you match two lists on a shared id without losing the rows that find no partner?</i>"]
  CV["<b>Course use case</b><br/>Match 120 Seller A orders to a 30-product list and a 36-buyer list in your database tool"]
  RL["<b>Real-world example</b><br/>A hostel warden matches laundry bag tags to the student sheet before Sunday pickup"]

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

Have you ever wondered how the hostel warden matches each laundry bag to the right student?

By the end of this session, you will be able to:

- <span style="color:#D9660B">**Identify**</span> the shared student id that links bag B-1 to Ananya on the sheet.
- <span style="color:#D9660B">**Predict**</span> the number of report lines when Ananya has two bags, B-1 and B-2.
- <span style="color:#D9660B">**Determine**</span> which students, such as Priya and Meera, have no bag in the log.
- <span style="color:#D9660B">**Compare**</span> four ways to treat bag B-4, whose student id is missing from the sheet.
- <span style="color:#D9660B">**Trace**</span> which three lists and which id columns a bag, student and wing question needs.
- <span style="color:#D9660B">**Justify**</span> which list must keep every row when the warden asks for all students or all bags.

> <span style="color:#2F7DDE">**Topics you will meet:**</span> Keys and INNER JOIN; LEFT RIGHT and FULL JOIN; Unmatched rows (IS NULL); Row count after a join; Join three tables.
>
> Choosing the join a reporting question needs; Reading the schema a question needs.
>
> Join the session to learn each of these in detail.

---

### <span style="color:#2F7DDE">Why You Are Learning This Topic</span>

On Sunday, the hostel warden collects one laundry bag from each student.
Every bag carries a tag with a student id.
The student sheet holds names and wings. The laundry log holds bag tags and kilograms.
A tag alone does not tell the warden whose bag it is.
She must match each tag id to an id on the sheet.

A <span style="color:#D9660B">**join**</span> means placing two lists side by side by matching a shared column.

You will use the same match on Seller A orders, products and buyers.

> <span style="color:#2F7DDE">**Think about it:**</span> What should the warden do with a bag whose student id is not on the sheet?

---

### <span style="color:#2F7DDE">The Hostel Laundry Puzzle</span>

The warden keeps two small lists. A third list maps each wing letter to a wing warden.

**Student sheet**

| Student id | Name | Wing |
|:----------:|:----:|:----:|
| S-01 | Ananya | A |
| S-02 | Priya | A |
| S-03 | Karthik | B |
| S-04 | Meera | B |

**Laundry log**

| Bag | Student id | Weight (kg) |
|:---:|:----------:|:-----------:|
| B-1 | S-01 | 3 |
| B-2 | S-01 | 2 |
| B-3 | S-03 | 4 |
| B-4 | S-07 | 5 |

<span style="color:#D9660B">**What you want to happen:**</span>

- Bag B-1 shows Ananya's name beside 3 kg.
- Bag B-4 stays on the report, even though S-07 is missing from the sheet.
- Priya and Meera appear on a list of students with no bag.

> <span style="color:#D9660B">**Wonder about this:**</span>
>
> - How long is the report when Ananya owns two bags?
> - What shows in the name box for bag B-4?

---

### <span style="color:#2F7DDE">Think It Through</span>

There is no wrong first try. Keep your guesses for the session.

**1. Which column links a laundry bag to a student?**
Hint: Find the value that both lists share.

**2. Ananya has bags B-1 and B-2. What is the line count with her name on a bag report?**
Hint: Count one line per bag, not one per student.

**3. Which students never handed in a bag?**
Hint: Look for ids on the sheet that the log never uses.

---

### <span style="color:#2F7DDE">One Question to Carry Into the Session</span>

> <span style="color:#2F7DDE">**When two lists share an id, which rows must stay if they find no partner?**</span>
>
> Would your answer change if the warden wants every student listed, or every bag?
