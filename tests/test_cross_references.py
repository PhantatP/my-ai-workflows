"""Fail when a document references a repository path that does not exist.

Prose drifts from the tree silently: a deleted directory can survive in a
sentence that a path-string grep never finds. This checks the path-shaped
references only; a prose mention with no path in it ("the archived V1
definitions") is still invisible here.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "__pycache__", "node_modules", "graphify-out", ".pytest_cache", ".workflow"}

# Paths that are correctly absent. Each needs a reason.
KNOWN_ABSENT = {
    # The v2.4 phase protocols exist to instruct that this file is NOT created.
    "workflow/core/interaction.md",
}

# Skills are portable methodologies; these name shapes to look for in whatever
# project the skill is applied to, not paths in this repository.
ILLUSTRATIVE = {
    "test/",
    "src/test/",
    "__init__.py",
}

LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
CODE = re.compile(r"`([^`\n]+)`")
PATH_SUFFIX = re.compile(r"\.(md|py|ya?ml|json|sh|html|txt|toml)$")


def _references() -> list[tuple[str, int, str]]:
    found = []
    for document in sorted(ROOT.rglob("*.md")):
        relative = document.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in relative.parts):
            continue
        source = relative.as_posix()
        for lineno, line in enumerate(document.read_text(encoding="utf-8").splitlines(), 1):
            for match in LINK.finditer(line):
                found.append((source, lineno, match.group(1)))
            for match in CODE.finditer(line):
                # A backticked token may carry arguments: `bin/scan-triggers --platform codex`.
                token = match.group(1).split()[0] if match.group(1).split() else ""
                if "/" in token or PATH_SUFFIX.search(token):
                    found.append((source, lineno, token))
    return found


def _is_checkable(target: str) -> bool:
    if not target or target.startswith(("http", "#", "mailto:", "~", "/")):
        return False
    # Globs, placeholders like <repo>, and shell variables are not real paths.
    if any(character in target for character in "*<>$:"):
        return False
    # Operational evidence is generated at runtime and gitignored.
    if target.startswith(".workflow/") or "/.workflow/" in target:
        return False
    if target in ILLUSTRATIVE:
        return False
    return target.split("#")[0].rstrip("/") not in KNOWN_ABSENT


def _resolves(source: str, target: str) -> bool:
    cleaned = target.split("#")[0].rstrip("/")
    if not cleaned:
        return True
    # Documents here address each other both file-relative and repo-relative.
    return ((ROOT / source).parent / cleaned).exists() or (ROOT / cleaned).exists()


def test_documented_paths_exist() -> None:
    missing = [
        f"{source}:{lineno} -> {target}"
        for source, lineno, target in _references()
        if _is_checkable(target) and not _resolves(source, target)
    ]
    assert not missing, "Documented paths that do not exist:\n" + "\n".join(missing)


def test_known_absent_entries_are_still_absent() -> None:
    """An allowlist entry that now exists is stale and hides real breakage."""
    resurrected = [path for path in KNOWN_ABSENT if (ROOT / path).exists()]
    assert not resurrected, f"KNOWN_ABSENT entries that now exist: {resurrected}"
