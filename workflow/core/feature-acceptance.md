# Workflow feature acceptance

Before making a feature part of the default workflow, answer:

1. What failure does it prevent?
2. What meaningful effort does it reduce?
3. Is it Core, domain policy, model routing, information handling, or adapter behavior?
4. Could Main perform the work adequately without it?
5. Does it add ceremony to L0/L1 tasks?
6. Does it require another agent unnecessarily?
7. Could a stronger model solve the problem more cheaply?
8. Could a cheaper model execute the bounded portion?
9. Is it supported by actual usage evidence?
10. What happens when it fails?
11. Can assurance degradation be detected?
12. Does persistent information remain human-readable?
13. Does assistant-generated information remain distinguishable from curated Knowledge?
14. If removed, would the workflow meaningfully become worse?

If the answer to the last question is no, keep the feature optional or omit it.
