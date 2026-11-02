"""TST005 - Chart generation (REQ005, DES005): charts/make_chart.py writes the PNG and SVG
from the CSV sources, and exits non-zero naming a missing required input."""
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "charts" / "make_chart.py"
REQUIRED = [ROOT / "sources" / "norway-grades" / "grunnskolepoeng.csv",
            ROOT / "sources" / "ib-statistics" / "ib_session_stats.csv",
            ROOT / "sources" / "pisa" / "pisa_country_year.csv"]
PY = ROOT / ".venv" / "bin" / "python"
PYTHON = str(PY) if PY.exists() else sys.executable


def run(args, cwd=ROOT):
    return subprocess.run([PYTHON, str(SCRIPT), *args], cwd=cwd, capture_output=True, text=True)


def test_chart_is_written(tmp_path):
    missing = [p for p in REQUIRED if not p.is_file()]
    if missing:
        pytest.skip(f"source CSVs not present yet: {missing}")
    res = run(["--out", str(tmp_path)])
    assert res.returncode == 0, res.stdout + res.stderr
    for name in ("grade_inflation_vs_ib", "grade_inflation_vs_ib_indexed"):
        assert (tmp_path / f"{name}.png").stat().st_size > 1000
        assert (tmp_path / f"{name}.svg").stat().st_size > 1000


def test_missing_input_is_named(tmp_path):
    copy = tmp_path / "repo"
    shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(".venv", ".git", "llm-logs", "__pycache__", ".pytest_cache"))
    target = copy / "sources" / "ib-statistics" / "ib_session_stats.csv"
    if target.exists():
        target.unlink()
    res = subprocess.run([PYTHON, str(copy / "charts" / "make_chart.py"), "--out", str(tmp_path / "out")],
                         cwd=copy, capture_output=True, text=True)
    assert res.returncode != 0
    assert "sources/" in res.stderr and ".csv" in res.stderr, res.stderr
