---
name: plan-as-html
description: Use when the user asks to write, create, or generate a plan as HTML — or when producing a structured implementation plan that should be visually browsable rather than markdown text.
---

# Plan as HTML

Generate implementation plans as self-contained HTML files that can be opened in a browser.

## When to Use

- User says "make a plan as HTML", "write plan as HTML", "create HTML plan"
- User wants a browsable/shareable plan document
- Plan has many steps and benefits from visual structure

## Output

Write to a file named `plan-<slug>.html` in the project root (or path user specifies).

## Template

Use this structure — inline CSS, no external dependencies:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Plan: {TITLE}</title>
<style>
  :root { --accent: #4f8ef7; --bg: #0f1117; --surface: #1a1d27; --border: #2a2d3a; --text: #e2e4ed; --muted: #6b7280; --success: #22c55e; --warn: #f59e0b; }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { background: var(--bg); color: var(--text); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; font-size: 15px; line-height: 1.6; padding: 40px 24px; }
  .container { max-width: 860px; margin: 0 auto; }
  h1 { font-size: 1.8rem; font-weight: 700; margin-bottom: 6px; }
  .meta { color: var(--muted); font-size: 0.85rem; margin-bottom: 32px; }
  .section { margin-bottom: 32px; }
  .section-title { font-size: 0.75rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); margin-bottom: 12px; }
  .goal-box { background: var(--surface); border-left: 3px solid var(--accent); border-radius: 6px; padding: 16px 20px; }
  .steps { list-style: none; display: flex; flex-direction: column; gap: 10px; }
  .step { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 16px 20px; display: grid; grid-template-columns: 28px 1fr; gap: 12px; align-items: start; }
  .step-num { background: var(--accent); color: #fff; border-radius: 50%; width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 700; flex-shrink: 0; margin-top: 2px; }
  .step-title { font-weight: 600; margin-bottom: 4px; }
  .step-desc { color: var(--muted); font-size: 0.9rem; }
  .step-verify { display: inline-block; margin-top: 8px; font-size: 0.8rem; color: var(--success); }
  .step-verify::before { content: "verify: "; color: var(--muted); }
  .risks { display: flex; flex-direction: column; gap: 8px; }
  .risk { background: var(--surface); border: 1px solid var(--border); border-left: 3px solid var(--warn); border-radius: 6px; padding: 12px 16px; font-size: 0.9rem; }
  .risk strong { display: block; margin-bottom: 2px; }
  .risk span { color: var(--muted); }
  code { background: #252836; padding: 1px 6px; border-radius: 4px; font-family: "JetBrains Mono", "Fira Code", monospace; font-size: 0.85em; }
</style>
</head>
<body>
<div class="container">

  <h1>{TITLE}</h1>
  <div class="meta">Generated {DATE}</div>

  <div class="section">
    <div class="section-title">Goal</div>
    <div class="goal-box">{GOAL}</div>
  </div>

  <div class="section">
    <div class="section-title">Steps</div>
    <ol class="steps">
      <!-- Repeat per step: -->
      <li class="step">
        <div class="step-num">1</div>
        <div>
          <div class="step-title">{STEP_TITLE}</div>
          <div class="step-desc">{STEP_DETAIL}</div>
          <span class="step-verify">{VERIFY_CHECK}</span>
        </div>
      </li>
    </ol>
  </div>

  <div class="section">
    <div class="section-title">Risks</div>
    <div class="risks">
      <!-- Repeat per risk: -->
      <div class="risk">
        <strong>{RISK_TITLE}</strong>
        <span>{MITIGATION}</span>
      </div>
    </div>
  </div>

</div>
</body>
</html>
```

## Rules

- Fill in `{DATE}` with today's date (from session context).
- Remove sections with no content (e.g. no risks → drop risks section).
- Add a `step-verify` span only when a concrete check exists for that step.
- Use `<code>` tags for file paths, commands, and identifiers inline.
- Output the HTML file path to the user so they can open it.
