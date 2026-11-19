# AIML course content (pre-reads & lecture scripts)

Repository for IITP AIML batches: pre-reads and 120-minute lecture scripts generated from curriculum CSVs.

**Remote:** [github.com/ayaznoori/AIML](https://github.com/ayaznoori/AIML)

## Layout

```
courses/
  IITP-AIMLPX-ADV-II-2610/   curriculum.csv, prereads/, lecture-scripts/
  IITP-AIDA-EN-III-2610/
  IITP-AIAG-TA-I-2610/
preread/                     Pre-read team pipeline (guidelines, agents, template)
lecture/                     Lecture script team pipeline + tools/
.claude/commands/            Claude Code slash commands (optional)
tools/resolve_session.py     Match a session title to CSV row + batch
```

## Cursor

Use the project skill **aiml-preread-lecture** (`.cursor/skills/aiml-preread-lecture/SKILL.md`): ask to create a pre-read and/or lecture script by **session title**; optionally pass batch code if titles overlap.

## Claude Code (optional)

From this repo root:

```
/create-pre_read "Module" "Session" "Topics" "LOs" "No"
/create-lecture-script "Module" "Session" "Topics" "LOs" "No" "courses/<batch>/curriculum.csv"
```

Move outputs into the matching `courses/<batch>/prereads/` or `lecture-scripts/` folder.

## Resolve a session

```bash
python3 tools/resolve_session.py "Probability and Bayes Theorem" --json
python3 tools/resolve_session.py "Probability and Bayes Theorem" --course IITP-AIMLPX-ADV-II-2610 --json
```