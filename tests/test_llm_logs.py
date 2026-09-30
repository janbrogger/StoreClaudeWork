"""TST001 - LLM log integrity (REQ001, DES001)."""
import csv
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / "llm-logs"
HOOKS = {"SessionStart": "llmlog-session-start.sh", "UserPromptSubmit": "llmlog-prompt.sh",
         "Stop": "llmlog-archive.sh", "SessionEnd": "llmlog-commit.sh"}


def session_dirs():
    return {p.name for p in LOG.iterdir()
            if p.is_dir() and (p / "transcript.jsonl").exists()}


def test_every_session_folder_is_indexed_and_complete():
    folders = session_dirs()
    if not folders:
        pytest.skip("no archived sessions yet")
    with open(LOG / "sessions.csv", encoding="utf-8", newline="") as f:
        indexed = {r["session_id"] for r in csv.DictReader(f)}
    assert folders <= indexed, f"folders not in sessions.csv: {folders - indexed}"
    for sid in folders:
        for name in ("session.json", "prompts.csv", "PROMPTS-AND-RESPONSES.md"):
            assert (LOG / sid / name).exists(), f"{sid}/{name} missing"


def test_index_regenerates_cleanly():
    res = subprocess.run([sys.executable, str(LOG / "tools" / "llmlog.py"), "index"],
                         cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0 and "llmlog:" not in res.stderr, res.stderr
    assert (LOG / "SESSIONS.md").exists()


def test_hooks_are_registered():
    settings = json.loads((ROOT / ".claude" / "settings.json").read_text(encoding="utf-8"))
    for event, script in HOOKS.items():
        commands = [h["command"] for group in settings["hooks"][event] for h in group["hooks"]]
        assert any(script in c for c in commands), f"{event} does not run {script}"
        assert (ROOT / ".claude" / "hooks" / script).is_file()


def test_archive_of_a_synthetic_session(tmp_path):
    """Run `archive` on a made-up transcript in a throw-away copy of llm-logs/."""
    repo = tmp_path / "repo"
    shutil.copytree(LOG / "tools", repo / "llm-logs" / "tools")
    subprocess.run(["git", "init", "-q", str(repo)], check=True)
    sid = "00000000-test-4000-8000-000000000000"
    lines = [
        {"type": "user", "timestamp": "2026-01-01T10:00:00Z", "gitBranch": "main", "version": "9.9",
         "message": {"role": "user", "content": "Write a function that adds two numbers."}},
        {"type": "assistant", "timestamp": "2026-01-01T10:00:05Z",
         "message": {"model": "test-model", "content": [
             {"type": "tool_use", "name": "Write", "input": {}},
             {"type": "text", "text": "Added `add()` with REQ, DES and TST items."}]}},
        {"type": "user", "timestamp": "2026-01-01T10:00:06Z",
         "message": {"role": "user", "content": "<system-reminder>not a human prompt</system-reminder>"}},
    ]
    transcript = tmp_path / f"{sid}.jsonl"
    transcript.write_text("\n".join(json.dumps(l) for l in lines) + "\n", encoding="utf-8")
    res = subprocess.run([sys.executable, str(repo / "llm-logs" / "tools" / "llmlog.py"), "archive",
                          "--session-id", sid, "--transcript", str(transcript)],
                         cwd=tmp_path, capture_output=True, text=True)
    assert res.returncode == 0 and "llmlog:" not in res.stderr, res.stderr
    sdir = repo / "llm-logs" / sid
    assert (sdir / "transcript.jsonl").read_bytes() == transcript.read_bytes()
    with open(sdir / "prompts.csv", encoding="utf-8", newline="") as f:
        prompts = list(csv.DictReader(f))
    assert [p["prompt_text"] for p in prompts] == ["Write a function that adds two numbers."]
    md = (sdir / "PROMPTS-AND-RESPONSES.md").read_text(encoding="utf-8")
    assert "Added `add()` with REQ, DES and TST items." in md
    meta = json.loads((sdir / "session.json").read_text(encoding="utf-8"))
    assert meta["models"] == ["test-model"] and meta["tool_use_counts"] == {"Write": 1}
    with open(repo / "llm-logs" / "sessions.csv", encoding="utf-8", newline="") as f:
        assert [r["session_id"] for r in csv.DictReader(f)] == [sid]
    assert (repo / "llm-logs" / "SESSIONS.md").exists()
