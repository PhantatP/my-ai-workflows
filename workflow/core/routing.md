# Core routing procedure

Use for every domain and Assistant operation.

1. State objective, constraints, and completion; segment BUILD, RESEARCH, and LEARN. Do not impose one segment's level on another; Main integrates.
2. Assess complexity (LOW–HIGH), risk (LOW–CRITICAL), uncertainty (LOW–HIGH), evidence need (NONE, INTERNAL, EXTERNAL, PRIMARY, MULTI_SOURCE), and reversibility (REVERSIBLE, COSTLY_TO_REVERSE, IRREVERSIBLE). Profiles add signals. Required level is the higher of mechanical floor and judgment.
3. Select L0–L4 ([assurance.md](assurance.md)) and mechanisms ([execution-strategy.md](execution-strategy.md)). For initial L0–L2 work, record `possible_miss` and observable `escalation_evidence`; at L3–L4 do so if routing remains meaningfully uncertain.
4. Select the cheapest suitable capability under [model-routing.md](model-routing.md); model strength never supplies independence.
5. Follow the profile and re-route when complexity, risk, uncertainty, reversibility, evidence needs, mechanical floor, or platform assurance changes. Escalation is always allowed. De-escalation needs inspectable evidence and a fresh counterargument; profiles may require stricter disproof.
6. Verify each domain contract and report domains, initial/final levels, material model changes, evidence, verification, degraded assurance, uncertainty, and next action if incomplete.
