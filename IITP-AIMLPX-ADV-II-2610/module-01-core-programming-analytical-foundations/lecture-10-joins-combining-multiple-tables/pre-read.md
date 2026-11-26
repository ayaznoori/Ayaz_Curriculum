## <span style="color:#2F7DDE">Joins: Combining Multiple Tables</span>

### <span style="color:#2F7DDE">Mental Map</span>

```mermaid
%%{init: {'flowchart': {'nodeSpacing': 45, 'rankSpacing': 55, 'padding': 20}}}%%
flowchart TB
  CUR["<b>Current Session</b><br/>Joins: Combining Multiple Tables"]
  Q["<b>The Big Question</b><br/><i>How do you match two lists without losing a student or a slip?</i>"]
  CV["<b>Course use case</b><br/>Match 120 Seller A orders to 30 products and 36 buyers in Workbench"]
  RL["<b>Real-world example</b><br/>A teacher matches the class list with permission slips before the trip bus leaves"]

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

Have you ever wondered how a teacher knows which students have not handed in a trip slip?

By the end of this session, you will be able to:

- <span style="color:#D9660B">**Identify**</span> which roll numbers appear in both the class list and the slip box, and which students have no slip.
- <span style="color:#D9660B">**Predict**</span> the line count of a combined sheet when roll number 101 handed in two slips.
- <span style="color:#D9660B">**Use**</span> a third list, the bus seat chart, to add each student's seat to the same sheet.
- <span style="color:#D9660B">**Compare**</span> four ways to line up two lists by which unmatched names stay on the page.
- <span style="color:#D9660B">**Examine**</span> a drawing of three lists to name the shared column and the columns a question needs.
- <span style="color:#D9660B">**Justify**</span> which way of lining up the lists answers "who still owes a slip?"

> <span style="color:#2F7DDE">**Topics you will meet:**</span> Keys and INNER JOIN; LEFT RIGHT and FULL JOIN; Unmatched rows (IS NULL).
>
> Row count after a join; Join three tables; Choosing the join a reporting question needs; Reading the schema a question needs.
>
> Join the session to learn each of these in detail.

---

### <span style="color:#2F7DDE">Why You Are Learning This Topic</span>

Before a class trip, the teacher holds a class list in one hand. A box of permission slips sits on the desk.

Each slip has a roll number. She matches every slip to a name, one by one.

One slip carries a roll number that is not on the list. Two students have no slip at all.

A <span style="color:#D9660B">**join**</span> means placing two tables side by side by matching a shared column, such as a roll number.

You will join Seller A's order, product and buyer tables in this course.

> <span style="color:#2F7DDE">**Think about it:**</span> If the teacher only keeps students who have a slip, who disappears from her sheet?

---

### <span style="color:#2F7DDE">The Class Trip Puzzle</span>

Here is the class list and the slip box, matched by roll number.

| Roll number | Name on the class list | Slip in the box |
|:-----------:|:----------------------:|:---------------:|
| 101 | Asha | Yes, two copies |
| 102 | Bilal | No |
| 103 | Chitra | Yes |
| 104 | Dev | No |
| 109 | Not on the class list | Yes |

<span style="color:#D9660B">**What you want to happen:**</span>

- One sheet that shows each student next to their slip.
- A short list of the students who still owe a slip.
- A way to spot the slip that has no name.

> <span style="color:#D9660B">**Wonder about this:**</span>
>
> - Does Asha's name print once or twice when she handed in two slips?
> - What should the sheet do with the slip for roll number 109?

---

### <span style="color:#2F7DDE">Think It Through</span>

There is no wrong first try. Keep your guesses for the session.

**1. Which roll numbers appear on both the class list and in the slip box?**
Hint: Tick the numbers that you find in both places.

**2. What is the line count of the sheet if all four students stay and Asha's two slips each get a line?**
Hint: Count four students, then add one extra line for Asha's second slip.

**3. The teacher also has a bus seat chart with a roll number beside each seat. How could it join the same sheet?**
Hint: Use the shared roll number again.

---

### <span style="color:#2F7DDE">One Question to Carry Into the Session</span>

> <span style="color:#2F7DDE">**Which lines must stay on the sheet, and which way of matching keeps exactly those lines?**</span>
>
> Bring one guess about what happens to Bilal and Dev when only matching lines are kept.
