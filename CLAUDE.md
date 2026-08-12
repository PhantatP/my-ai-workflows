# My AI Workflows — Claude Code adapter

This repository implements My AI Workflows V2.2. The shared workflow policy is
platform-neutral and lives in [`workflow/`](workflow/README.md). This file is
only the Claude Code entry point.

## Required reading order for BUILD work

1. [`workflow/principles.md`](workflow/principles.md)
2. [`workflow/routing/build.md`](workflow/routing/build.md)
3. [`workflow/routing/triggers.yaml`](workflow/routing/triggers.yaml)
4. [`workflow/telemetry/schema.yaml`](workflow/telemetry/schema.yaml) when a
   routing, escalation, de-escalation, disproof, review, or verification event
   must be recorded.
5. [`workflow/agents/roles.md`](workflow/agents/roles.md) before delegating.

## Main owns the task

The current agent is Main: it owns assessment, strategy, execution,
integration, and user communication. Do not invoke the legacy `orchestrator`
agent as a mandatory entry point. Planning and testing are phases; debugging is
a methodology. Create a separate worker only when independent context or
judgment materially improves the outcome.

For BUILD tasks, follow the shared routing pipeline: inspect, scan mechanical
triggers, assess complexity and judgment risk, run the counterargument
checkpoint before Levels 0–2, execute, re-evaluate on new evidence, verify, and
record required audit events. Mechanical floors cannot be reduced by narrative.

## Claude-specific execution

- Use subagents only at Level 3+ when independent verification is required, or
  at Level 4 when work is genuinely separable.
- The active Claude Code definitions are in `.claude/agents/`; their model and
  allowed-tool frontmatter enforce the Explorer, Implementer, and Reviewer
  boundaries. Do not replace these with the archived V1 definitions.
- Pass an independent reviewer the task intent, changed-file list/diff, relevant
  evidence, and the instruction to falsify correctness. The reviewer must not
  edit the implementation.
- `archive/v1/` contains legacy Claude Code inventory for audit only. It is not
  part of normal routing and does not create mandatory workflow stages.
- Active reusable methodologies are in `skills/`. Load one only when it is
  relevant to the selected workflow level and task; they are not fixed stages.
- Store a telemetry record under `.workflow/telemetry/` only when that project
  has elected to persist records. Otherwise include the schema fields in the
  final task report.

## Core coding constraints

- Understand the relevant execution path before modifying it.
- For bugs, reproduce and establish a root-cause hypothesis before patching.
- Keep scope surgical and verify every requested behavior with proportionate
  evidence.
- Do not treat a test run as proof beyond what it actually exercised.
