# Claude Code adapter

`CLAUDE.md` bootstraps Core and the relevant domain profile. `.claude/settings.json` installs a `PreToolUse` hook for `Bash|Write|Edit|MultiEdit`.

For Bash, the hook invokes `workflow/bin/enforce-operation` and blocks on sensitive matches or scanner failure. This is enforced only within the configured hook scope. For write tools, it scans the intended path and records mechanical BUILD floors; this is advisory routing evidence rather than a write block. `scan-change-set` remains the post-change backstop.

`.claude/agents/` contains optional role definitions and provider-specific model mappings. Their existence does not create a fixed pipeline. Main selects them only when delegation adds identifiable value.

Human approval for an override is not implemented by the shared guard. If a future adapter adds one, approval must be external to the proposing model, specific, short-lived, and logged without secrets.
