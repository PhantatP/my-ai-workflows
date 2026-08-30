# Core routing procedure

Use this router for BUILD, RESEARCH, LEARN, Assistant operations, and tasks containing more than one domain.

## 1. Understand and segment

State the user's objective, constraints, and completion condition. Classify each meaningful segment as BUILD, RESEARCH, or LEARN. Treat capture, retrieval, organization, dispatch, and handoff as Assistant operations supporting those domains.

Do not impose the highest segment's process on every other segment. Main retains ownership of the whole task and integrates the results.

## 2. Assess independent properties

Use qualitative values; numeric scoring is not required.

| Property | Values | Primary effect |
| --- | --- | --- |
| Complexity | LOW, MEDIUM, HIGH | Coordination and structure |
| Risk | LOW, MEDIUM, HIGH, CRITICAL | Assurance |
| Uncertainty | LOW, MEDIUM, HIGH | Exploration |
| Evidence requirement | NONE, INTERNAL, EXTERNAL, PRIMARY, MULTI_SOURCE | Verification method |
| Reversibility | REVERSIBLE, COSTLY_TO_REVERSE, IRREVERSIBLE | Assurance and approval |

Domain profiles add domain-specific signals and correctness evidence. Mechanical policy may impose a minimum level. The required level is the maximum of that floor and Main's risk, complexity, uncertainty, and evidence judgment.

## 3. Choose assurance and execution strategy

Select L0–L4 using [assurance.md](assurance.md). Then choose mechanisms using
[execution-strategy.md](execution-strategy.md). An assurance level does not
prescribe an agent count.

Before initial L0–L2 work, record concisely:

- `possible_miss`: how the classification or scope could be wrong;
- `escalation_evidence`: observable evidence that requires stronger routing.

At L3–L4, use the same checkpoint when a meaningful routing judgment remains uncertain.

## 4. Select model capability

Apply [model-routing.md](model-routing.md) after choosing assurance. Use the cheapest sufficiently capable model for the current operation, considering handoff cost. Model strength does not satisfy an independence requirement.

## 5. Execute and re-evaluate

Follow the relevant domain profile. Re-enter routing whenever evidence changes complexity, risk, uncertainty, reversibility, evidence needs, mechanical floors, or platform assurance.

Escalation is always permitted. De-escalation requires inspectable evidence and a fresh counterargument checkpoint. Domain-specific mechanical floors may have stricter disproof requirements.

## 6. Verify and report

Apply the correctness contract of each domain segment. Report the domain, initial and final level, model capability changes when material, evidence obtained, verification performed, assurance degradation, remaining uncertainty, and next action if incomplete.
