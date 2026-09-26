# Codex adapter

`AGENTS.md` bootstraps policy. Codex documents a `PreToolUse` hook that can
deny Bash, `apply_patch`, and MCP calls, but none here invokes the shared
guard, so it stays `ADVISORY` until one does and a test demonstrates the deny
path. Until then, intended scanning and
`enforce-operation` are advisory caller obligations; explicit
`scan-change-set` is the authoritative post-change backstop; native command
denial is not platform-enforced. If pre-action blocking is required but absent,
report `DEGRADED`.

Map abstract model classes through active configuration; do not promise
unsupported automatic switching. Role restrictions are delegation contracts,
not guaranteed per-role sandboxing. Use Task Packets for handoff/persistent
working state; vault access requires user-scoped accessible filesystem.
Codex memories are Codex-only; facts about the user or project belong in the
portable profile and project state under
[information.md](../../core/information.md).
