# Logging and observability

Log enough routing evidence without secrets or unnecessary user content:
`timestamp, platform, session, domain, level_before, level_after, reason,
model_before, model_after, action, result, assurance_state`. `.workflow/log.txt`
is append-only and human-readable; paths/trigger IDs are allowed when needed.
Never log raw commands, credentials, tokens, environment values, or unrelated
content. Logs improve workflow from use; they do not prove correctness or
enforcement.
