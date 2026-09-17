"""Fail when the global install has drifted from this repository.

`~/.claude/workflow/` is a standalone copy on purpose: it enforces in projects
that do not contain this repository, so it cannot be a link to it. The cost is
that the two can diverge silently, and the global copy is the one guarding all
other work. This detects that divergence rather than preventing it.

The two hooks legitimately differ in module docstring and in ROOT (the global
lives one directory shallower), so those lines are excluded and the remaining
logic is compared.
"""
from __future__ import annotations

from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
GLOBAL_ROOT = Path.home() / ".claude"

SHARED = (
    "workflow/enforcement/core.py",
    "workflow/routing/triggers.yaml",
    "workflow/bin/scan-triggers",
    "workflow/bin/enforce-operation",
)

needs_global_install = pytest.mark.skipif(
    not (GLOBAL_ROOT / "workflow").is_dir(),
    reason="no global install at ~/.claude/workflow",
)


def _normalised(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def _hook_logic(path: Path) -> str:
    """Hook text without its docstring or its ROOT line."""
    lines = _normalised(path).splitlines()
    start = next((i for i, line in enumerate(lines) if line.startswith("from __future__")), 0)
    return "\n".join(line for line in lines[start:] if not line.startswith("ROOT = "))


@needs_global_install
@pytest.mark.parametrize("relative", SHARED)
def test_shared_enforcement_file_matches_global_install(relative: str) -> None:
    mirrored = GLOBAL_ROOT / relative
    assert mirrored.exists(), f"{relative} is missing from the global install"
    assert _normalised(ROOT / relative) == _normalised(mirrored), (
        f"{relative} differs between this repo and {mirrored}. "
        "The global copy enforces in every other project; re-sync it."
    )


@needs_global_install
def test_hook_logic_matches_global_install() -> None:
    mirrored = GLOBAL_ROOT / "hooks" / "pre_tool_use.py"
    assert mirrored.exists(), "global pre_tool_use.py is missing"
    assert _hook_logic(ROOT / ".claude" / "hooks" / "pre_tool_use.py") == _hook_logic(mirrored), (
        "Hook logic differs between this repo and the global install. "
        "Editing one and not the other leaves the global guard on stale rules."
    )
