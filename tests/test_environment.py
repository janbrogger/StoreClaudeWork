"""TST003 - Development environment (REQ003, DES003)."""
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_venv_is_gitignored():
    res = subprocess.run(["git", "check-ignore", "-q", ".venv"], cwd=ROOT)
    assert res.returncode == 0, ".venv is not gitignored"


def test_doorstop_is_pinned():
    lines = (ROOT / "requirements-dev.txt").read_text(encoding="utf-8").splitlines()
    assert any(l.split("#")[0].strip().startswith("doorstop==") for l in lines)


def test_scripts_are_executable():
    scripts = [ROOT / "setup.sh", ROOT / "tools" / "publish_traceability.sh",
               ROOT / "llm-logs" / "tools" / "llmlog.py", *(ROOT / ".claude" / "hooks").glob("*.sh")]
    for p in scripts:
        assert os.access(p, os.X_OK), f"{p.relative_to(ROOT)} is not executable"


def test_session_start_hook_runs_setup():
    assert "./setup.sh" in (ROOT / ".claude" / "hooks" / "session-start.sh").read_text(encoding="utf-8")


def test_ci_runs_setup_and_pytest():
    wf = (ROOT / ".github" / "workflows" / "tests.yml").read_text(encoding="utf-8")
    assert "./setup.sh" in wf and "pytest" in wf
