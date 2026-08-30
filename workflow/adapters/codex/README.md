# Codex adapter

Codex is a primary surface for BUILD, serious RESEARCH, and structured LEARN work. `AGENTS.md` bootstraps the portable workflow; Core logic remains under `workflow/`.

Codex does not currently provide a repository-local hook that reliably intercepts every native write or command. Therefore:

- intended-path scanning and `enforce-operation` are advisory caller obligations;
- `scan-change-set` is the authoritative post-change backstop when explicitly run;
- command denial is not claimed as platform-enforced for native tool calls;
- unavailable interception lowers assurance to `DEGRADED` when pre-action blocking is required.

Model choice is session- or delegation-dependent. Map abstract capability classes through the active Codex configuration. Do not promise automatic mid-session switching unless the running surface exposes it. Role restrictions are delegation contracts because repository-local per-role sandboxing is not guaranteed.

Use Markdown Task Packets for cross-platform handoff and persistent working state. Vault access is supported only when the user places a vault within accessible filesystem scope.
