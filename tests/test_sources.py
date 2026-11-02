"""TST004 - Sources tree integrity (REQ004, DES004): every evidence folder has a
REPORT.md ending in a Sources section and a TO-FETCH.md; every CSV parses and
carries source_url and note columns."""
import csv
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"
SKIP_FOLDERS = {"papers"}


def evidence_folders():
    if not SOURCES.is_dir():
        return []
    out = []
    for d in sorted(SOURCES.iterdir()):
        if d.is_dir() and d.name not in SKIP_FOLDERS and any(p.is_file() for p in d.rglob("*")):
            out.append(d)
    return out


def csv_files():
    return sorted(SOURCES.rglob("*.csv")) if SOURCES.is_dir() else []


@pytest.mark.parametrize("folder", evidence_folders(), ids=lambda d: d.name)
def test_folder_has_report_and_to_fetch(folder):
    report = folder / "REPORT.md"
    assert report.is_file(), f"{folder.name}/REPORT.md missing"
    assert (folder / "TO-FETCH.md").is_file(), f"{folder.name}/TO-FETCH.md missing"
    headings = re.findall(r"^#+\s+(.+?)\s*$", report.read_text(encoding="utf-8"), flags=re.M)
    assert headings, f"{folder.name}/REPORT.md has no headings"
    assert headings[-1].strip().lower().startswith("sources"), (
        f"{folder.name}/REPORT.md must end with a 'Sources' section, last heading is {headings[-1]!r}")


@pytest.mark.parametrize("path", csv_files(), ids=lambda p: str(p.relative_to(SOURCES)))
def test_csv_parses_with_provenance_columns(path):
    with path.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.reader(fh))
    assert rows, f"{path} is empty"
    header = [h.strip() for h in rows[0]]
    assert "source_url" in header and "note" in header, f"{path}: header lacks source_url/note: {header}"
    for i, row in enumerate(rows[1:], start=2):
        assert len(row) == len(header), f"{path}:{i} has {len(row)} fields, header has {len(header)}"
