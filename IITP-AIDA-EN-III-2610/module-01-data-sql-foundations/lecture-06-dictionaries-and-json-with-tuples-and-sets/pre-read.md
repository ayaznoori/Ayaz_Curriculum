## <span style="color:#2F7DDE">Dictionaries and JSON with Tuples and Sets</span>

### <span style="color:#2F7DDE">Mental Map</span>

```mermaid
%%{init: {'flowchart': {'nodeSpacing': 45, 'rankSpacing': 55, 'padding': 20}}}%%
flowchart TB
  CUR["<b>Current Session</b><br/>Dictionaries and JSON with Tuples and Sets"]
  Q["<b>The Big Question</b><br/><i>How does a payment app find one payee's details in a long list?</i>"]
  CV["<b>Course use case</b><br/>Store one merchant's fields in a Python map before loading rows into SQL"]
  RL["<b>Real-world example</b><br/>RupeeRing shows your saved UPI payees on the home screen"]

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

Have you ever wondered how RupeeRing opens Anita's UPI card without mixing her up with Arun?

By the end of this session, you will be able to:

- <span style="color:#D9660B">**Build**</span> a payee card for Anita at `anita@rupeering` and read her display name from it.
- <span style="color:#D9660B">**Retrieve**</span> Anita's cashback value safely when that field is missing on her card.
- <span style="color:#D9660B">**Check**</span> whether `shop@rupeering` sits on RupeeRing's allowed merchant list.
- <span style="color:#D9660B">**Write**</span> one payment tuple and unpack its id, amount, and status into names.
- <span style="color:#D9660B">**Construct**</span> a set from six favourite tags and count how many unique tags remain.
- <span style="color:#D9660B">**Classify**</span> each field in a RupeeRing API message by the Python type it becomes.

> <span style="color:#2F7DDE">**Topics you will meet:**</span> Dictionary (key and value); Safe lookup with get; Search with in; Tuple and unpacking; Set (remove duplicates); JSON as a dictionary.
>
> Join the session to learn each of these in detail.

---

### <span style="color:#2F7DDE">Why You Are Learning This Topic</span>

You open RupeeRing to pay your college canteen. You tap a saved payee, not a search box.
The app must match one UPI id to one row of details. It must also skip repeat tags in your history.
Sometimes the server sends a text blob that your notebook must turn into Python values.
A <span style="color:#D9660B">**dictionary**</span> is a labeled box: each label points to one value.
In this course you will meet the same shapes inside files and SQL steps later.
You already used lists and strings; now you add labeled records and deduped tags.

> <span style="color:#2F7DDE">**Think about it:**</span> What breaks if two payees share the same label?

---

### <span style="color:#2F7DDE">RupeeRing Payee Puzzle</span>

RupeeRing stores three recent payees for your phone.

| Payee label on screen | UPI id |
|:---------------------:|:------:|
| Anita | anita@rupeering |
| Canteen | canteen@rupeering |
| Metro card | metro@rupeering |

<span style="color:#D9660B">**What you want to happen:**</span>

- Tap Anita and see her UPI id, not the canteen's id.
- Mark `metro@rupeering` as allowed without scanning the whole list by hand.
- Show three unique spend tags when the history lists `food` twice.

> <span style="color:#D9660B">**Wonder about this:**</span>
>
> - How can the app return zero cashback when that field was never saved?
> - Why might six tag strings collapse to three unique labels?

---

### <span style="color:#2F7DDE">Think It Through</span>

There is no wrong first try. Keep your guesses for the session.

**1. Anita's card holds `name` and `upi`. Which part is the label you look up?**
Hint: Think about the word you would say before the colon on a form.

**2. You have four saved ids in a list. How would you ask Python if `canteen@rupeering` is on it?**
Hint: You already tested truth values with `if` in an earlier session.

**3. The server sends `{"amount": 120, "paid": true}` as one text string. What Python type is the whole message after parsing?**
Hint: The topic name compares the message shape to another container you will meet today.

---

### <span style="color:#2F7DDE">One Question to Carry Into the Session</span>

> <span style="color:#2F7DDE">**How do dictionaries, tuples, sets, and JSON text work together on one RupeeRing payment?**</span>
>
> Which container would you pick first to store payee labels, and why?