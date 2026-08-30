# Adaptive model routing

Model selection is separate from assurance routing. Choose the cheapest model that can reliably perform the current operation.

Core uses provider-neutral capability classes:

- `STRONG`: judgment-heavy framing, architecture, difficult decomposition, conflicting-evidence synthesis, high-uncertainty diagnosis, adversarial review, or final judgment;
- `BALANCED`: ordinary implementation, analysis, tool use, and integration;
- `ECONOMY`: bounded edits, extraction, formatting, candidate collection, simple classification, and mechanical checks.

Platform adapters map these classes to available models. Core must not depend on provider or product names.

Evaluate models by the capabilities that matter to the operation: reasoning,
judgment, context handling, instruction following, tool execution, precision,
speed, and cost. A provider model may be strong on some dimensions and weak on
others; the three classes are routing shorthand, not universal rankings.

## Routing rules

1. Start with the cheapest class that can meet the operation's capability needs.
2. Escalate capability when ambiguity, judgment, context, instruction-following, tool precision, or synthesis exceeds the current class.
3. Return to a cheaper class after the difficult decision is bounded.
4. Prefer a stronger model over another agent when the problem is insufficient reasoning capacity.
5. Use an independent reasoning instance when the problem is insufficient independence; a stronger Main model is not a substitute.
6. Avoid switching when context transfer, serialization, re-reading, and misunderstanding risk exceed expected savings.
7. Keep small tasks on the model already holding the necessary context.

Record material capability transitions and their reasons. Platform-specific automatic switching must not be claimed unless the adapter can actually perform it.
