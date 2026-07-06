# OAuth Scope Diff

Detect OAuth scope creep in app manifest changes. In practice it is a narrow guardrail for deployment, cloud, CI, config, and operational safety checks: one command, a concrete report, and very little ceremony.

## Project card

<img src="assets/readme-cover.svg" alt="OAuth Scope Diff cover" width="100%" />

| Detail | Value |
| --- | --- |
| Area | delivery and infrastructure |
| Command | `oauth-scope-diff` |
| Example | `examples/sample.txt` |

## What would make me stop a review

| Stopper | Level | Why it matters |
| --- | --- | --- |
| `admin-scope` | high | administrative scope requested |
| `write-scope` | medium | write scope requested |
| `offline-access` | low | long-lived access requested |

## Run from a fresh clone

```bash
git clone https://github.com/mertefekurt/oauth-scope-diff.git
cd oauth-scope-diff
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
oauth-scope-diff examples/sample.txt
oauth-scope-diff examples/sample.txt --json
```
