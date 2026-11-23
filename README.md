# AIML — pre-reads and lecture scripts

Published course content for IITP AIML batches. Each batch is a top-level folder (batch id from the INI sheet).

## Repository layout

```
├── README.md
├── templates/
│   ├── pre-read-template.md
│   └── lecture-script-template.md
├── <batch-id>/
│   ├── module-01-<topic>/
│   │   ├── lecture-01-<topic>/
│   │   │   ├── pre-read.md
│   │   │   ├── lecture-script.md
│   │   │   ├── data/          # optional; upload to Colab for file sessions
│   │   │   └── images/        # optional; charts at width 900 in the script
│   │   └── ...
│   └── ...
└── ...
```

**Batches in this repo**

| Batch id |
|---|
| `IITP-AIMLPX-ADV-II-2610` |
| `IITP-AIDA-EN-III-2610` |
| `IITP-AIAG-TA-I-2610` |
| `IITREICT-DSAI-EN-IV-2611` |

Session folders are created when pre-reads and lecture scripts are added. Optional assets for a session (for example `images/` or `data/`) live inside that session’s `lecture-XX-<topic>/` folder.

**Templates** under `templates/` are reference skeletons only. Session files in batch folders are the source of truth.

**Remote:** [github.com/ayaznoori/Ayaz_Curriculum](https://github.com/ayaznoori/Ayaz_Curriculum/tree/main)

## Curriculum CSV (local, not in this repo)

Authoring uses `.local/curricula/<batch-id>/curriculum.csv` from the INI export. Important columns:

| Column | Use in content |
|---|---|
| Session Title | Folder name and verbatim lecture title |
| Topics | Pre-read “Topics you will meet”; four lecture topics |
| LO_Statement | Verbatim LOs in lecture Agenda and Closing |
| **Tools Used** | **Runtime and platform** — must match the script (see below) |

Resolve a session (paths, LOs, tools):

```bash
python3 tools/resolve_session.py "Session Title" --course IITP-AIDA-EN-III-2610 --json
```

Context for bridges (completed sessions + **tools_used** on target):

```bash
python3 lecture/tools/curriculum_context.py .local/curricula/<batch-id>/curriculum.csv "Session Title" --json
```

## Tools Used → how to write

Read the **Tools Used** cell for the session before drafting. Typical IITP-AIDA-EN-III-2610 patterns:

| Tools Used (CSV) | Pre-read | Lecture script |
|---|---|---|
| Google Colab | Mention **notebook cells**; file paths only as future filenames, not terminal commands | **What We Will Use** states Colab; upload `data/`; each block is a **code cell**; tracebacks use `File "<cell>"`; Instructor Note for Colab file upload |
| ChatGPT; Claude; Gemini | “AI tool” in outcomes if session teaches prompt + test fix | Topic that teaches debugging names the tools; paste prompt in prose; **re-run the Colab cell** before accepting |
| (SQL / MySQL later rows) | No live SQL in pre-read unless taught | Per SQL playbook when CSV says so |

Do **not** write a file-I/O session as local terminal Python (`<stdin>` tracebacks, “run python script.py”) when **Tools Used** is Google Colab.

## Authoring checklist (before push)

1. `python3 lecture/tools/check_script.py` on `lecture-script.md` (structure, LOs, images).
2. `/tmp/lecvenv/bin/python3 tools/verify_lecture_script.py` on the session (Output, images, **Tools Used**, plain language).
3. Regenerated PNG → **new filename** and update `img src` (GitHub may cache same path).
4. Push only under `<batch-id>/` (not `tools/`, `lecture/tools/`, or `.cursor/skills/`).

Skills (local): `.cursor/skills/aiml-preread-lecture`, `aiml-lecture-verify`.