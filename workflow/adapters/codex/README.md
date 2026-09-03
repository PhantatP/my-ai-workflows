# Codex adapter

`AGENTS.md` bootstraps policy. Codex has no repository-local hook reliably
intercepting every native write/command: intended scanning and
`enforce-operation` are advisory caller obligations; explicit
`scan-change-set` is the authoritative post-change backstop; native command
denial is not platform-enforced. If pre-action blocking is required but absent,
report `DEGRADED`.

Map abstract model classes through active configuration; do not promise
unsupported automatic switching. Role restrictions are delegation contracts,
not guaranteed per-role sandboxing. Use Task Packets for handoff/persistent
working state; vault access requires user-scoped accessible filesystem.
