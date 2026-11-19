---
name: aiml-preread-lecture
description: >-
  Creates AIML course pre-reads and lecture scripts from session titles by matching
  curriculum CSV rows (title, topics, LO_Statement). Uses preread/ and lecture/ team
  pipelines, saves under courses/{batch}/, pushes to github.com/ayaznoori/AIML.
  Use when the user asks to create a pre-read, lecture script, or both by session title
  or batch code for IITP AIML courses.
---

# AIML pre-read and lecture script pipeline

Workspace root: the repo that contains `courses/`, `preread/`, and `lecture/`.

GitHub: `https://github.com/ayaznoori/AIML`

## Courses (batch codes)

| Batch folder | Curriculum |
|---|---|
| `IITP-AIMLPX-ADV-II-2610` | `courses/IITP-AIMLPX-ADV-II-2610/curriculum.csv` |
| `IITP-AIDA-EN-III-2610` | `courses/IITP-AIDA-EN-III-2610/curriculum.csv` |
| `IITP-AIAG-TA-I-2610` | `courses/IITP-AIAG-TA-I-2610/curriculum.csv` |

Outputs never go in the workspace root. Use:

- Pre-read: `courses/{batch}/prereads/{SafeSessionName}_{YYYY-MM-DD}/preread.md`
- Lecture: `courses/{batch}/lecture-scripts/{SafeSessionName}_{YYYY-MM-DD}/` (`lecture_script.md`, `images/`, `data/`)

## Step 0 — Resolve the session

From workspace root:

```bash
python3 tools/resolve_session.py "<Session Title>" --json
# optional: --course IITP-AIMLPX-ADV-II-2610
```

Use the JSON fields for pipeline arguments. Split `topics_semicolon` and `learning_objectives_semicolon` on `;` only at the pipeline boundary; LO text in the Agenda must stay **verbatim** from the CSV (`LO_Statement` segments).

If resolve fails or is ambiguous, ask the user for the exact **Session Title** or `--course` batch code. Never guess module, topics, or LOs.

Skip rows with empty `Session Title` or empty `LO_Statement` (Filler, Evaluation, etc.) unless the user explicitly requests them.

## Pre-read pipeline (Cursor)

Follow `.claude/commands/create-pre_read.md` and `preread/guidelines.md`, `preread/template.md`, `preread/agents/creator.md`, then `preread/agents/reviewer.md` (10 categories, fix in place).

**Arguments** (from resolve):

1. `module_name` — from CSV module column (context only, never printed)
2. `session_name` — `session_title`
3. `topics` — CSV Topics (`;` separated)
4. `learning_objectives` — CSV `LO_Statement` (`;` separated)
5. `setup` — `No` unless the user says Yes
6. `setup_text` — only if setup is Yes; paste user text exactly

Create the folder under `preread_output_dir` (not workspace root). Run preread self-checks from `preread/agents/creator.md`. Reviewer must accept before you treat the file as done.

**Claude Code equivalent** (same repo root):

```
/create-pre_read "Module" "Session" "Topic 1; Topic 2" "LO 1; LO 2" "No"
```

Then move the output folder into `courses/{batch}/prereads/`.

## Lecture script pipeline (Cursor)

Follow `.claude/commands/create-lecture-script.md`, `lecture/guidelines.md`, `lecture/terms.md`, `lecture/template.md`, `lecture/playbook.md`, creator then verifier agents under `lecture/agents/`.

**Arguments**:

1. `module_name`
2. `session_name`
3. `topics`
4. `learning_objectives` — verbatim LO segments from CSV
5. `announcements` — `No` unless the user says Yes (optional announcement text)
6. `curriculum_csv` — absolute path from resolve

Before writing:

```bash
python3 lecture/tools/curriculum_context.py "<curriculum_csv>" "<session_title>" --json
```

Exit code 2: show `ASK:` lines; ask the user; do not guess columns or session names.

Create output under `lecture_output_dir`. After writing:

```bash
python3 lecture/tools/check_script.py "<path>/lecture_script.md" \
  --los "<LO segments joined with ;>" --announcements no \
  --module "<module_name>" --session "<session_title>"
```

**Claude Code equivalent**:

```
/create-lecture-script "Module" "Session" "Topics" "LOs" "No" "courses/<batch>/curriculum.csv"
```

Then move the folder into `courses/{batch}/lecture-scripts/`.

## User requests

| User says | Do |
|---|---|
| Pre-read only | Pre-read pipeline only |
| Lecture script only | Lecture pipeline only |
| Both / default | Pre-read then lecture (same resolved row) |
| Push / GitHub | Commit relevant paths and `git push` (see below) |

## Git push

Remote: `origin` → `https://github.com/ayaznoori/AIML`

After new or updated artifacts:

```bash
git add courses/
git status
git commit -m "$(cat <<'EOF'
Add pre-read and lecture script for <Session Title> (<batch>).

EOF
)"
git push -u origin main
```

Push only when the user asks to push or their request implies publishing. Do not commit secrets or `.env`.

## Reference docs in repo

- Pre-read pack: `preread/SKILL.md`, team `README` content in skill above
- Lecture pack: `lecture/SKILL.md`, `lecture-examples/` for finished samples
- Commands: `.claude/commands/create-pre_read.md`, `.claude/commands/create-lecture-script.md`