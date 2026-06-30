from __future__ import annotations

from oauth_scope_diff.models import Rule

PROJECT_NAME = 'oauth-scope-diff'
SUMMARY = 'Detect OAuth scope creep in app manifest changes.'
SAMPLE_RISK = 'added scope admin:write offline_access users:read billing:write'
SAMPLE_CLEAN = 'added scope profile:read email:read'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "endpoint", "service", "job", "route", "event")

RULES = (
    Rule(
        code='admin-scope',
        severity='high',
        pattern='\\b(admin|owner|root)[\\w:-]*\\b',
        message='administrative scope requested',
        recommendation='Require security review and explicit business justification.',
    ),
    Rule(
        code='write-scope',
        severity='medium',
        pattern='\\b[\\w:-]*:write\\b',
        message='write scope requested',
        recommendation='Confirm least privilege and limit the token audience.',
    ),
    Rule(
        code='offline-access',
        severity='low',
        pattern='\\boffline_access\\b',
        message='long-lived access requested',
        recommendation='Document refresh-token storage and rotation controls.',
    ),
)
