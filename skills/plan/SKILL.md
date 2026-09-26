---
name: plan
description: Create or refine an actionable plan through a lightweight interaction preset across BUILD, RESEARCH, or LEARN. Use when the user explicitly asks for collaborative planning or a plan; do not invoke merely because ordinary work requires internal planning.
---

# PLAN interaction preset

PLAN is a V2.4 interaction preset, not a domain, assurance level,
model tier, agent role, or state machine.

Apply the existing Core router and the relevant BUILD, RESEARCH, or LEARN
profile first. The domain defines correctness. PLAN only shapes how the plan is
developed with the user.

## Preset

Use the lightest useful tendency:

```text
ELICIT → STRUCTURE → CHALLENGE → refine
```

- Before drafting, identify the one unknown most likely to change the plan. If
  it is missing, ask one focused question and stop, optionally giving only a
  short provisional spine. Do not write a detailed speculative plan and then
  ask the question that would determine its structure.
- Use existing context before asking anything. Ask only for missing information
  that can materially change the plan, such as the end state, a binding
  constraint, dependency, uncertainty, resource limit, or irreversible choice.
- If the task is sufficiently specified, skip elicitation and structure the
  plan directly.
- Produce the smallest execution structure that makes action clearer: sequence,
  dependencies, decisions, checkpoints, and a fallback only where useful.
- Default to a compact plan whose steps state outcomes or decisions. Defer
  detailed substeps, exhaustive evidence fields, schedules, and full curricula
  until the user requests them or they are necessary for the next action.
- Challenge the single most consequential assumption or failure mode before
  treating the plan as stable. If that challenge exposes an unanswered choice
  that would materially change the architecture, sequence, or scope, use it as
  the focused elicitation question: give at most a short provisional spine and
  stop. Do not present a detailed plan followed by the decision that determines
  it. Do not append a generic risk checklist.
- Refine from the answer, then stop planning when the next useful action is
  clear. Do not execute unless the user's request authorizes execution.

Ask one focused question at a time when interaction is needed. Skip, repeat, or
reorder the primitives when evidence warrants it. For a learning plan, do not
invent a curriculum before resolving a missing goal or binding time constraint.
For a research plan, structure how to test the question rather than prematurely
performing the whole analysis.

Keep domain labels, assurance levels, preset names, routing rationale, and other
workflow metadata out of the user-facing plan unless the user asks to inspect
the workflow.

Avoid planning theater, generic interviews, premature structure, irrelevant
risk dumping, and plan paralysis.
