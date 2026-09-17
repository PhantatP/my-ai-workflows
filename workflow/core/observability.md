# Logging and observability

Log enough routing evidence without secrets or unnecessary user content:
`timestamp, platform, session, domain, level, reason, action, result,
assurance_state, event`. Carry only fields some mechanism actually populates.
`model_before`, `model_after`, `review`, `elapsed`, and `level_before` were
removed: only Main could supply them, Main never did, and empty columns bury
the fields that do carry information. `session` correlates every event from one
run and is what makes the log readable later. `.workflow/log.txt`
is append-written and human-readable; paths/trigger IDs are allowed when needed.
It has no tamper evidence, and each hook logs under its own root, so the trail
may span more than one file.
Never log raw commands, credentials, tokens, environment values, or unrelated
content. Logs improve workflow from use; they do not prove correctness or
enforcement.
