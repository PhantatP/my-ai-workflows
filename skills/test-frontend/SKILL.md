---
name: test-frontend
description: Use when the user asks to test the frontend UI, verify a page works, check that a button or interaction behaves correctly, or test a user flow in the browser. Uses Playwright MCP tools — no test files written.
---

# Frontend Testing (Playwright MCP)

Test the frontend interactively using Playwright MCP browser tools. No test files are written — tests are live browser sessions executed by Claude directly.

---

## Step 1: Understand what to test

From context or the user's request, identify:
- The page or component to test
- The user flow or interaction to verify
- The expected outcome

---

## Step 2: Open the browser and navigate

```
browser_navigate → <app URL>
```

If the dev server isn't running, tell the user to start it first. Do not guess the URL — check CLAUDE.md or ask.

Take a snapshot after navigation to confirm the page loaded:
```
browser_snapshot
```

---

## Step 3: Execute the test steps

Each test step is one interaction + one verification:

| Action | Tool |
|--------|------|
| Click a button or link | `browser_click` |
| Fill an input | `browser_fill_form` or `browser_type` |
| Wait for something | `browser_wait_for` |
| Read page state | `browser_snapshot` |
| Take a screenshot | `browser_take_screenshot` |
| Check console errors | `browser_console_messages` |

**After each meaningful action**, take a snapshot or screenshot to confirm the UI state is what you expect.

---

## Step 4: Verify the result

After each interaction, check that:
- The expected element is visible / hidden
- The expected text is present
- No JS errors in `browser_console_messages`

If something unexpected appears, take a screenshot to document it.

---

## Step 5: Report results

```
## Frontend Test Results

### Test: <what was tested>
Steps:
1. Navigated to /page — page loaded ✓
2. Clicked [Button] — modal appeared ✓
3. Filled form and submitted — success message shown ✓

Result: PASSED

---

### Test: <another flow>
Steps:
1. Navigated to /page — page loaded ✓
2. Clicked [Button] — expected dropdown did NOT appear

Result: FAILED
Console errors: TypeError: cannot read property 'x' of undefined
Screenshot: [taken]

---

### Summary
2 tests · 1 passed · 1 failed
Next: [what to investigate or fix]
```

---

## Common mistakes

| Mistake | Fix |
|---------|-----|
| Assuming the server is running | Ask or check before navigating |
| No snapshot after action | Always verify state after each interaction |
| Reporting pass without checking console | Always run `browser_console_messages` at the end |
| Testing too many things in one run | One flow per test — easier to isolate failures |
