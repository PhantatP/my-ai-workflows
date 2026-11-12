# Claude Code adapter

`CLAUDE.md` bootstraps Core and the relevant domain profile. `.claude/settings.json` installs a `PreToolUse` hook for `Bash|Write|Edit|MultiEdit`.

For Bash, the hook invokes `workflow/bin/enforce-operation` and blocks on sensitive matches or scanner failure. This is enforced only within the configured hook scope. For write tools, it scans the intended path and records mechanical BUILD floors; this is advisory routing evidence rather than a write block. `scan-change-set` remains the post-change backstop.

`.claude/agents/` contains optional role definitions and provider-specific model mappings. Their existence does not create a fixed pipeline. Main selects them only when delegation adds identifiable value.

[`models.yaml`](models.yaml) maps the model-routing classes to Claude models and effort levels. Agent frontmatter sets only each role's default model (Explorer haiku, Implementer sonnet, Reviewer opus, Researcher sonnet); effort otherwise follows the user's settings. For each delegation, Main picks the cheapest class among those [roles.md](../../agents/roles.md) lists for the role that fits the operation's complexity and risk, passes that class's `model` and `effort`, and states a model above or below the role default in its report. Main cannot change its own model; the user selects it with `/model`, so Main may suggest a cheaper model when a session's work is routine.

Use the built-in `general-purpose` agent only when no role in [roles.md](../../agents/roles.md) fits, for example image transcription that writes files. Main always passes a class's `model` and `effort` (default `BALANCED`), never letting it inherit Main's model, and names in the prompt the files the agent may write.

Every call re-sends the whole context, so cost grows with context size times the number of calls. Keep one task per session: when a task is complete and the next one is unrelated, suggest `/clear` or a new session; suggest `/compact` when a long task continues.

`~/.claude/` holds a copy of this repository's `workflow/`, role agents, and hook, not a link. After changing them, run `scripts/install-global.py` to preview and `scripts/install-global.py --apply` to install; `tests/test_global_install_in_sync.py` fails until the copy matches.

Claude Code auto-memory (`~/.claude/projects/<project>/memory/`) loads every session but is invisible to other platforms. Keep it to Claude-specific behavior; facts about the user or project belong in the portable profile and project state under [information.md](../../core/information.md).

Human approval for an override is not implemented by the shared guard. If a future adapter adds one, approval must be external to the proposing model, specific, short-lived, and logged without secrets.
