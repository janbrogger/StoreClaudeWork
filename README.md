# StoreClaudeWork - template for LLM-traceable repositories

A GitHub **template repository**. A repository created from it ("Use this
template" on GitHub) gets, with no further setup:

1. **Automatic LLM provenance.** Every Claude Code session is archived into
   `llm-logs/<session_id>/` - full transcript, every prompt verbatim, a
   readable `PROMPTS-AND-RESPONSES.md`, model and tool metadata - indexed in
   `llm-logs/sessions.csv` and committed (only `llm-logs/`) at session end.
   Implemented as Claude Code hooks around one dependency-free Python script;
   see [`llm-logs/README.md`](llm-logs/README.md).
2. **A requirements traceability chain.** [Doorstop](https://github.com/doorstop-dev/doorstop)
   documents NEED -> REQ -> DES -> TST in [`docs/traceability/`](docs/traceability/README.md),
   validated by the test suite, with Doorstop installed in a gitignored `.venv`.
3. **Agent instructions** in [`CLAUDE.md`](CLAUDE.md) that make Claude steer
   towards eliciting requirements, design and tests, add REQ/DES/TST items
   (and the test) along with substantial code, and file GitHub issues for
   known bugs (`bug`) and feature ideas (`feature`) that come up in a chat.
4. **CI**: `.github/workflows/tests.yml` runs `./setup.sh` and `pytest` on
   every push.

The mechanism was first built in
[CwellEEGRead](https://github.com/janbrogger/CwellEEGRead) and extracted here.

## Starting a new project from the template

1. On GitHub: **Use this template -> Create a new repository**, then clone it.
2. `./setup.sh` (Python 3.9+; creates `.venv` with Doorstop and pytest,
   validates the tree, rebuilds the log index). Claude Code on the web runs
   it automatically at session start.
3. Edit the *Purpose* line at the top of `CLAUDE.md` and this README.
4. Add your project's first needs: `.venv/bin/doorstop add NEED`, then
   requirements, design and tests - or just ask Claude to help elicit them.
5. Start Claude Code **in the repository root** so that its hooks load
   (check with `/hooks`).

The template's own session logs come along in `llm-logs/`; they are the
provenance of the scaffolding. Delete them in the first commit of the new
repository if you prefer a clean log. The seed Doorstop items
(NEED001-002, REQ001-003, ...) describe the template's machinery and stay
valid in every derived repository.

## Layout

```
CLAUDE.md                     instructions for Claude Code (read every session)
.claude/settings.json         hook registration (committed)
.claude/hooks/                llmlog-*.sh wrappers, session-start.sh (runs setup.sh on the web)
llm-logs/                     archived sessions + tools/llmlog.py
docs/traceability/            Doorstop: needs/ requirements/ design/ tests/ published/
docs/research/prior-art.md    survey of similar tools and papers (2026-09)
tests/                        pytest: traceability, LLM log and environment checks
tools/publish_traceability.sh regenerate docs/traceability/published/*.md
setup.sh, requirements-dev.txt  gitignored .venv with Doorstop 3.2 + pytest
```

## Requirements

Python 3 and git. The logging hooks need nothing else; Doorstop and pytest
are installed into `.venv` by `./setup.sh`.

## Licence

[Unlicense](LICENSE) - public domain.
