# oauth-scope-diff

**Quick Pass.** Detect OAuth scope creep in app manifest changes.

## Use Case

OAuth apps often gain privileges gradually. This CLI gives reviewers a concrete list of risky scope changes before approval.

## Install

`oauth-scope-diff` accepts OAuth manifest diff or scope inventory in text, JSON, JSONL, or CSV form.

## Command Shape

```bash
python -m pip install -e ".[dev]"
oauth-scope-diff examples/sample.txt
oauth-scope-diff examples/sample.txt --json --fail-on medium
```

## Signals

| Rule | Severity | Meaning |
|---|---:|---|
| `admin-scope` | high | administrative scope requested |
| `write-scope` | medium | write scope requested |
| `offline-access` | low | long-lived access requested |

## Quality Gate

```bash
ruff check .
pytest
python -m oauth_scope_diff --help
```

License: MIT

### Example Input

```text
added scope admin:write offline_access users:read billing:write
```

### Architecture

`cli.py` reads files, `core.py` evaluates records, and `rules.py` keeps the oauth-scope-diff policy surface explicit.
