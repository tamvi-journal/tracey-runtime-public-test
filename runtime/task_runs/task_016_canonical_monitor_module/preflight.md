# Preflight — Task 016 Canonical Monitor Module

Task ID: `task_016_canonical_monitor_module`

## Goal
Implement a canonical rule-based monitor module with M1 Preflight, M2 Commit, and M3 Observability Mirror while preserving `runtime/core/monitor.py` as a compatibility wrapper.

## Allowed scope
- create `runtime/monitor/` module files
- add Task 016 tests
- update contracts/enums if monitor result types need explicit shapes
- adapt `runtime/core/monitor.py` into compat wrapper
- make minimal shared gate changes only if required by deterministic monitor outputs
- create Task 016 audit records

## Forbidden scope
- no unrelated sleep/wake integration work
- no unrelated demo expansion
- no unrelated authority-gate expansion
- no autonomous runtime wiring
- no LLM-based monitor judgment
- no canonical promotion changes
- no breaking existing callers of `runtime/core/monitor.py`

## Required verification
- run `runtime/tests/test_monitor_module.py`
- run listed regression tests for gate, verification, delegate-output, and final-synthesis boundary
- write `verification_record.json` only after tests complete

## Acceptance focus
- M2 stricter than M3
- M3 never softens or overrides M2
- deterministic rule-based scoring only
