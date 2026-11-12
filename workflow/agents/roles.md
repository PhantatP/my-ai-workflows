# Active V2.5.2 role contracts

Main owns the task. Create roles only for independent context/judgment,
specialist capability, or separable value; assurance, models, and agent count
do not map directly.

| Role | Assignment | Must not | Default |
| --- | --- | --- | --- |
| Explorer | Bounded evidence question | Edit, implement, teach as Main, choose strategy | `ECONOMY`/`BALANCED`, read-only |
| Implementer | Bounded approved BUILD change | Expand scope/self-approve consequences | `BALANCED`/`STRONG`, write/test |
| Reviewer | Independently falsify intent and primary evidence | Edit or rubber-stamp | `STRONG`, read-only |
| Researcher | One item of a research batch (one company, one lab); output as the batch spec Main writes first defines, e.g. one file per item or a text-only answer | Edit any file the spec does not name; compare, rank, or decide across items | `BALANCED`; `STRONG` only with a stated reason; web/write/shell |

Tool limits are restrictions, not unrelated authority. RESEARCH and LEARN are
profiles; a Researcher is only a worker for one item of a separable
multi-item research batch, and RESEARCH correctness, cross-item synthesis, and
conclusions stay with Main. V2.4 primitives do not create a Tutor. Planning,
testing, and debugging remain Main activities. Parallel agents are L4-only,
separable, and non-overlapping; Researcher batches are exempt from L4-only but
not from separable and non-overlapping.

A research batch spec names each item's output files, if any, and whether
each is created or updated under [information.md](../core/information.md),
plus a folder for raw copies of fetched sources (downloaded documents, not
WebFetch summaries). Main should have a Reviewer spot-check a sample of items
against those copies before relying on the batch.

Delegations state goal, bounded assignment, domain, level, evidence/diff,
output, and non-goals. A delegation that fits no role states its model class
and the files it may write; the platform adapter gives the details. Persistent/cross-platform handoffs use a Task Packet.
Reviewers also receive: falsify correctness with evidence; do not edit.
