# My AI Workflows — Claude Code adapter

This repository implements My AI Workflows V2.4 experimentally while retaining
the V2.3 general architecture. The shared workflow policy is platform-neutral
and lives in [`workflow/`](workflow/README.md). This file is only the Claude
Code entry point.

## Required reading order

1. [`workflow/core/principles.md`](workflow/core/principles.md)
2. [`workflow/core/architecture.md`](workflow/core/architecture.md)
3. [`workflow/core/routing.md`](workflow/core/routing.md)
4. [`workflow/core/assurance.md`](workflow/core/assurance.md)
5. The relevant profile under [`workflow/profiles/`](workflow/profiles/)
6. For BUILD, [`workflow/routing/triggers.yaml`](workflow/routing/triggers.yaml)
7. [`workflow/agents/roles.md`](workflow/agents/roles.md) before delegating.

## Main owns the task

The current agent is Main: it owns intent, domain segmentation, routing,
strategy, execution, integration, completion, and user communication. Planning
is a phase, testing an activity, and debugging a methodology. Delegate only
when independence, context isolation, specialist capability, or separable work
adds identifiable value.

Assess complexity, risk, uncertainty, evidence requirement, and reversibility
independently. Assurance, model capability, and agent count are separate.
Apply the relevant domain correctness contract and re-evaluate on new evidence.
Assistant material enters Capture or Working State unless deliberately curated.
For LEARN, apply the experimental interaction strategy in the LEARN profile and
keep workflow metadata internal by default; do not generalize it into a
cross-domain interaction policy yet.

## Claude-specific execution

- For Level 3+ BUILD use the independent read-only reviewer. In other domains,
  use a subagent only when genuine independence requires it; L4 parallel work
  must be genuinely separable.
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
- Scan intended BUILD paths with `workflow/bin/scan-triggers --platform
  claude_code` and use `workflow/bin/scan-change-set --platform claude_code`
  for the authoritative actual change set. Call `workflow/bin/enforce-operation
  --platform claude_code` before external sensitive commands;
  a denial is fail-closed. The mechanism writes append-only events to
  `.workflow/log.txt`.

## Core coding constraints

- Understand the relevant state and execution path before modifying it.
- For bugs, reproduce and establish a root-cause hypothesis before patching.
- Keep scope surgical and verify every requested behavior with proportionate
  evidence.
- Do not treat a test run as proof beyond what it actually exercised.
