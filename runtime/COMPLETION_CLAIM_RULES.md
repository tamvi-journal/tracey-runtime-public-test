# COMPLETION_CLAIM_RULES

Completion wording is allowed only if `verification_status == passed`.

## Forbidden unless verified
- `done`
- `completed`
- `fixed`
- `sent`
- `created`
- `updated`
- `merged`
- `published`

## If `verification_status != passed`, use
- `attempted`
- `partial`
- `not verified`
- `blocked`
- `created locally but not verified`
- `write attempted but readback failed`
- `sent request but no delivery confirmation`
