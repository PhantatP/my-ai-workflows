---
name: my-ai-workflows
description: Apply My AI Workflows V2.2 to BUILD tasks: mechanically scan changes, choose progressive rigor, challenge low-rigor routing, re-evaluate new evidence, and verify proportionately. Use for coding, debugging, refactoring, configuration, architecture, and automation work.
---

# My AI Workflows V2.2 — BUILD core

Main owns the task and selects the minimum reliable orchestration level. An
agent exists only for independent context or judgment; planning is normally a
phase, testing an activity, and debugging a root-cause methodology.

## Route every BUILD task

1. Inspect the intended behavior and relevant execution path before editing.
2. Mechanically scan the actual change set and tool output for sensitive paths,
   migrations/schema, dependency manifests/lockfiles, production/deployment/
   infrastructure, public API/protocol files, and destructive operations.
3. Every mechanical match establishes a Level 3 minimum. Record its trigger,
   detector, evidence reference, and floor. It cannot be reduced by explanation.
4. Assess complexity and explicit judgment risks separately: coupling,
   ambiguity, test-oracle quality, hidden dependencies, compatibility,
   concurrency, rollback, and unresolved assumptions.
5. Required level is `max(mechanical floor, judgment/complexity level)`:
   - Level 0: direct/negligible work.
   - Level 1: inspect → implement → verify.
   - Level 2: explore/plan → implement → verify.
   - Level 3: Level 2 plus independent, read-only falsification review.
   - Level 4: Level 3 plus parallel investigation only for separable work.
6. Before Levels 0–2 execution, record a possible miss and observable evidence
   that would force escalation. Repeat this checkpoint before de-escalation.
7. Re-evaluate new evidence continuously. Sensitive files entering the actual
   diff automatically activate their trigger. Escalation is always allowed.
8. De-escalation needs inspectable evidence, a fresh counterargument, and an
   audit event. Removing a mechanical floor additionally requires an
   inspectable trigger-disproof event.
9. Verify proportionately with relevant tests, builds, static/type checks,
   runtime checks, and diff inspection. At Level 3+, an independent reviewer
   tries to falsify correctness and does not edit.

## Report audit facts

Distinguish mechanical facts from semantic interpretation. Include mode,
initial/final level, mechanical floor and triggers, escalation/de-escalation or
disproof events, independent-review requirement/completion, verification
evidence, files changed, judgment risks, review findings, and remaining
uncertainty. Persist the record only when the repository opts in; otherwise
include it in the final report.

