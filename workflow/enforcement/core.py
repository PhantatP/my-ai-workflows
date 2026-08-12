"""Trigger scanning and fail-closed enforcement helpers.  Standard library only."""
from __future__ import annotations

import fnmatch
import json
import re
import shlex
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
    # Nested evaluation hides executable commands. A newline, an ordinary
    # interpreter invocation, and environment assignment are scanned normally.
    "shell_evaluated_command": re.compile(r"\$\(|`|<\(|^\s*eval\b|^\s*(?:sh|bash|zsh|powershell|pwsh)\s+[^\n]*-[A-Za-z]*c\b", re.I),
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
    """Split unquoted common Bash command-list separators.

    This tiny lexer deliberately recognizes only quotes, escapes, and list
    separators; it is not an attempt to parse shell grammar.
    """
    segments: list[str] = []
    start = 0
    quote: str | None = None
    escaped = False
    index = 0
    while index < len(command):
        char = command[index]
        if escaped:
            escaped = False
        elif char == "\\" and quote != "'":
            escaped = True
        elif quote:
            if char == quote:
                quote = None
        elif char in {"'", '"'}:
            quote = char
        elif char in "\r\n;|":
            end = index
            if char == "\r" and command[index + 1:index + 2] == "\n":
                index += 1
            elif char in "&|" and command[index + 1:index + 2] == char:
                index += 1
            segment = command[start:end].strip()
            if segment:
                segments.append(segment)
            start = index + 1
        elif char == "&" and command[index + 1:index + 2] == "&":
            segment = command[start:index].strip()
            if segment:
                segments.append(segment)
            index += 1
            start = index + 1
        index += 1
    segment = command[start:].strip()
    if segment:
        segments.append(segment)
    return segments


def executable_segment(segment: str) -> str:
    """Remove a small, explicit set of non-executing POSIX wrappers.

    This is intentionally not a shell parser. Unparseable input is returned
    unchanged; nested shell evaluation is handled by its own deny signature.
    """
    try:
        tokens = shlex.split(segment, posix=True)
    except ValueError:
        return segment

    while tokens:
        wrapper = tokens[0].lower()
        if wrapper in {"command", "nice"}:
            tokens.pop(0)
            if wrapper == "command":
                while tokens and tokens[0].startswith("-"):
                    tokens.pop(0)
            elif tokens[:1] == ["-n"]:
                del tokens[:2]
        elif wrapper == "sudo":
            tokens.pop(0)
            while tokens and tokens[0].startswith("-"):
                option = tokens.pop(0)
                if option in {"-u", "-g", "-h", "-p", "-r", "-t", "-C", "--user", "--group", "--host", "--prompt", "--role", "--type", "--close-from"} and tokens:
                    tokens.pop(0)
        elif wrapper == "timeout":
            tokens.pop(0)
            while tokens and tokens[0].startswith("-"):
                option = tokens.pop(0)
                if option in {"-k", "-s", "--kill-after", "--signal"} and tokens:
                    tokens.pop(0)
            if tokens:
                tokens.pop(0)
        elif wrapper == "env":
            tokens.pop(0)
            while tokens and (tokens[0].startswith("-") or re.fullmatch(r"[A-Za-z_]\w*=.*", tokens[0])):
                option = tokens.pop(0)
                if option in {"-u", "--unset", "-C", "--chdir", "-S", "--split-string"} and tokens:
                    tokens.pop(0)
        elif re.fullmatch(r"[A-Za-z_]\w*=.*", tokens[0]):
            tokens.pop(0)
        else:
            break
    return " ".join(tokens)


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
