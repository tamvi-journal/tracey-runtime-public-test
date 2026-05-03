# Architecture Overview

This public repo demonstrates a narrow runtime discipline pattern:

1. **route the turn**
2. **gate risky actions before side effects**
3. **treat tool or delegate output as evidence**
4. **verify outcomes before claiming completion**
5. **keep the UI viewer-only unless actor authority is explicitly designed and verified**

## Public slice contents
- `runtime/contracts/` — shared literals and typed structures
- `runtime/core/` — pure helpers for gate, monitor, verification, bridge, baton, evidence ledger
- `runtime/monitor/` — monitor-stage logic
- `runtime/tests/` — boundary-oriented tests
- `runtime/operator_ux/` — static local viewer artifacts
- `runtime/task_runs/` — sample audit records for viewer generation

## Why this slice exists
The purpose is not to claim a full AI system.
The purpose is to make a small, testable portion of the runtime discipline easy for outsiders to inspect and critique.
