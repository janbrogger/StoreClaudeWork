#!/bin/bash
# SessionStart hook for Claude Code on the web: build the gitignored .venv
# (Doorstop, pytest) in a fresh cloud container so that `doorstop` and
# `pytest` work from the first prompt. Local sessions are left alone - run
# ./setup.sh once yourself. Add project-specific setup below.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
    exit 0
fi

cd "$CLAUDE_PROJECT_DIR"
./setup.sh >/dev/null
echo "session-start: .venv ready ($(.venv/bin/doorstop --version 2>/dev/null | head -1))"
