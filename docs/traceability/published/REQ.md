### Table of Contents

    * 1.1 Automatic archive of every LLM session (REQ001)
    * 1.2 Requirements traceability chain (REQ002)
    * 1.3 Reproducible development environment (REQ003)

## 1.1 Automatic archive of every LLM session _(REQ001)_ {#REQ001}

Every Claude Code session run in the repository shall be archived without manual action into `llm-logs/<session_id>/`: the full transcript, every human prompt verbatim, and a human-readable file of prompts and the assistant's replies. Every session shall be indexed in `llm-logs/sessions.csv`, every prompt shall be logged in `llm-logs/prompt-log.csv` when it is submitted, and at session end the archive shall be committed and pushed in a commit that contains nothing but `llm-logs/`. A failure of the archiving shall never block the session.

*Parent links: NEED001*

*Child links: DES001*

## 1.2 Requirements traceability chain _(REQ002)_ {#REQ002}

Intended behaviour shall be documented as a Doorstop chain NEED -> REQ -> DES -> TST under `docs/traceability/`. Every active normative REQ shall link to a NEED and be implemented by a DES item, every DES shall be verified by a TST item, Doorstop validation shall pass, and committed Markdown copies of the four documents shall match a fresh publish. The test suite shall check all of this automatically.

*Parent links: NEED002*

*Child links: DES002*

## 1.3 Reproducible development environment _(REQ003)_ {#REQ003}

A single command (`./setup.sh`) on a fresh clone shall create a gitignored Python virtual environment `.venv` holding the pinned development tools (Doorstop, pytest), validate the traceability tree and rebuild the LLM log index. Claude Code on the web shall run it automatically at session start, and continuous integration shall run it and the test suite on every push.

*Parent links: NEED001, NEED002*

*Child links: DES003*

