# Working conventions for this repository

<!-- Template: replace this line with one or two sentences on what this project is for. -->
- **Purpose**: _describe the project here_.

## LLM provenance (automatic)

Every Claude Code session in this repository is archived automatically by
the hooks in `.claude/settings.json` into `llm-logs/<session_id>/`
(transcript, prompts, readable prompts-and-responses) and committed at
session end - see `llm-logs/README.md`. Never delete or hand-edit files
there except the `topic` column of `llm-logs/sessions.csv`; if the hooks
did not run (e.g. the session was started outside this repository's root),
archive by hand: `python3 llm-logs/tools/llmlog.py archive --session-id
<id> --transcript <path>`.

## Requirements, design and tests - steer towards them

This repository keeps a Doorstop traceability chain NEED -> REQ -> DES ->
TST in `docs/traceability/` (see its `README.md`); Doorstop and pytest live
in the gitignored `.venv` created by `./setup.sh`. The chain is only useful
if it grows together with the code, and the user wants you to help with
that actively:

- **Elicit before you build.** When asked to write or change code, help
  the user make explicit *what need it serves*, *what exactly it shall do*
  (testable requirements and acceptance criteria, edge cases, error
  behaviour, limits), *how it will be built* (design choices, alternatives
  rejected) and *how we will know it works* (tests). When a request is
  ambiguous, ask a few focused questions rather than guessing; when it is
  clear enough, state your assumptions as draft requirements and proceed.
  Do this briefly and in passing - a nudge, not a questionnaire - and do
  not block small or urgent tasks on it.
- **Add the chain with substantial code.** Whenever you write a
  substantial block of code (a new feature, module, command, public
  function, file format, or a bug fix that changes behaviour - roughly
  anything a reviewer would want specified), also add or update, in the
  same change:
  1. a **REQ** item ("The software shall ..."; one testable statement),
     linked to an existing NEED, or to a new NEED if none fits;
  2. a **DES** item linked to the REQ, naming the files/functions that
     implement it, the key decisions and known limits;
  3. a **TST** item linked to the DES, naming the automated test and its
     pass criterion - and write that test (pytest), with the TST id at the
     start of its docstring;
  then run `.venv/bin/doorstop review all`, `.venv/bin/doorstop clear all`,
  `tools/publish_traceability.sh` and `.venv/bin/pytest` before committing.
  Update existing items instead of adding duplicates when you change
  behaviour that is already specified.
- **Skip it for trivia** (typos, formatting, pure refactors, throw-away
  experiments) and say in one line that you did. If the user declines the
  chain for a piece of work, respect that and do not ask again in the same
  session; mention the gap in your summary.

## GitHub issues

If the repository is hosted on GitHub (`git remote get-url origin`), use
its issue tracker as the backlog, without being asked:

- **Known bugs**: when you find a bug that is not fixed in the current
  change (found while reading code, reported by the user, a failing test
  outside the task), create an issue labelled `bug` with what happens,
  what should happen, how to reproduce, and the file/line.
- **Feature ideas**: when a possible feature, improvement or follow-up
  comes up in the chat (from the user or from you) and is not being
  implemented now, create an issue labelled `feature` (create the label if
  the repository does not have it).
- File issues only in this repository's own `origin` - never in an
  upstream, a dependency's or a tool vendor's repository.
- Search the open issues first and comment on an existing one instead of
  filing a duplicate. Mention related REQ/DES/TST ids and the session id
  (see `llm-logs/`) in the body. Never put secrets or personal data in an
  issue.
- Use whichever GitHub access you have (the GitHub MCP tools or the `gh`
  CLI). If you have none, list the issues you would have filed in your
  reply instead. Always tell the user which issues you created, with links,
  and reference them in commits that fix them (`Fixes #12`).

## Other conventions

- **Python**: tooling runs from `.venv` (`./setup.sh`); pin new dev
  dependencies in `requirements-dev.txt`, runtime ones in `requirements.txt`.
- **Tests**: `pytest` (`tests/`); CI runs `./setup.sh` and `pytest` on every
  push (`.github/workflows/tests.yml`). Tests that need private data must
  skip, not fail, when it is absent.
- **Licence**: Unlicense.
