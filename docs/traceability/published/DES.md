### Table of Contents

    * 1.1 LLM session archive: hooks around llm-logs/tools/llmlog.py (DES001)
    * 1.2 Doorstop tree and its automated checks (DES002)
    * 1.3 setup.sh, the SessionStart hook and CI (DES003)

## 1.1 LLM session archive: hooks around llm-logs/tools/llmlog.py _(DES001)_ {#DES001}

**Implements** REQ001. `.claude/settings.json` registers four Claude Code hooks, each a one-line wrapper in `.claude/hooks/` around the single script `llm-logs/tools/llmlog.py`: `SessionStart` -> `session-start` (row in `sessions.csv`), `UserPromptSubmit` -> `prompt` (row in `prompt-log.csv`; system-injected turns starting with `<` are skipped), `Stop` -> `archive` (copy the transcript to `llm-logs/<id>/transcript.jsonl`, or `transcript.resumed.jsonl` if a larger archive already exists; regenerate `session.json`, `prompts.csv`, `PROMPTS-AND-RESPONSES.md` and `SESSIONS.md`; `git add llm-logs`), `SessionEnd` -> `archive` then `commit` (`git commit -o llm-logs` and push to the current branch). The script finds the repository from its own location, needs only Python 3 and git, catches every exception and always exits 0. `index` rebuilds all generated files from the archived transcripts; `archive --session-id --transcript` archives a session by hand when the hooks did not run.

*Parent links: REQ001*

*Child links: TST001*

## 1.2 Doorstop tree and its automated checks _(DES002)_ {#DES002}

**Implements** REQ002. Four Doorstop documents with `digits: 3`, empty separator and YAML items: `needs/` (NEED, root), `requirements/` (REQ, parent NEED), `design/` (DES, parent REQ), `tests/` (TST, parent DES). `tools/publish_traceability.sh` validates the tree and writes `docs/traceability/published/{NEED,REQ,DES,TST}.md`. `tests/test_traceability.py` loads the item YAML directly and checks the link rules of REQ002, runs `doorstop` and compares a fresh publish with the committed Markdown. HTML output is gitignored.

*Parent links: REQ002*

*Child links: TST002*

## 1.3 setup.sh, the SessionStart hook and CI _(DES003)_ {#DES003}

**Implements** REQ003. `setup.sh` creates `.venv` with the interpreter in `$PYTHON` (default `python3`), installs `requirements-dev.txt` (Doorstop pinned to 3.2, pytest, PyYAML), makes the hooks executable, runs `doorstop` and `llmlog.py index`. `.gitignore` excludes `.venv/`. `.claude/hooks/session-start.sh` runs `setup.sh` when `CLAUDE_CODE_REMOTE` is `true`. `.github/workflows/tests.yml` runs `setup.sh` and `pytest` on every push and pull request.

*Parent links: REQ003*

*Child links: TST003*

