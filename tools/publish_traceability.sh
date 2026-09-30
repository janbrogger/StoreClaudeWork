#!/usr/bin/env bash
# Regenerate the committed Markdown copies of the Doorstop documents
# (docs/traceability/published/*.md). tests/test_traceability.py fails when
# they are stale.
set -euo pipefail
cd "$(dirname "$0")/.."
DOORSTOP=.venv/bin/doorstop
"$DOORSTOP"
for doc in NEED REQ DES TST; do
    "$DOORSTOP" publish "$doc" "docs/traceability/published/$doc.md" >/dev/null
done
echo "published: docs/traceability/published/{NEED,REQ,DES,TST}.md"
