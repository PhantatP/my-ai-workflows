# Enforcement adapters

The deterministic implementation is in `workflow/enforcement/` and is shared
by all platforms. Adapters must call `workflow/bin/scan-triggers --log-root .` for intended
paths before editing and `workflow/bin/scan-change-set` after changes. They
must call `workflow/bin/enforce-operation --command <command>` before an
external command that could change production state.

`enforce-operation` denies every command when its scanner cannot run or returns
malformed JSON. It denies matched destructive and production-sensitive commands.
The shared core intentionally has no approval flag: a caller-provided boolean
would let the proposing model silently approve itself. An adapter may add an
override only when it can obtain a separate, explicit user confirmation, and
must log that override. The mechanism appends activations and denials to
`.workflow/log.txt`; `.workflow/` is local operational evidence.

## Codex

Codex currently has no repository-local reliable pre-write or pre-command hook
that can intercept every native edit/tool invocation. The Codex adapter is
therefore the scanner and guard entry points above: callers can enforce before
their own operations, and `scan-change-set` is the authoritative post-change
backstop. This is not claimed to provide Claude hook parity.

## Claude Code

`.claude/settings.json` wires a `PreToolUse` hook (`.claude/hooks/pre_tool_use.py`)
for `Bash|Write|Edit|MultiEdit`. For Bash it calls `enforce-operation` and
blocks (exit 2) on denial, so a proposed destructive or production-sensitive
command cannot execute merely because the model decides to continue. For
Write/Edit/MultiEdit it calls `scan-triggers --intended-path` on the target
file; this is advisory logging that raises the mechanical floor for routing,
not a block, since path triggers are not destructive operations. A malformed
hook payload is denied and logged; a path-scanner failure is logged as degraded
mode but does not block an ordinary edit. The shared scanner remains the sole
trigger implementation; the hook only wires it in.
