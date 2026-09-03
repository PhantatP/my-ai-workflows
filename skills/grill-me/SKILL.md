---
name: grill-me
description: Stress-test a user's understanding, claim, design, or plan through adaptive one-question-at-a-time challenge across BUILD, RESEARCH, or LEARN. Use when the user explicitly asks to be grilled, challenged, or probed for weaknesses.
---

# GRILL interaction preset

GRILL is an experimental V2.4 interaction preset, not a domain, assurance level,
model tier, reviewer role, or state machine. It does not replace independent
verification when the selected assurance level requires it.

Apply the existing Core router and the relevant BUILD, RESEARCH, or LEARN
profile first. The domain still defines correctness; GRILL only shapes the
interaction.

## Preset

Use the lightest useful tendency:

```text
ELICIT current position → CHALLENGE → inspect response → ADAPT
```

- Establish what is being tested from existing context. Ask one focused setup
  question only if the target is genuinely unclear.
- Ask one high-information question at a time, then stop for the user's answer.
  Use a list only when the user explicitly requests a questionnaire, mock exam,
  or batch exercise. Do not combine sequential questions with "and" merely to
  make them one sentence. A prediction plus its reasoning may be one integrated
  task; two answers where the first could determine the second should be split
  across turns.
- Select each next question from evidence in the previous response. Move past
  demonstrated strengths and deepen the weakness that matters most.
- Do not lecture before the user's attempt. Use STRUCTURE only when a concise
  clarification or correction will unlock the next challenge.
- Prefer consequential failure modes, predictions, transfer cases,
  counterexamples, or comparisons over trivia. In RESEARCH, distinguish
  evidence, inference, assumption, and prediction.
- Stop or change mode when the target has been demonstrated, further questions
  add little diagnostic value, the weakness is established, the user asks for
  explanation, or the exchange becomes repetitive.

Keep workflow metadata internal unless the user asks to inspect the experiment.
Do not follow a prepared script when the user's answers point elsewhere, and do
not move the goalposts merely to prolong the grill.
