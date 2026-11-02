# IB conversion table: evidence base

Evidence for a data-driven op-ed on the Norwegian conversion table for
International Baccalaureate (IB) Diploma points to Norwegian grade points
(hearing of 29 Oct 2026, deadline 10 Dec 2026). Thesis under test: Norwegian
and other Western school grades have inflated while the exam-based IB Diploma
has stayed stable, and PISA has fallen; the conversion method treats the
inflated Norwegian distribution as the gold standard.

- `sources/SYNTHESIS.md`: the findings in one page, with gaps.
- `sources/<stream>/REPORT.md`, `*.csv`, `TO-FETCH.md`: one folder per
  evidence stream (see `sources/README.md`). Numbers come from primary
  documents where reachable and otherwise from search snippets, flagged as
  such; nothing is fabricated.
- `charts/make_chart.py`: the pivotal chart (Norwegian grades up, IB flat,
  PISA down) from the CSVs alone; outputs `charts/*.png|svg`.

```bash
./setup.sh
.venv/bin/pip install pandas matplotlib
.venv/bin/python charts/make_chart.py
.venv/bin/pytest
```

The repository was created from the
[StoreClaudeWork](https://github.com/janbrogger/StoreClaudeWork) template:
every Claude Code session is archived in `llm-logs/`, and requirements,
design and tests are traced with Doorstop in `docs/traceability/`.

Licence: [Unlicense](LICENSE). Data files keep their sources' licences (noted
in each `REPORT.md`).
