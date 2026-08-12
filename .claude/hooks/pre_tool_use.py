#!/usr/bin/env python3
"""Claude Code PreToolUse hook: wires the shared V2.2.1 enforcement core.

Bash: runs `workflow/bin/enforce-operation` on the proposed command and
blocks (exit 2) when it denies. Write/Edit/MultiEdit: runs
`workflow/bin/scan-triggers --intended-path` on the target file so sensitive
paths are logged before mutation; this is advisory (raises the mechanical
floor for Main's routing) and does not block, matching workflow/routing/build.md.
Any failure to run the scanner itself is fail-closed for Bash only, per
workflow/enforcement/core.py's contract.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
ENFORCE = ROOT / "workflow" / "bin" / "enforce-operation"
SCAN = ROOT / "workflow" / "bin" / "scan-triggers"

from workflow.enforcement.core import append_log  # noqa: E402


def deny(reason: str) -> None:
    print(reason, file=sys.stderr)
    raise SystemExit(2)


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except Exception as error:
        append_log(ROOT, "L?", f"DENIED: malformed hook payload ({error})")
        deny("Blocked by workflow enforcement: malformed hook payload. See .workflow/log.txt.")

    if not isinstance(payload, dict):
        append_log(ROOT, "L?", "DENIED: malformed hook payload (not an object)")
        deny("Blocked by workflow enforcement: malformed hook payload. See .workflow/log.txt.")

    tool_name = payload.get("tool_name")
    tool_input = payload.get("tool_input") or {}
    if not isinstance(tool_input, dict):
        append_log(ROOT, "L?", "DENIED: malformed hook payload (tool_input is not an object)")
        deny("Blocked by workflow enforcement: malformed hook payload. See .workflow/log.txt.")

    if tool_name == "Bash":
        command = tool_input.get("command")
        if command is not None and not isinstance(command, str):
            append_log(ROOT, "L?", "DENIED: malformed hook payload (Bash command is not a string)")
            deny("Blocked by workflow enforcement: malformed hook payload. See .workflow/log.txt.")
        if not command:
            raise SystemExit(0)
        result = subprocess.run(
            [sys.executable, str(ENFORCE), "--command", command, "--log-root", str(ROOT)],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            raise SystemExit(0)
        if result.returncode in (2, 3):
            try:
                decision = json.loads(result.stdout)
                reason = decision.get("reason", "sensitive_operation")
            except Exception:
                reason = "scanner_failure"
            deny(f"Blocked by workflow enforcement: {reason}. See .workflow/log.txt.")
        # Unexpected guard failure: fail closed for Bash, per core.py's contract.
        deny("Blocked by workflow enforcement: enforce-operation could not be evaluated.")

    if tool_name in ("Write", "Edit", "MultiEdit"):
        path = tool_input.get("file_path")
        if not path:
            raise SystemExit(0)
        try:
            rel = str(Path(path).resolve().relative_to(ROOT)).replace("\\", "/")
        except ValueError:
            rel = path.replace("\\", "/")
        result = subprocess.run(
            [sys.executable, str(SCAN), "--intended-path", rel, "--log-root", str(ROOT)],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            append_log(ROOT, "L?", "DEGRADED: path scanner failure before edit")
        # Path triggers only raise the mechanical floor for Main's routing;
        # they do not block the write (workflow/routing/build.md).
        raise SystemExit(0)

    raise SystemExit(0)


if __name__ == "__main__":
    main()
