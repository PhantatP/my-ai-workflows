# My AI Workflows — Codex adapter

This repository implements My AI Workflows V2.2.1. The platform-neutral policy
lives in [`workflow/`](workflow/README.md); this is the Codex entry point.

## Required reading order for BUILD work

1. [`workflow/principles.md`](workflow/principles.md)
2. [`workflow/routing/build.md`](workflow/routing/build.md)
3. [`workflow/routing/triggers.yaml`](workflow/routing/triggers.yaml)
4. [`workflow/agents/roles.md`](workflow/agents/roles.md) before delegating.

## Main owns the task

The active agent is Main. It owns task understanding, strategy, execution,
integration, and communication. Planning is normally a phase; testing is an
activity; debugging is a methodology. Use an independent worker only when its
separate context or judgment is useful.

For BUILD tasks, apply the shared routing pipeline: inspect, mechanically scan
the actual change set, assess complexity and judgment risk, run the
counterargument checkpoint before low-rigor work, execute, re-evaluate on new
evidence, verify, and record required audit events. Never reduce a mechanical
floor without an inspectable trigger-disproof event.

## Codex-specific execution

- Use a reviewer subagent at Level 3+; give it task intent, changed files/diff,
  relevant evidence, and a falsification-oriented assignment. It must not edit
  the implementation.
- Follow [`.codex/README.md`](.codex/README.md) for Codex's session-level model
  and permission controls; role-level restrictions are delegation contracts.
- Use parallel workers only at Level 4 and only for independent, separable
  questions.
- `archive/v1/` contains Claude Code V1 inventory, retained for audit. It is
  not Codex configuration and does not create mandatory workflow stages.
- Use `workflow/bin/scan-triggers` for intended paths and actual changed paths.
  Use `workflow/bin/enforce-operation` before external sensitive commands;
  its deny decision is fail-closed. Report enforcement evidence in the final
  response; `.workflow/log.txt` is the minimal local operational log.

## Core coding constraints

- Inspect the relevant execution path before editing.
- Reproduce bugs and test the root-cause hypothesis before applying a fix.
- Keep changes within the requested scope and verify requested behavior with
  proportionate evidence.
