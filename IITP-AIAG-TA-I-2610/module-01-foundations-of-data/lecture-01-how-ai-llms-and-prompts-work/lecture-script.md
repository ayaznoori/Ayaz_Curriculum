# <font color='#1d4ed8'>Lecture Script: How AI, LLMs and Prompts Work</font>

---

## <font color='blue'>Agenda</font>

The lecture runs as four topics. Each topic ends with a quiz.

| Topic | What we do | Learning objectives covered | Minutes |
|:-:|:--|:--|:-:|
| 1 | Sort the three AI labels | Compare AI, machine learning and generative AI by what each term covers | 20 |
| 2 | Watch words get chosen and split | Describe next-token prediction as the mechanism that produces an LLM response<br>Describe how a tokenizer splits text into subword tokens | 30 |
| 3 | Fit the message in the window | Explain what a context window limits and what counts against it<br>Predict how raising temperature changes the variability of an output | 35 |
| 4 | Spot fluent wrong facts and fix the prompt | Explain why a model can produce fluent text that is factually wrong<br>State the four elements of a well-formed prompt: task, context, format and constraints | 25 |
| — | Closing: Outcome & Summary | | 10 |
| | **Total** | | **120** |

> <font color="red">**🎯 Instructor Note**</font> Pace: keep Topic 1 naming-only; spend most live demo time in Topics 3 and 4 on ChatGPT, Claude, and Gemini free chat pages.

---

## <font color='blue'>Scenario</font>

Seller A sells cotton kurtas on a large shopping app. The listing needs a short blurb: fabric, size range, and wash care.

An intern opens a free chat page, pastes one line from an old catalog, and ships the reply without reading it.

| Field | Seller A value (invented for teaching) |
|:--|:--|
| Product title | Cotton Kurta — Blue |
| Fabric on the label | 100% cotton |
| Sizes live on site | S, M, L, XL |
| Wash line on label | Cold wash, dry in shade |

> <font color="red">**🎯 Instructor Note**</font> A Flipkart-style app is only the setting; do not claim Seller A or these rows are real. Data is invented for teaching.

---

## <font color='blue'>Problem Statement</font>

The intern’s chat reply said “silk blend, dry clean only.” The listing went live. A buyer ordered for daily college wear, opened the parcel, and filed a return.

Seller A’s mentor asked for one repeatable way to draft blurbs: right facts, steady tone, and a prompt anyone on the team can reuse.

> <font color='purple'>**How do we use free chat tools so Seller A’s blurbs stay factual, fit the message limit, and do not invent fabric or care rules?**</font>

> <font color="red">**🎯 Instructor Note**</font> Poll: “Is a smooth product blurb always safe to paste live?” Give learners 30 seconds to respond in chat. Reveal the answer in the Closing.

---

## <font color='blue'>What We Will Use</font>

Every topic uses the same three free chat pages in the browser. No notebook is required today.

| Topic | Tools | In one line |
|:-:|:--|:--|
| 1 | ChatGPT (Free plan) | Name which broad label fits text-generating chat tools |
| 2 | Claude (Free plan) | Watch how one reply is built word by word and split into tokens |
| 3 | Gemini (Free plan) | See how pasted listing rows fill the reading limit and how settings change reruns |
| 4 | ChatGPT, Claude, Gemini | Compare fluent wrong lines and rewrite using task, context, format, constraints |

---

## <font color='blue'>How: Walking Through Seller A’s Blurb</font>

```mermaid
flowchart LR
    A["Topic 1<br>Three AI labels"] --> B["Topic 2<br>Next token and pieces"]
    B --> C["Topic 3<br>Window and temperature"]
    C --> D["Topic 4<br>Hallucination and prompt shape"]
    D --> E["Closing<br>One safe blurb rule"]
    style A fill:#2563eb,stroke:#1d4ed8,color:#ffffff
    style B fill:#16a34a,stroke:#15803d,color:#ffffff
    style C fill:#d97706,stroke:#b45309,color:#ffffff
    style D fill:#7c3aed,stroke:#6d28d9,color:#ffffff
    style E fill:#dc2626,stroke:#b91c1c,color:#ffffff
```

---

## <font color='blue'>Topic 1: Three AI Labels</font> `20 min`

> <font color='purple'>**Seller A’s intern said “the AI decided.” Which family of tools actually writes listing text—and how is that different from every smart app on the phone?**</font>

### <font color='green'>Example: map the three labels to Seller A’s task</font>

> <font color='purple'>**Where does a chat page that drafts blurbs sit inside the wider AI map?**</font>

$$\boxed{\text{Generative AI} \subset \text{Machine learning} \subset \text{Artificial intelligence}}$$

Artificial intelligence is the wide label for software that handles tasks that look intelligent, such as recommending similar kurtas.

Machine learning is a part of AI where patterns are learned from examples, such as ranking search results.

Generative AI is a part of machine learning that creates new text (or images). Seller A’s blurb draft comes from a **generative** text model.

#### <font color='#c2410c'>Logic Explanation</font>

- **Outermost circle** Any rule-based chat bot from ten years ago could still count as AI, but it is not what you use today for blurbs.
- **Middle circle** A fraud score on orders uses machine learning but does not write sentences.
- **Inner circle** ChatGPT, Claude, and Gemini free chat pages are generative AI tools focused on language.

> <font color='green'>**Result**</font> Seller A is not “using AI” in the vague sense—they are using a generative text model, which is one slice inside machine learning and the wider AI idea.

<p align="center"><img src="images/01_ai_ml_genai_nesting.png" alt="Nested circles: artificial intelligence contains machine learning, which contains generative AI for text chat tools" width="900"></p>

### <font color='green'>Extending it: same tool, three names in the news</font>

> <font color='purple'>**A headline says “AI tutor,” another says “machine learning model,” a third says “generative AI copilot.” Which headline points at blurb writing?**</font>

> <font color="red">**🎯 Instructor Note**</font> Expected: only the generative AI / copilot headline. Give learners 30 seconds to respond in chat.

#### <font color='#c2410c'>Logic Explanation</font>

- **AI tutor** could mean many things; ask what it creates.
- **Machine learning model** might score risk or demand; ask if it outputs full sentences.
- **Generative AI copilot** signals text creation—closest to Seller A’s blurb job.

> <font color='green'>**Result**</font> For Seller A, the useful label is generative AI, because the deliverable is new product text.

> <font color='#b45309'>**Common mistake**</font> Calling every smart feature “AI” hides the fact that only generative tools write blurbs.

### <font color='purple'>Quiz 1</font>

**Question:** Seller A uses a free chat page to draft a kurta blurb. Which term is most precise for that tool?

**Options:**
- A) Generative AI, because it creates new text from a prompt
- B) Artificial intelligence only, because every app is AI
- C) Machine learning only, with no generative piece
- D) A fixed rule list that never learns from data

**Correct Answer:** A

**Explanation:**
- **A)** Correct: blurb writing is text generation, a generative AI use case.
- **B)** Too broad; many AI systems never write listings.
- **C)** Too narrow a name; generative models are a subset of machine learning.
- **D)** Describes old rule bots, not modern chat pages.

---

## <font color='blue'>Topic 2: Next Token and Pieces</font> `30 min`

> <font color='purple'>**The intern pressed Enter once and got a full sentence. Did the model plan the whole blurb in one flash?**</font>

### <font color='green'>Example: one word at a time</font>

> <font color='purple'>**What mechanism produces the visible reply on the chat page?**</font>

$$\boxed{\text{next-token prediction: pick the next word, append it, repeat}}$$

Open Claude (Free plan). Type only: `Cotton kurta for Seller A:` and stop. Watch the reply grow.

The model does not jump to the final blurb in one jump. It repeatedly asks: “Given everything so far, what is the likely next word?”

#### <font color='#c2410c'>Logic Explanation</font>

- **Each step** The hidden state is the prompt plus every word already shown.
- **Each choice** Many words get scores; one is sampled or taken as top choice (depends on settings).
- **Stops when** an end-of-text signal or length limit appears—not when a human would pause.

> <font color='green'>**Result**</font> A fluent blurb is a chain of many next-word choices, not a single lookup from a table of blurbs.

<p align="center"><img src="images/02_next_token_probabilities.png" alt="Horizontal bars showing invented scores for four candidate next words after a partial slogan" width="900"></p>

### <font color='green'>Extending it: tokenizer subword pieces</font>

> <font color='purple'>**Before the model scores the next word, how does it read `Cotton Kurta — Blue`?**</font>

A **tokenizer** splits text into **tokens**—often whole words, but long or rare words may split into subword pieces.

Invented teaching split for `RoboRally`-style text:

| Piece index | Text piece |
|:-:|:--|
| 1 | `Cotton` |
| 2 | ` Kur` |
| 3 | `ta` |
| 4 | ` —` |
| 5 | ` Blue` |

The model never sees the string as one unbroken blob; it sees numbered tokens.

#### <font color='#c2410c'>Logic Explanation</font>

- **Subword split** helps the model handle rare product names without a dictionary entry for every long product code.
- **Spaces and punctuation** often become their own tokens.
- **Your prompt length** is counted in tokens, not characters—important for Topic 3.

> <font color='green'>**Result**</font> Seller A’s title can cost more tokens than a shorter name because of how pieces are split.

<p align="center"><img src="images/03_tokenizer_subword_pieces.png" alt="Four colored boxes showing subword pieces of a festival title example" width="900"></p>

### <font color='green'>Extending it: same prompt, first word fork</font>

> <font color='purple'>**If two interns run the same opening line, why might the first chosen word already differ?**</font>

> <font color="red">**🎯 Instructor Note**</font> Expected: randomness from sampling and tiny setting differences between tools. Demo the same one-line prompt in ChatGPT and Gemini.

#### <font color='#c2410c'>Logic Explanation</font>

- **Sampling** The model may roll among high-scoring words instead of always picking the top one.
- **Tool differences** Free plans can use different default creativity settings even when the typed prompt matches.

> <font color='green'>**Result**</font> Next-token prediction explains both fluency and early drift between reruns.

### <font color='purple'>Quiz 2</font>

**Question:** Which statement best describes how an LLM reply appears in the chat window?

**Options:**
- A) The model retrieves one stored blurb that exactly matches the product title
- B) The model repeatedly picks a next token until the reply ends
- C) The model runs a SQL query on Seller A’s live database
- D) The model only reorders words the user already typed, with no new words

**Correct Answer:** B

**Explanation:**
- **A)** Wrong: responses are built, not fetched as a whole document.
- **B)** Correct: next-token prediction builds the answer stepwise.
- **C)** Not in scope; free chat pages do not query Seller A’s database here.
- **D)** Generative models add new tokens beyond the prompt.

---

## <font color='blue'>Topic 3: Window and Temperature</font> `35 min`

> <font color='purple'>**The intern pasted four old blurbs plus the full size chart. The reply ignored XL wash care. What limit did they hit?**</font>

### <font color='green'>Example: context window budget</font>

> <font color='purple'>**What does a context window limit, and what counts against it?**</font>

$$\boxed{\text{context window} = \text{max tokens the model can attend to at once (prompt + reply)}}$$

Everything you paste counts: title, fabric facts, your instructions, and earlier chat turns on the same thread.

| Item pasted (invented) | Approx. tokens (teaching) |
|:--|:-:|
| Seller A title and fabric facts | 28 |
| Three old blurbs | 210 |
| Size and wash table | 180 |
| Your instruction paragraph | 55 |
| **Subtotal in prompt** | **473** |

If the window for a free plan is smaller than your pile, the model may drop or forget the bottom lines—such as “cold wash, dry in shade.”

#### <font color='#c2410c'>Logic Explanation</font>

- **Prompt tokens** All instructions and pasted catalog text in the message box.
- **Reply tokens** The generated blurb also sits inside the same window while it is being written.
- **Not counted** Files sitting on your laptop that you never pasted into the chat.

> <font color='green'>**Result**</font> Seller A should paste only the facts needed for one listing, not the entire season catalog in one message.

<p align="center"><img src="images/04_context_window_fill.png" alt="Bar chart showing most of an example 100-token window filled by pasted prompt text" width="900"></p>

### <font color='green'>Extending it: temperature and variability</font>

> <font color='purple'>**Same facts, same prompt—why does run two sound more poetic than run one?**</font>

**Temperature** controls how strongly the model explores lower-scoring next tokens.

| Setting (wording varies by tool) | Effect on Seller A blurb reruns (teaching) |
|:--|:--|
| Lower / more focused | Wording stays closer between reruns |
| Higher / more creative | More adjectives and more line-to-line change |

$$\boxed{\text{higher temperature} \Rightarrow \text{more variability across reruns}}$$

On Gemini (Free plan), run the same Seller A prompt twice at default settings, then compare if your UI exposes a creativity slider.

> <font color="red">**🎯 Instructor Note**</font> Expected: higher creativity means wider word choice, not guaranteed better facts. Give learners 30 seconds to respond in chat.

#### <font color='#c2410c'>Logic Explanation</font>

- **Temperature does not fetch new facts** It only changes which likely words are picked.
- **Marketing tone** Often wants moderate creativity after facts are fixed in the prompt.
- **Compliance tone** Often wants low creativity so wash lines stay stable.

> <font color='green'>**Result**</font> Variability is a setting effect, not proof that the model rechecked the label.

<p align="center"><img src="images/05_temperature_variability.png" alt="Two bars comparing low versus high temperature spread between reruns on an example index" width="900"></p>

### <font color='purple'>Quiz 3</font>

**Question:** Seller A pastes six long PDF blurbs and wonders why XL wash care vanished from the reply. What is the best explanation?

**Options:**
- A) The model refused cotton products by policy
- B) Pasted text used too much of the context window, so later facts were lost
- C) Temperature was zero so the model could not write the word “wash”
- D) Tokenizer removed every digit from sizes

**Correct Answer:** B

**Explanation:**
- **A)** Fabric policy is unrelated to window limits.
- **B)** Correct: oversized prompts exceed what the model can attend to at once.
- **C)** Low temperature narrows word choice; it does not delete care instructions by itself.
- **D)** Tokenizers do not strip digits as a rule.

---

## <font color='blue'>Topic 4: Hallucination and Prompt Shape</font> `25 min`

> <font color='purple'>**The silk-blend line read beautifully. Why was it still wrong—and how do we rewrite the message so the tool stays on the label facts?**</font>

### <font color='green'>Example: fluent but false</font>

> <font color='purple'>**Why can a model sound confident when the fabric line is false?**</font>

A **hallucination** (in this course) means fluent generated text that does not match real facts.

The model optimizes for likely next words given language patterns, not for reading Seller A’s physical label.

Show learners this invented wrong line:

> Soft **silk blend** kurta; **dry clean only**; ideal for evening wear.

Label truth: **100% cotton**, **cold wash**, daily wear.

#### <font color='#c2410c'>Logic Explanation</font>

- **Language patterns** “Silk blend” often appears near “kurta” in training text, even when your label says cotton.
- **No live label check** The free chat page does not automatically open Seller A’s warehouse photo.
- **Human check** Compare every material and care claim to the four-row fact table in the Scenario.

> <font color='green'>**Result**</font> Smooth wording is not evidence. Seller A needs a person or a checklist against source facts.

### <font color='green'>Extending it: four prompt elements</font>

> <font color='purple'>**What belongs in one well-formed prompt for Seller A’s kurta blurb?**</font>

$$\boxed{\text{prompt} = \text{task} + \text{context} + \text{format} + \text{constraints}}$$

| Element | Seller A content (invented) |
|:--|:--|
| Task | Write one listing blurb for the blue cotton kurta |
| Context | Title, 100% cotton, sizes S–XL, cold wash, dry in shade |
| Format | Two short sentences, plain English, no bullet symbols |
| Constraints | Do not name other fabrics; do not add dry clean; under 45 words |

Paste a single message with all four parts into ChatGPT (Free plan). Rerun once in Claude (Free plan) with the same text.

> <font color="red">**🎯 Instructor Note**</font> Expected: outputs stay closer to cotton and cold wash. Poll tie-in: fluency ≠ safety.

#### <font color='#c2410c'>Logic Explanation</font>

- **Task** Stops the model from guessing your goal (title vs FAQ vs email).
- **Context** Supplies the only facts it should echo.
- **Format** Sets length and shape so uploads stay consistent.
- **Constraints** States forbidden inventions (silk, dry clean).

> <font color='green'>**Result**</font> The four-element prompt is Seller A’s reusable template—not a one-line “write a blurb” wish.

<p align="center"><img src="images/06_four_prompt_elements.png" alt="Four labeled boxes for task, context, format, and constraints in a product blurb prompt" width="900"></p>

### <font color='green'>Extending it: quick check on three tools</font>

> <font color='purple'>**Do all three free chat pages obey constraints every time?**</font>

#### <font color='#c2410c'>Logic Explanation</font>

- **Same prompt** should be typed, not paraphrased, when comparing tools.
- **Any violation** (silk, dry clean) means edit the blurb manually—do not publish.
- **Next session** you will run Python in Colab; today’s skill is prompt shape and model behaviour.

> <font color='#b45309'>**Common mistake**</font> Trusting the first neat sentence because it matches the tone of last season’s catalog.

### <font color='purple'>Quiz 4</font>

**Question:** Which prompt line is the **constraint** for Seller A?

**Options:**
- A) “Product: Cotton Kurta — Blue”
- B) “Write two short sentences”
- C) “Do not mention silk or dry clean only”
- D) “Sizes S, M, L, XL”

**Correct Answer:** C

**Explanation:**
- **A)** Context fact, not a rule about forbidden text.
- **B)** Format instruction.
- **C)** Correct: tells the model what not to invent.
- **D)** Context fact about sizes.

---

## <font color='blue'>Closing: Outcome & Summary</font> `10 min`

Seller A needs one blurb pattern that survives free chat tools, intern turnover, and reruns.

> <font color='purple'>**1. Which label fits the chat tools you used today?**</font>

Generative AI inside machine learning inside the wider AI label—because the output is new listing text.

> <font color='purple'>**2. How is the blurb actually produced?**</font>

Next-token prediction builds the reply piece by piece; the tokenizer turns your pasted facts into tokens that fill the context window.

> <font color='purple'>**3. Why did wash care disappear when too much was pasted?**</font>

The context window budget was spent on old blurbs; temperature only changes word choice, not label reading.

> <font color='purple'>**4. Was the silk line safe because it sounded polished?**</font>

No—that was hallucination. The fix is a four-part prompt plus a human check against the Scenario table.

### <font color='green'>Outcome</font>

| Check | Weak one-line prompt | Four-element prompt |
|:--|:-:|:-:|
| Names cotton correctly | Sometimes | Usually |
| Keeps cold wash line | Often dropped when paste is huge | Stays when context is short |
| Avoids silk / dry clean | Often fails | Fails less; still needs human read |
| Stable across reruns | Low | Higher with lower creativity |

> <font color='green'>**Therefore,**</font> Seller A should treat chat output as a draft: generative models guess language, limits and settings shape variability, and a structured prompt plus fact check prevents fluent wrong blurbs.

> <font color="red">**🎯 Instructor Note**</font> Reveal poll answer: smooth blurbs are **not** always safe. Point to the silk-blend mistake.

### <font color='green'>Summary</font>

| Learning objective | Takeaway |
|:--|:--|
| Compare AI, machine learning and generative AI by what each term covers | Blurb chat tools are generative AI—a slice of ML inside the wider AI idea |
| Describe next-token prediction as the mechanism that produces an LLM response | Replies grow one token at a time by scoring what comes next |
| Describe how a tokenizer splits text into subword tokens | Your title and paste are counted as pieces, not one invisible string |
| Explain what a context window limits and what counts against it | Prompt + reply share a token budget; huge pastes drop facts |
| Predict how raising temperature changes the variability of an output | Higher creativity widens wording swings between reruns |
| Explain why a model can produce fluent text that is factually wrong | Likely language ≠ verified label facts—hallucination |
| State the four elements of a well-formed prompt: task, context, format and constraints | Seller A reuses all four so every intern sends the same shape of message |
| **Practical value** | You can open ChatGPT, Claude, or Gemini on the free plan, send a structured prompt, and verify output before anything goes live |

---

# <font color='red'>Launch the Feedback Poll</font>

> <font color="red">**🎯 Instructor Note**</font> Reminder: launch the feedback poll now to collect learner feedback.