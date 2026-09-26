# Antigravity adapter

Antigravity loads the root `AGENTS.md` as a workspace rule, so it shares the
Codex entry point. [`.agents/rules/antigravity.md`](../../../.agents/rules/antigravity.md)
is an always-on rule that overrides the Codex-specific parts; rule files
without a valid `trigger` frontmatter are silently discarded.

Antigravity documents `PreToolUse` hooks that can deny a tool call
(`<workspace>/.agents/hooks.json`), terminal deny/ask/allow lists, subagents, skills, and
model selection. None is wired to the shared guard or validated here, so they
stay `ADVISORY`. `pre_action_hook` and `command_blocking` can become `ENFORCED`
only after a hook invokes `workflow/bin/enforce-operation` and a test
demonstrates the deny path. `~/.gemini/antigravity/knowledge/` exists but its
behavior is undocumented; use the portable profile and project state instead.

Global rules live in `~/.gemini/AGENTS.md` or `~/.gemini/GEMINI.md`. Rule
files are capped at 24 KB each and 20,000 tokens across active rules.
