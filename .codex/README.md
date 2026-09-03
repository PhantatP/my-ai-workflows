# Codex V2.4 experimental adapter notes

Codex loads repository instructions from `AGENTS.md`. Core policy, domain
profiles, model routing, and information conventions remain in `workflow/`;
this file documents session-level limitations only.

V2.4 retains the V2.3 general architecture and adds a LEARN-profile interaction
experiment; it does not add a cross-domain Interaction Layer.

The portable role restrictions are defined in
[`workflow/agents/roles.md`](../workflow/agents/roles.md) and must be included
in every Codex subagent handoff. The active Main controls model, sandbox, and
approval through the available CLI or app settings. Repository policy cannot
guarantee automatic mid-session model switching or per-role tool enforcement.
For example:

```text
codex --model <chosen-model> --sandbox workspace-write --ask-for-approval on-request
```

Map provider models to `STRONG`, `BALANCED`, and `ECONOMY` through adapter
configuration. Use the least privilege appropriate to the task. Require
read-only behavior in Reviewer assignments and do not delegate edits to an
Explorer or Reviewer. These are contracts enforced by Main and available
session permissions, not repository-local guarantees. See
[`workflow/adapters/codex/README.md`](../workflow/adapters/codex/README.md) for
the explicit capability declaration and degraded-assurance rules.

