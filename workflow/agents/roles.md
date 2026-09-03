# Active V2.4 role contracts

Main is the task owner. A role is created only when independent context,
judgment, specialist capability, or separable work adds identifiable value.
Assurance level does not map directly to agent count or model tier.

| Role | Typical level | Assignment | Must not | Default capability |
| --- | --- | --- | --- | --- |
| Explorer | L2 or L4 | Inspect a bounded question; return evidence, provenance, and uncertainty. | Edit, implement, teach as Main, or choose final strategy. | `ECONOMY` or `BALANCED`; read-only tools. |
| Implementer | L2–L4 BUILD | Make a bounded, approved artifact change and report verification evidence. | Expand scope or self-approve consequential work. | `BALANCED` or `STRONG`; read/write and test tools. |
| Reviewer | L3–L4 | Independently falsify an artifact or conclusion from intent and primary evidence. | Edit the implementation or rubber-stamp. | Usually `STRONG`; read-only tools. |

Main selects the cheapest sufficiently capable model and appropriate tools.
Exploration may be inexpensive, BUILD implementation needs write access, and
review is read-only and independently reasoned. A role's tool boundary is a
minimum restriction, not permission for unrelated action.

RESEARCH and LEARN are active domain profiles, not permanent agent roles. Main
may give an Explorer a bounded evidence question or a Reviewer an independent
falsification task. A permanent Researcher or Tutor should not be added until
real use demonstrates value that a bounded assignment cannot supply.

The experimental LEARN interaction strategy does not create a Tutor role. Its
primitives are conversational tendencies owned by Main, not agent assignments
or a separate orchestration system.

Planning is normally Main's L2 phase, testing is a verification activity, and
debugging follows the root-cause methodology. Parallel agents are an L4 option
for separate, non-overlapping questions, not a default for long tasks.

`archive/v1/agents/` is V1 inventory, not the V2.2 active roster. Its
reduction is a subsequent audit, not part of the BUILD-core migration.

## Hand-off contract

Every delegation includes the goal, bounded assignment, domain, assurance
level, relevant evidence or diff, expected output, and explicit non-goals. Use
the Core Task Packet when persistence or cross-platform transfer is useful.
Reviewers additionally receive: "Try to falsify correctness; report concrete
findings with evidence. Do not edit files."

