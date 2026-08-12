# Active V2.2 role contracts

These are the small active BUILD roster. Main is the task owner; a role is
created only when independent context or judgment adds value.

| Role | Typical level | Assignment | Must not | Default capability |
| --- | --- | --- | --- | --- |
| Explorer | 2 or 4 | Inspect a bounded question; return paths, evidence, and uncertainty. | Edit, implement, or choose final strategy. | Fast/low-cost model; read-only tools. |
| Implementer | 2–4 | Make a bounded, approved change and report verification evidence. | Expand scope or self-approve high-risk work. | Strong coding model; read/write and test tools. |
| Reviewer | 3–4 | Independently falsify the proposed change using the task intent and diff. | Edit code or rubber-stamp. | Strong reasoning model; read-only tools. |

Main selects the model and tools appropriate to the platform. The default
posture is deliberately asymmetric: exploration may be inexpensive,
implementation needs write access, and review is read-only and independently
reasoned. A role's tool boundary is a minimum restriction, not permission to
take unrelated action.

Experimental RESEARCH and LEARN roles (Researcher, Tutor) are not configured as
active agents yet: Researcher would report sources and uncertainty for
RESEARCH work, Tutor would teach without owning product decisions for LEARN
work. Neither exists until real use justifies the independence.

Planning is normally Main's Level 2 phase, not a separate agent. Testing is a
verification activity. Debugging follows the root-cause methodology. Parallel
agents require separate, non-overlapping questions; do not parallelize
duplicate investigation.

`archive/v1/agents/` is V1 inventory, not the V2.2 active roster. Its
reduction is a subsequent audit, not part of the BUILD-core migration.

## Hand-off contract

Every delegation includes the task, bounded assignment, current orchestration
level, relevant evidence/diff, expected output, and explicit non-goals.
Reviewers additionally receive: "Try to falsify correctness; report concrete
findings with evidence. Do not edit files."

