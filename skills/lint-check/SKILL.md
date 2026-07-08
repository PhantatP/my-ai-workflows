---
name: lint-check
description: Run Ruff and Basedpyright (Python-only linters) on the current project and report all errors categorized by severity and action. Use this skill whenever the user asks to check lint errors, run ruff, run pyright/basedpyright, check code quality, or asks "what errors do we have". Also use after any significant code change session to verify nothing broke.
---

## Tools

Both tools are **Python-only** — they analyze `.py` files exclusively.

- **Ruff** — fast Python linter (style, unused imports, real bugs)
- **Basedpyright** — Python static type checker

---

## Step 1: Locate source directories and config

Before running, do a quick scan:

1. **Find Python source dirs** — look for common patterns: `src/`, `app/`, `lib/`, subdirs containing `__init__.py`. If none of those, use the project root. Exclude `test/`, `tests/`, `venv/`, `.venv/`, `__pycache__/`, `migrations/`.

2. **Find pyrightconfig** — check for `pyrightconfig.json` or `pyproject.toml` with a `[tool.pyright]` section. Note which directory it's in — run basedpyright from there so the config is picked up.

3. **Find ruff config** — check for `ruff.toml`, `.ruff.toml`, or `[tool.ruff]` in `pyproject.toml`. Ruff auto-discovers config when run from the project root.

---

## Step 2: Run both linters in parallel

```bash
# From project root (or wherever ruff.toml / pyproject.toml lives)
ruff check <source-dirs>
```

```bash
# From the directory containing pyrightconfig.json (if present), otherwise project root
basedpyright <source-dirs>
```

If `pyrightconfig.json` is missing, basedpyright will report many `reportImplicitRelativeImport` errors that are false positives — note this in the report.

---

## Step 3: Report results

Present a structured report in three sections.

### Section A — Ruff

Group by error code, show count and `file:line: message` for each.

| Tier | Codes | Action |
|------|-------|--------|
| Critical | F821 (undefined name), F811 (redefined — duplicate logic?) | Fix immediately |
| Safe to fix | F401 (unused import), F541 (f-string no placeholder), F841 (unused variable) | Auto-fixable: `ruff check --fix --select F401,F541,F841` |
| Needs care | E722 (bare `except`), E741 (ambiguous name) | Manual review — bare excepts in hardware/IO code may be intentional |
| Style only — skip | E701, E702 (multi-statement lines), E402 (import not at top) | No behavior impact, low priority |

### Section B — Basedpyright

Group by error code, show count and `file:line` for each.

| Tier | Codes | Action |
|------|-------|--------|
| Review (may be real bugs) | `reportPossiblyUnbound`, `reportIndexIssue`, `reportUndefinedVariable` | Check each location |
| Review (often false positives) | `reportOptionalMemberAccess`, `reportOptionalCall` | Real if no None-guard; false positive if guarded by `if x is not None` or similar |
| Config fix (1 file) | `reportImplicitRelativeImport`, `reportMissingImports` | Add `pyrightconfig.json` with correct `executionEnvironments.root` |
| Skip | `reportMissingTypeArgument`, `reportUnknownVariableType`, `reportUnknownMemberType` | Annotation work only, no runtime impact |
| Skip | `reportConstantRedefinition` | Mutable module-level state with UPPER_CASE names — suppress in pyrightconfig if needed |
| Skip | `reportImportCycles` | Architectural, needs major refactor to fix |

### Section C — Summary

```
Ruff:         X errors  (Y critical, Z safe-to-fix, W style-skip)
Basedpyright: X errors  (Y review, Z config-fix, W skip)
```

End with a one-line recommendation, e.g.:
> "Run `ruff check --fix --select F401,F541,F841` to clear 12 safe errors. 2 E722 bare-excepts need manual review."

---

## pyrightconfig.json quick-fix

If `reportImplicitRelativeImport` errors are high, create this at the project root (or the dir that contains `src/`):

```json
{
  "pythonVersion": "3.12",
  "include": ["src"],
  "executionEnvironments": [{ "root": "src" }],
  "reportMissingImports": "none",
  "reportMissingModuleSource": "none"
}
```

Adjust `"include"` and `"root"` to match the actual source directory. Note: if `*.json` is in `.gitignore`, this file needs `git add -f` or a gitignore exception to be tracked.
