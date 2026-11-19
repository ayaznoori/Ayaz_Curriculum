## <span style="color:#2F7DDE">How AI and LLMs Work with Prompts</span>

### <span style="color:#2F7DDE">Mental Map</span>

```mermaid
%%{init: {'flowchart': {'nodeSpacing': 45, 'rankSpacing': 55, 'padding': 20}}}%%
flowchart TB
  CUR["<b>Current Session</b><br/>How AI and LLMs Work with Prompts"]
  Q["<b>The Big Question</b><br/><i>Why does the same chat tool give different poster lines—and sometimes a wrong guest name?</i>"]
  CV["<b>Course use case</b><br/>Draft 3 seller product blurbs in a free AI chat before upload"]
  RL["<b>Real-world example</b><br/>Your batch WhatsApp group asks for one-line fest slogans by Friday"]

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

Have you ever wondered why two classmates paste the same opening line and still get different poster slogans?

By the end of this session, you will be able to:

- <span style="color:#D9660B">**Classify**</span> artificial intelligence, machine learning, and generative AI when your club picks a free chat tool for poster text.
- <span style="color:#D9660B">**Describe**</span> next-token prediction as the step that adds the next word to a one-line fest slogan draft.
- <span style="color:#D9660B">**Identify**</span> subword pieces inside the title `RoboRally 2026` before the model reads your poster request.
- <span style="color:#D9660B">**Explain**</span> what fills the reading limit when you paste three old posters plus this year’s date list.
- <span style="color:#D9660B">**Predict**</span> how raising the creativity setting changes two slogan endings from the same opening line.
- <span style="color:#D9660B">**State**</span> task, context, format, and constraints in one chat request after you spot a wrong guest name on the poster.

> <span style="color:#2F7DDE">**Topics you will meet:**</span> AI vs ML vs GenAI; Next-token prediction; Tokens context and temperature (why answers vary); Hallucination; Four elements of a prompt.
>
> Join the session to learn each of these in detail.

---

### <span style="color:#2F7DDE">Why You Are Learning This Topic</span>

Your cultural committee needs a fresh one-line slogan for Tech Fest.

You open a free chat page and type “Write a catchy line for RoboRally 2026.”

The first reply sounds perfect. You run it again and get a different rhyme.

Your friend pastes last year’s three posters plus a long guest list. The reply invents a speaker who never agreed to come.

A **prompt** means the full message you send the chat tool, including instructions and pasted notes.

Seller teams will use the same kind of chat page to draft product blurbs. You need to know what the tool is doing, not just copy the first reply.

> <span style="color:#2F7DDE">**Think about it:**</span> If the line reads smoothly, why would you still check the guest name before printing?

---

### <span style="color:#2F7DDE">The Tech Fest Poster Puzzle</span>

The committee keeps a small fact sheet for this year’s RoboRally poster.

| Fact | Value |
|:----:|:-----:|
| Event name | RoboRally 2026 |
| Dates | 14–16 March |
| Venue | Main auditorium |
| Confirmed guest | Dr. Meera Shah (robotics lab) |
| Tone needed | Short, student-friendly, under 12 words |

<span style="color:#D9660B">**What you want to happen:**</span>

- One chat request returns a slogan that fits the tone and length.
- A second run with the same facts does not surprise you with a wild swing unless you change a setting.
- No printed poster names a guest who is not on the fact sheet.

> <span style="color:#D9660B">**Wonder about this:**</span>
>
> - Why might the tool split `RoboRally` into more than one small piece before it answers?
> - What four parts would you put in your message so the tool knows the task, the facts, the shape, and the limits?

---

### <span style="color:#2F7DDE">Think It Through</span>

There is no wrong first try. Keep your guesses for the session.

**1. Your classmate says “the AI guessed the next word.” What do you think that means for slogan line two?**
Hint: Think about finishing a sentence one word at a time.

**2. You paste three old posters and a long guest list into one message. What might get cut off if the message is too long?**
Hint: Picture a fixed-size text box with a fill line.

**3. Two drafts both sound confident. How would you decide which guest name is safe to print?**
Hint: Compare each name to the fact sheet, not to how smooth the sentence sounds.

---

### <span style="color:#2F7DDE">One Question to Carry Into the Session</span>

> <span style="color:#2F7DDE">**What must you put in a prompt so a chat tool stays helpful instead of confidently wrong?**</span>
>
> Bring your guess about task, facts, format, and limits—and one example slogan you would not print without checking.