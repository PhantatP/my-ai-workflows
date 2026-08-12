# BUILD routing procedure

Use this procedure for coding, debugging, refactoring, configuration,
architecture, automation, and other artifact modifications.

## 1. Inspect and mechanically scan

Understand the requested behavior and relevant execution path before editing.
Scan the actual proposed/current change set and available tool output using
`triggers.yaml`. Record every match, its detection method, evidence reference,
and the highest resulting mechanical floor.

A path discovered during exploration is not a trigger. It becomes one when it
enters the actual change set. A tool/command trigger applies when that command
or structured result occurs.

## 2. Assess and choose a level

Main explicitly assesses both complexity and judgment risk. Consider component
breadth, unfamiliarity, ambiguity, plausible approaches, exploration needed,
regression surface, consequences, detectability, reversibility, test-oracle
quality, hidden dependencies, concurrency, cross-boundary state, compatibility,
rollback, and unresolved assumptions.

Choose the required level as:

```text
max(mechanical floor, Main's complexity/risk level)
```

| Level | Minimum work |
| --- | --- |
| 0 | Direct answer or negligible non-behavioral change. |
| 1 | Inspect → implement → verify. |
| 2 | Explore/plan → implement → verify. |
| 3 | Level 2 discipline plus independent verification. |
| 4 | Level 3 plus parallel investigation only for genuinely separable work. |

Level 3 independent verification must include an independent reviewer; tests
are run when a relevant test or other verification mechanism exists. A lack of
a reliable test oracle is a judgment risk that may require stronger review or
additional evidence; it is not a mechanical trigger.

## 3. Counterargument checkpoint

Before initial Level 0, 1, or 2 execution, record concisely:

- `possible_miss`: how the scope or risk assessment could be wrong;
- `escalation_evidence`: observable evidence that would force a higher level.

For Levels 3–4, perform the same challenge when a meaningful routing judgment
is uncertain. This is a falsification target, not a request for lengthy hidden
reasoning.

## 4. Execute and re-evaluate

Implement with the chosen level. Whenever new evidence appears, rescan it:

- A new mechanical match activates its floor automatically and records an
  escalation event when it raises the required level.
- A judgment signal requires Main to reassess and record the semantic reason if
  it changes the level.

Escalation is always permitted. Prefer the higher level when the incremental
cost is reasonable and uncertainty remains.

## 5. De-escalate only with evidence

Complexity-driven reduction requires all of:

1. inspectable evidence supporting the reduction;
2. a fresh counterargument checkpoint;
3. an append-only `.workflow/log.txt` entry stating the evidence reference and
   counterargument.

It cannot lower the mechanical floor. To remove a mechanical floor, append a
trigger-disproof entry to `.workflow/log.txt` that includes the trigger,
detector, evidence reference, evidence summary, and `disproved: true`. An
explanation alone is never sufficient. The deferred structured telemetry schema
is not runtime policy.

## 6. Verify and report

Perform proportionate verification: tests, builds, types, static analysis,
runtime checks, diff inspection, and regression checks as applicable. At Level
3+, independent review attempts to find a concrete failure, missing assumption,
or compatibility issue. Record the evidence and any remaining uncertainty.
