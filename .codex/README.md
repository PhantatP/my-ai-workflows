# Codex V2.2 adapter notes

Codex loads repository instructions from `AGENTS.md`. The current Codex CLI
exposes model, sandbox, and approval choices for the session, but does not
provide a repository-local, per-subagent model/tool manifest equivalent to
Claude Code's `.claude/agents/*.md` frontmatter.

The portable role restrictions are defined in
[`workflow/agents/roles.md`](../workflow/agents/roles.md) and must be included
in every Codex subagent hand-off. The active Main controls its session with the
Codex CLI or app settings; for example:

```text
codex --model <chosen-model> --sandbox workspace-write --ask-for-approval on-request
```

Use the least privilege appropriate to the task. In particular, require
read-only behavior in the Reviewer assignment and do not delegate an editing
task to an Explorer or Reviewer. This is a contract enforced by Main and the
platform's session permissions, not a per-agent repository setting.

