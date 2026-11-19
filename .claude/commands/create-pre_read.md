Parse the arguments: $ARGUMENTS

The arguments are quoted strings in this order:
1. module_name — the module the session belongs to (context only, never printed in the pre-read)
2. session_name — the session title
3. topics — the topics to cover, separated by semicolons
4. learning_objectives — the objectives, separated by semicolons
5. setup — `Yes` or `No`
6. setup_text — only when setup is Yes: the setup text or documentation link to paste

If any of arguments 1 to 5 is missing, ask for all missing inputs in one short message. Never guess them.
If setup is `Yes` and there is no setup_text, ask the user to paste it. If setup is `No`, skip the Set Up section.

Execute the following pipeline:

## Step 1 — Create the output folder

Run from the workspace root (the folder that contains `preread/` and `CLAUDE.md`):

```python
from datetime import date
import re, os

session_name = "<parsed from arg 2>"
root = os.getcwd()
assert os.path.isdir(os.path.join(root, 'preread')), "Run this from the workspace root"
safe_name = re.sub(r'[^\w\s-]', '', session_name).strip().replace(' ', '_')
folder_name = f"{safe_name}_{date.today().strftime('%Y-%m-%d')}"
folder_path = os.path.join(root, folder_name)
os.makedirs(folder_path, exist_ok=True)
print(folder_path)
```

If `{folder_path}/preread.md` already exists, ask the user before overwriting it.

## Step 2 — Invoke the creator agent

Spawn the `agent_preread_creator` agent with these inputs:
- module_name (from arg 1)
- session_name (from arg 2)
- topics (from arg 3)
- learning_objectives (from arg 4)
- setup (from arg 5)
- setup_text (from arg 6, only when setup is Yes)
- folder_path (from Step 1)

Wait for it to finish. It saves `preread.md` only. No PNG is created. Outcome bullets open with Bloom's verbs from the bank in `preread/guidelines.md`. Any code preview is tested before it stays.

## Step 3 — Invoke the reviewer agent

Spawn the `agent_preread_verifier` agent with:
- preread_path: `{folder_path}/preread.md`
- module_name, session_name, topics, learning_objectives and setup (from the arguments)

## Step 4 — Report

Print to the user:
- Path to the saved `preread.md`
- Status: Accepted / Rejected, with iterations and fixes applied
- The scenario the pre-read uses
- Remarks (if rejected)
- Anything unverified, such as a pasted link that was not opened
