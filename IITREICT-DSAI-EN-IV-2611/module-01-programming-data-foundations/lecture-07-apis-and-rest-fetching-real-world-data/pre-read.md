## <span style="color:#2F7DDE">APIs and REST: Fetching Real-World Data</span>

### <span style="color:#2F7DDE">Mental Map</span>

```mermaid
%%{init: {'flowchart': {'nodeSpacing': 45, 'rankSpacing': 55, 'padding': 20}}}%%
flowchart TB
  CUR["<b>Current Session</b><br/>APIs and REST: Fetching Real-World Data"]
  Q["<b>The Big Question</b><br/><i>How does a phone app show the next bus without you copying a file by hand?</i>"]
  CV["<b>Course use case</b><br/>In Colab you send a GET request and read JSON into lists and dictionaries"]
  RL["<b>Real-world example</b><br/>A RedBus-style tracker asks a server for live minutes at stop ST04 Koramangala"]

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

Have you ever wondered how the bus screen updates when the same stop has five different route numbers?

By the end of this session, you will be able to:

- <span style="color:#D9660B">**Explain**</span> why a **GET** call only asks the server to send data back without changing it.
- <span style="color:#D9660B">**Read**</span> a response and name the **status code**, the **URL**, and a **query parameter** such as `limit=5`.
- <span style="color:#D9660B">**Send**</span> a GET request from Python and print the status code plus one field from the JSON body.
- <span style="color:#D9660B">**Use**</span> an API key from the notebook environment instead of pasting it into a shared cell.

> <span style="color:#2F7DDE">**Topics you will meet:**</span> APIs; REST; HTTP Methods; Status Codes; Request-Response; API Keys; Responses to Datasets.
>
> Join the session to learn each of these in detail.

---

### <span style="color:#2F7DDE">Why You Are Learning This Topic</span>

Parth opens a RedBus-style city bus app before class.

Stop **ST04 Koramangala** shows five upcoming buses with minutes and route names.

Those rows were not typed into the app by hand.

The phone sent a short **GET** request to a web service, and the service answered with JSON text.

An **API** is the published door other programs use to ask that service for data in a fixed shape.

In this course you will send the same kind of request from **Google Colab** and turn the answer into Python lists you can loop over.

> <span style="color:#2F7DDE">**Think about it:**</span> What number should the app show when the server refuses the call because the key is missing?

---

### <span style="color:#2F7DDE">The Koramangala Stop Puzzle</span>

Five invented departure rows the API might return for one stop.

| Trip | Route | ETA (min) | Status |
|:---:|:-----:|:---------:|:------:|
| T041 | V-500 | 4 | on_time |
| T094 | KIA-14 | 10 | delayed |
| T080 | 335E | 15 | delayed |
| T112 | 500A | 18 | on_time |
| T058 | 201 | 22 | on_time |

<span style="color:#D9660B">**What you want to happen:**</span>

- Ask only for stop **ST04** and at most **5** rows.
- See status code **200** when the key is accepted.
- Drop any row with status **cancelled** before you show minutes on a chart.

> <span style="color:#D9660B">**Wonder about this:**</span>
>
> - Which HTTP method should only read data: GET or POST?
> - What status code fits a missing API key: **401**, **200**, or **404**?

---

### <span style="color:#2F7DDE">Think It Through</span>

| If you see… | It often means… |
|:--|:--|
| Status **200** | The server understood the request and sent a body back |
| Status **401** | The server wants a valid API key in the header |
| Status **404** | The path or stop id does not exist on this service |
| Query `limit=5` | Return at most five matching rows after sorting |

You already opened JSON files with dictionaries last week. This session the JSON arrives through one GET response instead of a file read.

---

### <span style="color:#2F7DDE">Before Session Checklist</span>

- Open **Google Colab** and confirm you can run a cell with `print("ready")`.
- Bring your notes on **dictionaries** and **lists** from the JSON session.
- Expect to upload the session **`data/`** folder when the mentor shares it. It holds invented bus rows and a small practice server file.

Join live to run **`requests.get`** against the practice server and build your first live dataset in the notebook.