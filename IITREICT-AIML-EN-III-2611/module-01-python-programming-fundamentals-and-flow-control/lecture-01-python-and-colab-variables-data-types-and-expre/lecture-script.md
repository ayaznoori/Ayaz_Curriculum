# <font color='#1d4ed8'>Lecture Script: Python and Colab: Variables, Data Types, and Expressions</font>

---

## <font color='blue'>Agenda</font>

The lecture runs as four topics. Each topic ends with a quiz.

| Topic | What we do | Learning objectives covered | Minutes |
|:-:|:--|:--|:-:|
| 1 | Open Colab and run the first pack line | Work in a Google Colab notebook and run Python code | 25 |
| 2 | Name hub values and spot each kind | Use variables and the core data types: int, float, string, and boolean | 30 |
| 3 | Multiply lines and compare to a cap | Build expressions with arithmetic and comparison operators | 30 |
| 4 | Fix quoted box count and read the printout | Convert between types and avoid common beginner errors<br>Print and inspect results to check your work | 25 |
| — | Closing: Outcome & Summary | | 10 |
| | **Total** | | **120** |

> <font color="red">**🎯 Instructor Note**</font> Pace: keep Colab clicks to five minutes inside Topic 1; spend time on quoted `"2"` versus `2` in Topic 4.
> Run every code cell live; learners mirror in their own blank notebook.

---

## <font color='blue'>Scenario</font>

**The risk:** A Blinkit-style neighbourhood grocery hub must print three pack lines on a rider slip before the bike leaves. If one box count stays as quoted text, the mango line total is wrong and the customer may refuse the bag.

| Pack row | Name on slip | Count or flag (invented) |
|:--|:--|:--|
| Mango crate | Alphonso Mango | 2 boxes at ₹180 each |
| Fruit bunch | Banana | 3 bunches at ₹40 each |
| Dairy tub | Curd | `"1"` tub saved as text at ₹55 |

> <font color="red">**🎯 Instructor Note**</font> Blinkit is only the setting; counts and prices are invented for teaching.
> No `data/` upload today; rows live as named values in notebook cells. Later sessions may add a `data/` folder for larger tables.

---

## <font color='blue'>Problem Statement</font>

The hub helper typed mango boxes as text `"2"` but multiplied before turning the text into a whole number. The slip showed a nonsense mango line instead of ₹360. She fixed `mango_boxes = 2` and got the right total, but she never printed all three lines in one cell. The rider still could not tell whether mango, banana, and curd matched the screen at the gate.

> <font color='purple'>**How do named values and expressions let Colab fix a rider slip without redoing every step by hand?**</font>

> <font color="red">**🎯 Instructor Note**</font> Poll: "Which value is text: `2`, `\"2\"`, or `True`?" Give learners 30 seconds to respond in chat. Reveal the answer in the Closing.

---

## <font color='blue'>What We Will Use</font>

Today you work only in **Google Colab**: a **markdown cell** for notes and a **code cell** for Python. Each code block below is one cell; click the play button or press Shift+Enter to run it.

| Topic | Tools | In one line |
|:-:|:--|:--|
| 1 | Colab code and markdown cells, `print` | Run Python and see output under the cell |
| 2 | `=`, names, `int`, `float`, `str`, `bool`, `type` | Store each pack fact and see its kind |
| 3 | `*`, `+`, `>`, `==` | Build row totals and compare to a cap |
| 4 | `int`, `print`, fixing quoted numbers | Convert text to numbers and read the screen |

---

## <font color='blue'>How: Walking Through the Rider Slip Check</font>

```mermaid
flowchart LR
    A["Topic 1<br>Colab cells"] --> B["Topic 2<br>Names and types"]
    B --> C["Topic 3<br>Totals and compares"]
    C --> D["Topic 4<br>Convert and print"]
    D --> E["Closing<br>Slip matches screen"]
    style A fill:#2563eb,stroke:#1d4ed8,color:#ffffff
    style B fill:#16a34a,stroke:#15803d,color:#ffffff
    style C fill:#d97706,stroke:#b45309,color:#ffffff
    style D fill:#7c3aed,stroke:#6d28d9,color:#ffffff
    style E fill:#dc2626,stroke:#b91c1c,color:#ffffff
```

---

## <font color='blue'>Topic 1: Open Colab and Run the First Pack Line</font> `25 min`

> <font color='purple'>**Where do you type pack numbers so one run updates the slip?**</font>

Open a new **Google Colab** notebook. Add a markdown cell with the session title and your name. Add a code cell for Python. Only the code cell runs when you press the play icon or Shift+Enter.

### <font color='green'>Example: three named values from the mango row</font>

> <font color='purple'>**What prints for pack name, box count, and price per box?**</font>

A **variable** is a name with an `=` sign that holds one value. Use lowercase words with underscores between them.

**Predict before running: What will happen?**

> <font color="red">**🎯 Instructor Note**</font> Expected three lines: `Alphonso Mango`, `2`, `180`. Common wrong guess: all three on one line without three `print` calls.

```python
pack_name = "Alphonso Mango"
box_count = 2
price_per_box = 180
print(pack_name)
print(box_count)
print(price_per_box)
```

**Output**

```
Alphonso Mango
2
180
```

#### <font color='#c2410c'>Code Explanation</font>

- **Lines 1 to 3** Quotes make text. Numbers without quotes are whole numbers stored under names.
- **Lines 4 to 6** Each `print` shows one value in the output area under the cell.

> <font color='green'>**Result**</font> The notebook now holds the mango row facts the helper would need on screen.

### <font color='green'>Extending it: text without quotes</font>

> <font color='purple'>**What happens if the pack name has no quotes?**</font>

> <font color="red">**🎯 Instructor Note**</font> Ask for a prediction. Expected: `NameError`, because `Alphonso` is not a defined name.

```python
pack_name = Alphonso
```

**Output**

```
Traceback (most recent call last):
  File "<cell>", line 1, in <module>
NameError: name 'Alphonso' is not defined
```

> <font color='green'>**Result**</font> Without quotes, Python treats `Alphonso` as another variable name. No such name exists, so the cell stops.

> <font color='#b45309'>**Common mistake**</font> Putting spaces inside a name. Use `pack_name`, not `pack name`.

### <font color='purple'>Quiz 1</font>

**Question:** You want Python to calculate the mango line total. Which cell do you run?

**Options:**
- A) A markdown cell only
- B) A code cell in Google Colab
- C) The browser tab title at the top of the page
- D) The Colab menu bar with no code inside

**Correct Answer:** B

**Explanation:**
- **A)** Wrong: markdown holds notes; it does not run Python.
- **B)** Correct: only a code cell runs Python when you press play.
- **C)** Wrong: the browser tab title is not a notebook cell.
- **D)** Wrong: menus do not run code unless a code cell has statements.

---

## <font color='blue'>Topic 2: Name Hub Values and Spot Each Kind</font> `30 min`

> <font color='purple'>**The poll asked about quoted values. What kind is each pack fact?**</font>

Each value has a **data type**. Today you meet **int** (whole number), **float** (decimal), **str** (string text), and **bool** (`True` or `False`).

### <font color='green'>Example: four kinds on one rider slip</font>

> <font color='purple'>**What four type names appear for box count, price, pack name, and rider-ready flag?**</font>

**Predict before running: What will happen?**

> <font color="red">**🎯 Instructor Note**</font> Expected four `<class '...'>` lines ending in `int`, `float`, `str`, `bool`.

```python
box_count = 2
price_per_box = 180.0
pack_name = "Banana"
is_ready_for_rider = True
print(type(box_count))
print(type(price_per_box))
print(type(pack_name))
print(type(is_ready_for_rider))
```

**Output**

```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

#### <font color='#c2410c'>Code Explanation</font>

- **Lines 1 to 4** Each `=` stores one value: whole number, decimal, quoted text, and a true flag.
- **Lines 5 to 8** `type(...)` reports the class name for that value.

> <font color='green'>**Result**</font> You can point at each value on the slip and name its type before doing math.

### <font color='green'>Extending it: digits still inside quotes</font>

> <font color='purple'>**The screen shows mango boxes as `"2"`. Is it a whole number yet?**</font>

```python
box_count_text = "2"
print(type(box_count_text))
```

**Output**

```
<class 'str'>
```

> <font color='green'>**Result**</font> Digits inside quotes stay **str** until you convert them. That is why the mango line broke when the helper multiplied too early.

### <font color='purple'>Quiz 2</font>

**Question:** What type does `type(180.0)` report for the price per box?

**Options:**
- A) `<class 'int'>`
- B) `<class 'float'>`
- C) `<class 'str'>`
- D) `<class 'bool'>`

**Correct Answer:** B

**Explanation:**
- **A)** Wrong: `180.0` has a decimal point, so it is not an int.
- **B)** Correct: numbers with a decimal are float.
- **C)** Wrong: `180.0` is not inside quotes.
- **D)** Wrong: only `True` or `False` are bool.

---

## <font color='blue'>Topic 3: Build Totals and Compare to a Cap</font> `30 min`

> <font color='purple'>**How much is 2 mango boxes at ₹180, and does the banana line beat ₹100?**</font>

An **expression** combines values with **operators**. Use `*` and `+` for money math. Use `>` or `==` to compare a total to a cap on the hub screen.

### <font color='green'>Example: mango line total</font>

> <font color='purple'>**What single number prints for 2 boxes times ₹180?**</font>

**Predict before running: What will happen?**

> <font color="red">**🎯 Instructor Note**</font> Expected: `360`. Common wrong guess: `2180` from treating values as text — that mistake appears in Topic 4.

```python
mango_boxes = 2
mango_price = 180
mango_line_total = mango_boxes * mango_price
print(mango_line_total)
```

**Output**

```
360
```

#### <font color='#c2410c'>Code Explanation</font>

- **Lines 1 and 2** Names hold count and unit price as whole numbers.
- **Line 3** `*` multiplies boxes by price into one expression result.
- **Line 4** `print` shows the line total the rider should see.

> <font color='green'>**Result**</font> Alphonso Mango shows ₹360 without retyping both numbers.

### <font color='green'>Extending it: add banana and compare the line</font>

> <font color='purple'>**What is the slip total after banana, and is ₹120 above ₹100?**</font>

```python
banana_bunches = 3
banana_price = 40
banana_line_total = banana_bunches * banana_price
slip_so_far = mango_line_total + banana_line_total
print(slip_so_far)
```

**Output**

```
480
```

```python
print(banana_line_total)
print(banana_line_total > 100)
```

**Output**

```
120
True
```

> <font color='green'>**Result**</font> Mango plus banana is ₹480. Banana at 3 bunches is ₹120, which is greater than ₹100, so the compare line prints `True`.

### <font color='purple'>Quiz 3</font>

**Question:** Banana is 3 bunches at ₹40. Which expression gives the banana line total?

**Options:**
- A) `banana_bunches + banana_price`
- B) `banana_bunches / banana_price`
- C) `banana_bunches - banana_price`
- D) `banana_bunches * banana_price`

**Correct Answer:** D

**Explanation:**
- **A)** Wrong: `+` adds count and price, which is not the line total.
- **B)** Wrong: division would shrink the price, not build a row total.
- **C)** Wrong: subtraction does not model bunches times price.
- **D)** Correct: bunches multiplied by price per bunch matches the screen.

---

## <font color='blue'>Topic 4: Convert Quoted Box Count and Check the Printout</font> `25 min`

> <font color='purple'>**The screen still has `"2"` for mangoes. How do you multiply safely and read every line?**</font>

Use `int(...)` when quoted digits must become whole numbers before `*`. Use `print` with several values so you can **check your work** against the hub screen.

### <font color='green'>Example: fix quoted boxes then multiply</font>

> <font color='purple'>**What box count and mango total print after conversion?**</font>

**Predict before running: What will happen?**

> <font color="red">**🎯 Instructor Note**</font> Expected: `2` and `360` on one line from the last `print`.

```python
mango_boxes_text = "2"
mango_boxes = int(mango_boxes_text)
mango_price = 180
mango_line_total = mango_boxes * mango_price
print(mango_boxes, mango_line_total)
```

**Output**

```
2 360
```

#### <font color='#c2410c'>Code Explanation</font>

- **Line 1** Quoted `"2"` is still str on the slip photo.
- **Line 2** `int` builds a whole number you can multiply.
- **Lines 3 to 4** Price and total use numeric types only.
- **Line 5** Printing both values lets you confirm count and money together.

> <font color='green'>**Result**</font> Mango matches ₹360 once text becomes a whole number before math.

### <font color='green'>Extending it: adding text to a number</font>

> <font color='purple'>**What breaks if you add `"2"` and `180` without converting?**</font>

```python
broken_total = "2" + 180
```

**Output**

```
Traceback (most recent call last):
  File "<cell>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

> <font color='green'>**Result**</font> Python will not mix str and int with `+`. Convert first, then multiply or add numbers.

> <font color='#b45309'>**Common mistake**</font> Multiplying `"2" * 180` repeats text instead of charging for boxes — always convert box count before price math.

### <font color='green'>Extending it: one print line for the whole slip</font>

> <font color='purple'>**Do mango, banana, and curd totals still match 360, 120, and 55?**</font>

```python
curd_tubs = 1
curd_price = 55
curd_line_total = curd_tubs * curd_price
print("Mango", mango_line_total, "Banana", banana_line_total, "Curd", curd_line_total)
```

**Output**

```
Mango 360 Banana 120 Curd 55
```

> <font color='green'>**Result**</font> One print line shows every row total so you can compare the notebook to the hub screen.

### <font color='purple'>Quiz 4</font>

**Question:** Box count is saved as `box_count = "2"`. What is the safe next step before `box_count * 180`?

**Options:**
- A) `box_count = int(box_count)`
- B) `box_count = box_count + 180`
- C) `box_count = "2" * 180`
- D) `box_count = print(box_count)`

**Correct Answer:** A

**Explanation:**
- **A)** Correct: `int` turns quoted digits into a whole number for math.
- **B)** Wrong: you cannot add a string and an int without converting.
- **C)** Wrong: `"2" * 180` repeats characters; it is not a price total.
- **D)** Wrong: `print` shows a value; it does not convert the variable.

---

## <font color='blue'>Closing: Outcome & Summary</font> `10 min`

> <font color='purple'>**1. Which value was text in the opening poll: `2`, `\"2\"`, or `True`?**</font>

`"2"` is text (str) because of the quotes. `2` is a whole number (int). `True` is a bool flag.

> <font color='purple'>**2. Does the full slip notebook match the hub screen totals?**</font>

```python
print("Mango", mango_line_total, "Banana", banana_line_total, "Curd", curd_line_total)
```

**Output**

```
Mango 360 Banana 120 Curd 55
```

#### <font color='#c2410c'>Code Explanation</font>

- **Line 1** Reuses totals from Topics 3 and 4 so one run proves every row.

### <font color='green'>Outcome</font>

| | Wrong slip (quoted `"2"` held for math) | Fixed Colab notebook |
|:--|:-:|:-:|
| Mango line | broken or untrusted | ₹360 |
| Banana line | ₹120 | ₹120 |
| Curd line | ₹55 | ₹55 |
| Banana above ₹100? | unclear | Yes (`True`) |

> <font color='green'>**Therefore,**</font> named variables let you change one box count and refresh every expression; converting quoted digits before multiply is what makes the rider slip match the hub screen without redoing each step by hand.

> <font color="red">**🎯 Instructor Note**</font> Reveal the poll: `"2"` was the text value. Point at the Outcome table mango column.

### <font color='green'>Summary</font>

| Learning objective | Takeaway |
|:--|:--|
| Work in a Google Colab notebook and run Python code | Markdown for notes, code cells for Python, play or Shift+Enter to run |
| Use variables and the core data types: int, float, string, and boolean | Names with `=` hold values; `type` shows int, float, str, bool |
| Build expressions with arithmetic and comparison operators | `*` and `+` build totals; `>` answers hub caps |
| Convert between types and avoid common beginner errors | `int(...)` on quoted box counts before price math |
| Print and inspect results to check your work | One `print` with all row totals catches mismatches fast |
| **Practical value** | Any hub tablet that stores counts as text becomes fixable once you name values, convert safely, and read the cell output |

---

# <font color='red'>Launch the Feedback Poll</font>

> <font color="red">**🎯 Instructor Note**</font> Reminder: launch the feedback poll now to collect learner feedback.