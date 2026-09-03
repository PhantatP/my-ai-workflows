# V2.5.1 — Context Retrieval and Policy Compression (experimental)

This policy applies across BUILD, RESEARCH, LEARN, and Assistant information
logistics. Persistent storage is not active context: retrieve the smallest
working set that can support the current answer or action.

## Runtime rule

Start from the task. Identify the objective, constraints, required decision or
output, likely relevant artifacts, and what could change the result. Retrieve
progressively:

```text
Tier 0 metadata → Tier 1 canonical state → Tier 2 relevant detail → Tier 3 original evidence
```

- **Tier 0:** path, title, tags, role, lifecycle, timestamps, index entries, and
  known links. Use it to select candidates.
- **Tier 1:** the smallest canonical representation of current state.
- **Tier 2:** only the needed section, function, claim, excerpt, or result.
- **Tier 3:** original or large sources for verification, freshness, conflict,
  missing provenance/detail, or high-consequence decisions.

Maintain a compact working set: objective, constraints, decisions, open
questions, canonical artifacts, required evidence, and immediate next action.
Links and citations are candidates, not commands; follow them only for a
task-specific reason. Reuse unchanged valid summaries and refresh stale claims
selectively. Stop when more context is unlikely to change the answer, next
action, confidence, or verification state.

Correctness, safety, explicit comprehensive requests, and required evidence
override context reduction. If missing context causes rework, expand retrieval
and record the gap; do not optimize token counts at the expense of correctness.

Before creating durable information, retrieve first: search for the canonical
artifact, inspect its metadata/state, then update, link, snapshot, or create as
required by [information.md](information.md). Do not retain irrelevant context
after it stops contributing.

## Policy compression rule

Each behavioral invariant has one canonical home. Core contains universal
rules; domain profiles contain correctness behavior; skills contain thin
invocation behavior; adapters translate platform capability; experiments hold
only experimental deltas and evidence; local rules remain local. Hot policy is
concise. Rationale, history, and extended examples belong in cold documents.

Compress duplication and prose, never safety boundaries, exceptions,
escalation conditions, user-control rules, verification requirements, or stop
conditions. Do not load unrelated profiles, historical experiments, unused
skills, or adapters during routine work.

See the [V2.5.1 experiment record](../experiments/v2.5.1-context-retrieval.md)
for validation cases, measurements, and the promotion gate.
