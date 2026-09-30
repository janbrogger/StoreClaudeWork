# Traceability (Doorstop)

Four [Doorstop](https://github.com/doorstop-dev/doorstop) documents form the chain:

| Prefix | Folder | Content | Parent |
|---|---|---|---|
| `NEED` | `needs/` | stakeholder needs and project goals ("who needs what, and why") | - |
| `REQ` | `requirements/` | requirements: one testable "the software shall ..." statement each | NEED |
| `DES` | `design/` | design: how a requirement is implemented (files, functions, algorithms, decisions, limits) | REQ |
| `TST` | `tests/` | test specifications: which automated test proves the design, and the pass criterion | DES |

Rules (REQ002): every active normative REQ links to at least one NEED and
is implemented by a DES item; every DES is covered by at least one TST;
`doorstop` validation passes; `published/*.md` are up to date.
`tests/test_traceability.py` checks all of this.

The items shipped with the template (NEED001-002, REQ001-003, DES001-003,
TST001-003) describe the template's own machinery (LLM session archive,
this chain, the dev environment). Keep them - they are true of every
repository made from the template - and number your project's items after
them.

Commands (from the repository root, after `./setup.sh`; activate with
`source .venv/bin/activate` or prefix `.venv/bin/`):

```bash
doorstop                              # validate the whole tree
doorstop add REQ                      # create the next REQ item (edit the YAML file it prints)
doorstop link REQ004 NEED002          # link child -> parent
doorstop link DES004 REQ004
doorstop link TST004 DES004
doorstop review all                   # clear "unreviewed" after edits
doorstop clear all                    # clear "suspect link" after parent edits
tools/publish_traceability.sh         # regenerate published/{NEED,REQ,DES,TST}.md (committed)
doorstop publish all published/html   # browsable HTML with traceability matrix (gitignored)
```

Item files are YAML (`REQ001.yml` ...). `header` is the title, `text` the
normative statement, `links` the parent items, `level` the outline
position. Non-normative explanatory items can be added with
`normative: false`. Name the item in the code as well: a test's docstring
starts with its TST id, and a module or function implementing a DES item
mentions the DES id, so a reader can follow the chain in both directions.
