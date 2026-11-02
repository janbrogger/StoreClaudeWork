### Table of Contents

    * 1.1 Automatic archive of every LLM session (REQ001)
    * 1.2 Requirements traceability chain (REQ002)
    * 1.3 Reproducible development environment (REQ003)
    * 2.1 Sources tree: traceable reports and machine-readable data (REQ004)
    * 2.2 Pivotal chart: Norwegian grade inflation versus IB stability (REQ005)

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

## 2.1 Sources tree: traceable reports and machine-readable data _(REQ004)_ {#REQ004}

Every evidence folder under `sources/` shall contain a `REPORT.md` that ends with a `Sources` section and a `TO-FETCH.md`; every `*.csv` under `sources/` shall be UTF-8, comma-separated, with a header row that includes the columns `source_url` and `note`, and shall parse without error. Numbers that could not be traced to a primary document shall be marked as such in the `note` column or in the report rather than omitted silently.

*Parent links: NEED003*

*Child links: DES004*

## 2.2 Pivotal chart: Norwegian grade inflation versus IB stability _(REQ005)_ {#REQ005}

The software shall produce, from the CSV files under `sources/` alone, a chart that shows Norwegian grade means over time together with IB Diploma mean total points over time (and PISA for Norway where available), as a PNG and an SVG under `charts/`, with the data source of every series named in the chart, and shall fail with a clear message if a required series is missing.

*Parent links: NEED003*

*Child links: DES005*

