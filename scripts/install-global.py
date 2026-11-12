#!/usr/bin/env python3
"""Install this repository's Claude Code workflow into ~/.claude.

The global copy enforces in projects that do not contain this repository, so it
cannot be a link (see tests/test_global_install_in_sync.py). This mirrors
`workflow/` into `~/.claude/workflow/`, removing files the repository no longer
has, copies the role agents, and writes the global hook variant. It prints the
plan and changes nothing unless `--apply` is given. The global `CLAUDE.md` and
`settings.json` are not touched.

The hook fails closed, so a half-applied install can block every Bash call.
Apply therefore stages every new file first, swaps them in only after all
staged, and finishes by running the installed hook on a harmless command.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = Path.home() / ".claude"
SKIP = "__pycache__"  # tests/test_global_install_in_sync.py excludes the same
AGENTS = ("explorer.md", "implementer.md", "reviewer.md")
STAGED = ".install-tmp"
REPO_ROOT_LINE = "ROOT = Path(__file__).resolve().parents[2]"
GLOBAL_ROOT_LINE = "ROOT = Path(__file__).resolve().parents[1]"
HOOK_NOTE = """Global install variant of my-ai-workflows' .claude/hooks/pre_tool_use.py:
ROOT is ~/.claude (this file lives at ~/.claude/hooks/pre_tool_use.py, one
level shallower than the repo's <repo>/.claude/hooks/ layout), so it always
enforces against ~/.claude/workflow regardless of the current project.

"""


def _files(root: Path) -> set[str]:
    """Relative posix paths, compared case-sensitively like the drift test."""
    if not root.is_dir():
        return set()
    return {
        p.relative_to(root).as_posix()
        for p in root.rglob("*")
        if p.is_file() and SKIP not in p.parts
    }


def _same(a: Path, b: Path) -> bool:
    return b.exists() and a.read_bytes().replace(
        b"\r\n", b"\n"
    ) == b.read_bytes().replace(b"\r\n", b"\n")


def _global_hook(hook: Path) -> str:
    text = (ROOT / ".claude" / "hooks" / "pre_tool_use.py").read_text(encoding="utf-8")
    if text.count(REPO_ROOT_LINE) != 1:
        raise SystemExit("repo hook: ROOT line not found exactly once")
    opening, closing = text.find('"""'), text.find('"""', text.find('"""') + 3)
    summary_end = text.index("\n\n") + 2  # after the docstring's summary line
    if not opening < summary_end < closing:
        raise SystemExit(
            "repo hook: docstring layout changed; cannot place the global note"
        )
    text = text[:summary_end] + HOOK_NOTE + text[summary_end:]
    text = text.replace(REPO_ROOT_LINE, GLOBAL_ROOT_LINE)
    compile(text, str(hook), "exec")  # a SyntaxError here stops before any write
    return text


def plan() -> list[tuple[str, Path, Path | str | None]]:
    """Return (action, destination, source path or hook text) for every change."""
    steps: list[tuple[str, Path, Path | str | None]] = []
    src, dst = ROOT / "workflow", TARGET / "workflow"
    repo, installed = _files(src), _files(dst)
    for rel in sorted(repo):
        if not _same(src / rel, dst / rel):
            steps.append(
                ("add" if rel not in installed else "update", dst / rel, src / rel)
            )
    for rel in sorted(installed - repo):
        steps.append(("remove", dst / rel, None))
    for name in AGENTS:
        a, b = ROOT / ".claude" / "agents" / name, TARGET / "agents" / name
        if not _same(a, b):
            steps.append(("update" if b.exists() else "add", b, a))
    hook = TARGET / "hooks" / "pre_tool_use.py"
    text = _global_hook(hook)
    if (
        not hook.exists()
        or hook.read_text(encoding="utf-8").replace("\r\n", "\n") != text
    ):
        steps.append(("update" if hook.exists() else "add", hook, text))
    return steps


def _uncommitted() -> str:
    paths = ["workflow", ".claude/agents", ".claude/hooks"]
    result = subprocess.run(
        ["git", "status", "--porcelain", "--", *paths],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def _smoke_test() -> str | None:
    """Run the installed hook on a harmless Bash call; return an error or None."""
    event = json.dumps({"tool_name": "Bash", "tool_input": {"command": "echo ok"}})
    result = subprocess.run(
        [sys.executable, str(TARGET / "hooks" / "pre_tool_use.py")],
        input=event,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return f"exit {result.returncode}: {(result.stderr or result.stdout).strip()}"
    return None


def apply(steps: list[tuple[str, Path, Path | str | None]]) -> None:
    writes = [(dest, source) for action, dest, source in steps if action != "remove"]
    staged = []
    try:
        for dest, source in writes:
            tmp = dest.with_name(dest.name + STAGED)
            tmp.parent.mkdir(parents=True, exist_ok=True)
            if isinstance(source, Path):
                shutil.copy2(source, tmp)
            else:
                tmp.write_text(source, encoding="utf-8", newline="\n")
            staged.append((tmp, dest))
    except OSError as error:
        for tmp, _ in staged:
            tmp.unlink(missing_ok=True)
        raise SystemExit(f"Staging failed, nothing installed: {error}")
    for tmp, dest in staged:
        os.replace(tmp, dest)
    for action, dest, _ in steps:
        if action == "remove":
            dest.unlink()
            parent = dest.parent
            while parent != TARGET / "workflow" and not any(parent.iterdir()):
                parent.rmdir()
                parent = parent.parent


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write the changes (default: show the plan only)",
    )
    args = parser.parse_args()
    dirty = _uncommitted()
    if dirty:
        print("Warning: installing uncommitted repository changes:\n" + dirty + "\n")
    steps = plan()
    for action, dest, _ in steps:
        print(f"{action:7} {dest}")
    if not steps:
        print(f"{TARGET} is already in sync with {ROOT}")
        return 0
    if not args.apply:
        print(f"\n{len(steps)} change(s) planned. Re-run with --apply to write them.")
        return 0
    apply(steps)
    print(f"\nApplied {len(steps)} change(s).")
    error = _smoke_test()
    if error:
        print(f"SMOKE TEST FAILED, the global hook may block Bash: {error}")
        return 1
    print("Smoke test passed: the installed hook allows a harmless Bash command.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
