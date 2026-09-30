### Table of Contents

    * 1.1 LLM log integrity (TST001)
    * 1.2 Traceability chain validation (TST002)
    * 1.3 Development environment (TST003)

## 1.1 LLM log integrity _(TST001)_ {#TST001}

`tests/test_llm_logs.py`: every archived session folder is listed in `sessions.csv` and holds `session.json`, `prompts.csv` and `PROMPTS-AND-RESPONSES.md`; `llmlog.py index` runs without error; `.claude/settings.json` registers the four hooks and each hook script exists; `llmlog.py archive` on a synthetic transcript in a temporary copy of the log produces the session files, with the prompt verbatim and the reply included, and skips system-injected turns.

*Parent links: DES001*

## 1.2 Traceability chain validation _(TST002)_ {#TST002}

`tests/test_traceability.py`: `doorstop` validation passes; every active normative REQ links to a NEED and is implemented by a DES; every DES links to a REQ, has text and is covered by a TST; every REQ is covered by a TST through its DES; the committed `published/*.md` equal a fresh publish.

*Parent links: DES002*

## 1.3 Development environment _(TST003)_ {#TST003}

`tests/test_environment.py`: `.venv` is gitignored; `requirements-dev.txt` pins Doorstop; `setup.sh` and the hook scripts are executable; the SessionStart hook calls `setup.sh`. CI (`.github/workflows/tests.yml`) runs `setup.sh` and the whole suite on a fresh clone, which is the end-to-end form of this test.

*Parent links: DES003*

