# RESEARCH profile

## Objective and correctness contract

Produce conclusions whose confidence is proportional to the available evidence.

```text
source quality
+ evidence coverage
+ contradiction handling
+ calibrated uncertainty
```

Label material claims as `FACT`, `INFERENCE`, `HYPOTHESIS`, or `SPECULATION` when confusion between them would matter. Never silently collapse one category into another.

## Flow

```text
Define the question
→ gather evidence
→ evaluate quality, provenance, and recency
→ form candidate conclusions
→ search for contradiction or falsification
→ synthesize
→ state uncertainty
```

Evidence requirements guide source selection:

- `NONE`: explanation from stable knowledge is sufficient.
- `INTERNAL`: repository, runtime, or supplied evidence is sufficient.
- `EXTERNAL`: current external sources are needed.
- `PRIMARY`: authoritative or original evidence is required.
- `MULTI_SOURCE`: independent coverage or competing views are required.

Prefer primary sources for important factual claims. Separate source statements from Main's synthesis. Preserve enough provenance for later re-evaluation.

Start refreshes from the canonical research state. Identify stale or disputed
claims, retrieve targeted supporting evidence, and open full sources only when
the summary lacks needed detail or direct verification is required. See
[Core progressive retrieval](../../core/context.md).

## Escalation signals

Time-sensitive facts, predictions, conflicting credible sources, contested topics, important decisions, unclear provenance, large inference gaps, or missing primary evidence raise uncertainty or assurance.

## RESEARCH levels

- L0: direct stable fact or simple explanation with no meaningful evidence burden.
- L1: answer with a sanity check and proportionate source support.
- L2: structured question, targeted collection, source evaluation, synthesis, and explicit uncertainty.
- L3: actively challenge the candidate conclusion through independent reasoning, primary-source verification, contradiction search, or multiple independent sources.
- L4: rare, high-impact research with checkpoints, multiple evidence types, explicit decision criteria, and human review where appropriate.

A second agent is optional. At L3, independence may come from a genuinely alternative evidence path rather than agent count.
