## <span style="color:#2F7DDE">AI-Assisted SQL Writing and Checking</span>

### <span style="color:#2F7DDE">Mental Map</span>

```mermaid
%%{init: {'flowchart': {'nodeSpacing': 45, 'rankSpacing': 55, 'padding': 20}}}%%
flowchart TB
  CUR["<b>Current Session</b><br/>AI-Assisted SQL Writing and Checking"]
  Q["<b>The Big Question</b><br/><i>How do you get a correct answer from an AI helper and prove it matches what you asked?</i>"]
  CV["<b>Course use case</b><br/>Check a chat assistant's draft against a 100-row product table before it reaches a slide"]
  RL["<b>Real-world example</b><br/>You ask a friend to build a 5-song road-trip playlist from a shared sheet"]

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

Have you ever wondered why a friend's playlist looks perfect and still holds the wrong songs?

By the end of this session, you will be able to:

- <span style="color:#D9660B">**Interpret**</span> the rule "Hindi songs under 5 minutes, shortest first, first 5" in one sentence.
- <span style="color:#D9660B">**Solve**</span> a playlist rule that returns 9 songs instead of 5 by finding its wrong part.
- <span style="color:#D9660B">**Trace**</span> the order a playlist rule follows: open the sheet, filter, count, sort, then cut the list.
- <span style="color:#D9660B">**Compare**</span> asking a helper with no sample against asking with one playlist you already like.
- <span style="color:#D9660B">**Check**</span> a friend's rule against the sheet's column headings and against the request you made.
- <span style="color:#D9660B">**Write**</span> a clear request that names the sheet's columns and says what you want back.

> <span style="color:#2F7DDE">**Topics you will meet:**</span> Clause order in a query; Prompt for a SQL query; Zero-shot or few-shot: adding a worked example to a SQL prompt.
>
> Check AI SQL against the schema; Fix AI SQL mistakes; Explain what a query returns.
>
> Join the session to learn each of these in detail.

---

### <span style="color:#2F7DDE">Why You Are Learning This Topic</span>

You and four friends plan a road trip. You ask one friend to pick songs from a shared sheet.

The reply is a neat list of 5 songs. On the road, you hear a 9-minute song and a Tamil song. You wanted neither.

The list looked right, but nobody compared it with the sheet or with your request.

A <span style="color:#D9660B">**schema**</span> means the list of column headings in a table and what each heading holds.

In this course, an AI helper drafts a database question. You check the draft before you trust its numbers.

> <span style="color:#2F7DDE">**Think about it:**</span> What would you check before you play that playlist for the whole bus?

---

### <span style="color:#2F7DDE">The Road-Trip Playlist Puzzle</span>

Each row is one song on the shared sheet.

| Song | Language | Minutes | Mood |
|:----:|:--------:|:-------:|:----:|
| Highway Sunrise | Hindi | 4 | Happy |
| Chai Stop | Hindi | 3 | Calm |
| Midnight Rail | Tamil | 5 | Calm |
| Monsoon Drive | Hindi | 6 | Sad |
| Dhol Beat | Punjabi | 3 | Happy |

<span style="color:#D9660B">**What you want to happen:**</span>

- Keep only Hindi songs shorter than 5 minutes.
- Put the shortest song first.
- Stop after the first 5 songs.

> <span style="color:#D9660B">**Wonder about this:**</span>
>
> - Which songs does that rule pick from this sheet?
> - What goes wrong if the helper writes "length" when the sheet says "Minutes"?

---

### <span style="color:#2F7DDE">Think It Through</span>

There is no wrong first try. Keep your guesses for the session.

**1. Which songs stay when the rule says "Hindi, shorter than 5 minutes"?**
Hint: Test each row against both parts of the rule.

**2. Your friend writes "length" for the minutes column. Where do you look to spot it?**
Hint: Compare the word with the headings in the table.

**3. The list shows a Tamil song, but you asked for Hindi only. Which part of the rule is missing?**
Hint: Read the rule one wish at a time.

---

### <span style="color:#2F7DDE">One Question to Carry Into the Session</span>

> <span style="color:#2F7DDE">**How can you prove a helper's answer matches your request, and not only that it looks neat?**</span>
>
> Bring one check you would run before you share the list.
