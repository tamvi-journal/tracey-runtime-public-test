We’re testing a small public slice of Tracey: a bounded AI runtime-discipline harness.

It is not a production agent, not canonical memory, and not an autonomy claim.

The repo focuses on one question:
How do we prevent AI/tool/delegate output from being treated as completion before verification?

Core ideas:
- monitor before commit
- evidence is not authority
- verification before completion claims
- viewer-only audit UI should not gain actor powers

Looking for developer feedback on:
- boundary mismatches
- unclear architecture docs
- missing tests
- confusing viewer behavior
- places where “done” could be claimed too early

Positioning:
a runtime-discipline harness for evidence, verification, and boundary hygiene in AI-assisted work.
