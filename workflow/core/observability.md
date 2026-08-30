# Logging and observability

Record enough information to understand routing behavior without retaining unnecessary user content or secrets.

Useful event fields are:

```text
timestamp, platform, session, domain, level_before, level_after, reason,
model_before, model_after, action, result, assurance_state
```

The minimal local operational log remains `.workflow/log.txt`. Events should be append-only and human-readable. Paths and trigger identifiers may be recorded when needed for mechanical evidence. Raw command text, credentials, tokens, environment values, and unrelated user content must not be logged.

Logging exists to improve the workflow from actual use. It is not a substitute for domain correctness evidence or platform enforcement.
