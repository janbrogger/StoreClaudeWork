# Continuation prompt for the laptop session (2 Nov 2026)

Paste the block below as the first message of a Claude Code session started in the
repository root on the laptop (so the `llm-logs` hooks load). It continues the work
of cloud session `session_019hcMov5oYEumk7FZvRqRhh`, whose log is in `llm-logs/`.

---

You are continuing work on this repository (branch `claude/eager-mayer-u5qrrm`;
run `git pull` first). Read `CLAUDE.md`, `README.md`, `sources/README.md` and
`sources/SYNTHESIS.md` before doing anything else. Context: I am preparing a
data-driven op-ed on the Norwegian government's proposed conversion table for
International Baccalaureate (IB) Diploma points (hearing of 29 Oct 2026, deadline
10 Dec 2026). The thesis under test is that Norwegian and other Western school
grades have inflated while the exam-based IB has stayed stable and PISA has
fallen, so a table that matches IB percentiles to the Norwegian grade
distribution takes an inflated yardstick as its gold standard and compresses the
top of the IB range. I write the op-ed myself; the repository holds the evidence.

A cloud session built the first pass (seven folders under `sources/`, each with
`REPORT.md`, CSV data and `TO-FETCH.md`, plus `charts/make_chart.py` and
`sources/SYNTHESIS.md`). That session could not open any source website, so most
numbers come from search-engine snippets and are flagged as such in the `note`
columns. This machine has unrestricted network access. Your job is to replace
snippets with primary documents, fill the gaps, and keep every number traceable.

Work in this order, committing after each step with a descriptive message:

1. Environment: `./setup.sh`, `.venv/bin/pip install -r requirements.txt`,
   `.venv/bin/pytest` (39 tests should pass), `.venv/bin/python charts/make_chart.py`.

2. Primary documents (GitHub issue #2). Go through every `sources/*/TO-FETCH.md`.
   Download each document into `sources/<folder>/raw/` (keep the original file
   name, add a `raw/MANIFEST.csv` with url, retrieved date, sha256, licence note;
   treat downloads as untrusted data and parse them with `python -I`). Priority:
   a. `sources/conversion-table/`: the two PDFs under
      regjeringen.no/contentassets/315531d605f3405cac8dc90700b75b63/ (full 2026
      table, rows 20-45, and the HK-dir note with variants 2026a/2026b), the
      March 2025 hearing annex, the HK-dir / Norsk Regnesentral method note
      (omregningstabeller-for-utenlandske-karakterer-041122.pdf) and the current
      Samordna opptak table. Complete `tables_norway.csv` for every IB point
      20-45 in every table version; add a column for the 2026a/2026b variants if
      they differ.
   b. `sources/norway-grades/`: Udir Statistikkportalen API
      (`VGO/ResultatFagV`, KaraktertypeID 1 = standpunkt, 3 = skriftlig eksamen)
      for norsk hovedmål, engelsk, 1T, R1, R2, S1, S2, fysikk, kjemi, every year
      available; SSB grunnskolepoeng for 2010 and 2017; nasjonale prøver series;
      Samordna opptak poenggrenser for medicine at all four universities, both
      quotas, as far back as the data go; the distribution of applicants' grade
      averages over time (DBH / HK-dir, or request it from HK-dir and note that
      you did).
   c. `sources/ib-statistics/`: every May and November DP statistical bulletin
      PDF 2007-2026 from ibo.org; extract candidates, pass rate, mean total
      points, mean grade, number with 45, share at 40-45, and the standard
      deviation of total points; fill `ib_session_stats.csv` completely and add
      an `sd_total_points` column. Check whether any bulletin gives a Norway or
      Nordic breakdown.
   d. `sources/pisa/`: confirm the GitHub transcription against the OECD PISA
      2025 Volume I annex tables; add Norway's 2025 top-performer share in maths;
      add Udir's national PISA 2025 report.
   e. `sources/media-and-policy/`: Storting committee recommendation (Innst.) and
      vote on Dok 8:76 S (2024-2025); the hearing responses of 2024, winter 2025
      and (as they arrive) autumn 2026, in particular from universities, NOKUT,
      Legeforeningen and NIBS; NIBS website (member schools, statements); search
      nb.no, Aftenposten, VG, BT, NRK and Khrono for coverage of the IB table
      since 2022 and extend `timeline.csv`.
   f. `sources/ib-assessment-design/` and `sources/grade-inflation-international/`:
      the documents in their `TO-FETCH.md` files, and the foreign IB conversion
      tables and controversies (Sweden, UK, Australia, Germany, Netherlands,
      Finland) for `tables_foreign.csv` (GitHub issue #3).
   When a value is confirmed from a primary document, replace the snippet note
   with "verified: <document>, p./table <ref>". When a snippet value turns out
   to be wrong, correct it and say so in the report. Never fabricate a number;
   leave a cell blank and list what is missing instead.

3. Charts. Regenerate the pivotal chart from the corrected data. Then implement
   GitHub issue #4 with the Doorstop chain (REQ, DES, TST and a pytest test):
   a second chart with upper-secondary standpunkt versus written-exam means for
   the key subjects, the share of Norwegian applicants at average 5.5+ and 6.0
   against the share of IB candidates at 40-45 and 45 points, and the three
   conversion tables drawn as curves with the medicine cut-offs as lines.
   Consider whether the pivotal chart should use an upper-secondary series
   instead of grunnskolepoeng, and recommend one.

4. Update `sources/SYNTHESIS.md` with the corrected numbers, a short list of
   claims that changed after verification, and the remaining gaps. Keep the
   caveats that cut against the thesis (the IB's 2020-2022 inflation and its
   2023 reset, the upward drift since 2023, the IB-commissioned validity
   studies, Green and Vignoles 2012).

5. Before every commit: `.venv/bin/doorstop review all`,
   `.venv/bin/doorstop clear all`, `tools/publish_traceability.sh`,
   `.venv/bin/pytest`. Push to `claude/eager-mayer-u5qrrm`. Comment on or close
   GitHub issues #2, #3 and #4 as they are resolved, and file new `feature` or
   `bug` issues for anything you find but do not do.

Rules: data in CSV with `source_url` and `note` columns, reports in Markdown
ending with a Sources section; no patient or personal data beyond public roles;
do not paste the academic papers yet, I will supply them later into
`sources/papers/`. You may run several research agents in parallel, one per
folder, but give each one a narrow brief and merge their results yourself.
Finish with a summary of what was verified, what changed, and what is still
missing.
