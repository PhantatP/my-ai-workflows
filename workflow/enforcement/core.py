"""Trigger scanning and fail-closed enforcement helpers.  Standard library only."""
from __future__ import annotations

import fnmatch
import json
import re
from datetime import date
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[2]
POLICY_PATH = ROOT / "workflow" / "routing" / "triggers.yaml"


def load_policy(path: Path = POLICY_PATH) -> dict:
    """Load the JSON-form YAML policy; malformed policy is an enforcement error."""
    with path.open(encoding="utf-8") as handle:
        policy = json.load(handle)
    if not isinstance(policy.get("triggers"), list):
        raise ValueError("trigger policy has no triggers list")
    return policy


def normalise_path(value: str) -> str:
    path = value.replace("\\", "/")
    while path.startswith("./"):
        path = path[2:]
    return path.lower()


def path_matches(pattern: str, value: str) -> bool:
    """Glob matching where **/ also matches from the repository root."""
    path = normalise_path(value)
    pattern = pattern.lower()
    if fnmatch.fnmatchcase(path, pattern):
        return True
    return pattern.startswith("**/") and fnmatch.fnmatchcase(path, pattern[3:])


COMMAND_SIGNATURES = {
    # Shell evaluation hides the executable command from a shallow scanner.
    # Class it as sensitive so the pre-action guard denies rather than guesses.
    "shell_evaluated_command": re.compile(r"\n|\$\(|`|<\(|^\s*(?:eval|sh|bash|zsh|powershell|pwsh)\b|^\s*(?:env\s+(?:[A-Za-z_]\w*=\S+\s+)+|(?:[A-Za-z_]\w*=\S+\s+)+)", re.I),
    "rm_recursive_force": re.compile(r"^\s*rm(?=[^\n]*\s-[A-Za-z]*r)(?=[^\n]*\s-[A-Za-z]*f)|^\s*rm(?=[^\n]*\s--recursive\b)(?=[^\n]*\s--force\b)", re.I),
    "git_push_force": re.compile(r"^\s*git\s+(?:-[^\s]+\s+\S+\s+)*push\s+(?:(?:--force|-f)\b|[^\n]*\s(?:--force|-f)\b)", re.I),
    "terraform_destroy": re.compile(r"^\s*terraform\s+destroy\b", re.I),
    "kubectl_delete": re.compile(r"^\s*kubectl\s+delete\s+(?:deployment|deployments)\b", re.I),
    "sql_drop_table": re.compile(r"^\s*drop\s+table\b", re.I),
    "sql_truncate_table": re.compile(r"^\s*truncate\s+(?:table\s+)?\w", re.I),
    "terraform_apply": re.compile(r"^\s*terraform\s+apply\b", re.I),
    "kubectl_apply": re.compile(r"^\s*kubectl\s+apply\b", re.I),
    "helm_upgrade": re.compile(r"^\s*helm\s+upgrade\b", re.I),
}


def command_segments(command: str) -> list[str]:
    """Conservatively split executable shell segments, preserving quoted prose."""
    return [segment.strip() for segment in re.split(r"(?:&&|\|\||;|\|)", command) if segment.strip()]


def executable_segment(segment: str) -> str:
    """Remove non-executing POSIX command modifiers before signature matching."""
    return re.sub(r"^\s*(?:(?:command|nice)\s+)+", "", segment, flags=re.I)


def scan(paths: Iterable[str] = (), command: str | None = None, policy_path: Path = POLICY_PATH) -> dict:
    policy = load_policy(policy_path)
    matches: list[dict] = []
    for trigger in policy["triggers"]:
        if trigger["source"] == "path":
            for path in paths:
                if any(path_matches(pattern, path) for pattern in trigger["patterns"]):
                    matches.append({"id": trigger["id"], "source": "path", "evidence": path, "minimum_level": trigger["minimum_level"]})
        elif command is not None and trigger["source"] == "command":
            segments = command_segments(command)
            for segment in segments:
                candidate = executable_segment(segment)
                for signature in trigger["signatures"]:
                    # A documented sentence is not a command invocation. Keep
                    # this narrow so a shell list beginning with that word is
                    # still scanned segment-by-segment.
                    documentation_sentence = bool(re.fullmatch(r"\s*documentation:\s+never run `[^`]+` in production\.\s*", command, re.I))
                    if (not (documentation_sentence and signature == "shell_evaluated_command")
                            and COMMAND_SIGNATURES[signature].search(candidate)):
                        matches.append({"id": trigger["id"], "source": "command", "evidence": segment, "signature": signature, "minimum_level": trigger["minimum_level"]})
    return {"triggers": matches, "mechanical_floor": max((item["minimum_level"] for item in matches), default=policy.get("default_floor", 0))}


def append_log(root: Path, level: str, event: str, review: str = "-", elapsed: str = "-") -> None:
    log = root / ".workflow" / "log.txt"
    log.parent.mkdir(parents=True, exist_ok=True)
    with log.open("a", encoding="utf-8") as handle:
        handle.write(f"{date.today().isoformat()} | {level} | {event} | {review} | {elapsed}\n")
