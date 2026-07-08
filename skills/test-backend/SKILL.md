---
name: test-backend
description: Use when the user asks to test backend Python code, write pytest tests, verify a function works, check an API endpoint, or run the test suite. Also use after backend changes to confirm nothing broke.
---

# Backend Testing (pytest)

Write pytest **function tests** (not classes), run them, and report results clearly.

---

## Step 1: Understand what to test

From context or the user's request, identify:
- The function / endpoint / behavior to test
- Expected inputs and outputs
- Edge cases mentioned

Read the target source file before writing any test.

---

## Step 0: Check for project overrides

Before applying any defaults below, read the project's CLAUDE.md. If it has a **Backend Testing** section, its patterns take precedence over every default in this skill (test directory, import style, HTTP client, run command, mocking approach).

---

## Step 2: Find the test directory

Look for an existing test directory (`test/`, `tests/`, `src/test/`). If none, create one with an empty `__init__.py`. Name the file `test_<module_name>.py`. Reuse an existing test file if it already covers this module.

---

## Step 3: Write the test

Use **pytest functions**, not classes.

```python
# ✅ Correct style
def test_something_does_x():
    result = my_function(input)
    assert result == expected

# ❌ Avoid
class TestSomething:
    def test_x(self): ...
```

**Rules:**
- One assertion per test where possible — clearer failure messages
- Name tests `test_<what>_<condition>` e.g. `test_parse_empty_string`
- Do not mock internal functions — only mock at external boundaries (network, hardware, DB)
- For async functions use `pytest-anyio` or `pytest-asyncio` with `@pytest.mark.anyio`

**FastAPI endpoint template:**
```python
import pytest
from httpx import AsyncClient, ASGITransport
from <app_module> import app

@pytest.mark.anyio
async def test_endpoint_returns_200():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        res = await client.get("/api/your-route")
    assert res.status_code == 200
```

---

## Step 4: Run pytest

```bash
python -m pytest <test_file> -v
```

Flags:
- `-v` — always include (shows each test name)
- `-x` — stop on first failure (use when debugging)
- `--tb=short` — shorter tracebacks (use when many failures)

---

## Step 5: Report results

```
## Test Results — test_<module>.py

| Test | Result |
|------|--------|
| test_foo_returns_bar | PASSED |
| test_foo_empty_input | FAILED |

### Failed: test_foo_empty_input
What it tests: foo() with empty string returns None
Error:
  AssertionError: assert 'default' == None

### Summary
2 run · 1 passed · 1 failed
Next: [what to fix or investigate]
```

If all pass: one-liner summary is enough.

---

## Common mistakes

| Mistake | Fix |
|---------|-----|
| Wrong import path | Run with `python -m pytest` from the project root |
| Testing implementation details | Test behavior (inputs → outputs), not internal calls |
| `assert res == True` | Use `assert res` — clearer failure message |
| Mocking too deep | Mock only at the boundary (HTTP client, DB driver, hardware) |
