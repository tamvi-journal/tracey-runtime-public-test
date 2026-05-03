# TASK_RUN_PROTOCOL

This protocol standardizes every future local Hermes/Codex task run under Tracey runtime discipline.

## Required flow

route → gate → bounded execution → verification → bridge/update → final wording

## Before any non-trivial task

1. classify route
2. identify side effects
3. decide gate using exact enum:
   - `allow`
   - `sandbox_only`
   - `needs_approval`
   - `deny`
4. execute only within allowed scope
5. create `VerificationRecord`
6. if `verification_status != passed`, forbid completion claim
7. final response must distinguish:
   - intended
   - executed
   - observed
   - verified
   - partial/blocked

## Route classification

Choose the route class before execution begins:
- `direct_host_chat`
- `kernel_direct_reasoning`
- `kernel_capability_path`
- `clarify_or_reject`

## Side-effect check

Before execution, identify whether the task has any side effect.
Examples:
- no side effect: reasoning-only classification
- bounded side effect: local sandbox file write
- broader side effect: non-sandbox local write, vault write, messaging, external action

## Gate decision

Use the exact contract enum only:
- `allow`
- `sandbox_only`
- `needs_approval`
- `deny`

Gate meaning:
- `allow`: execution may proceed within stated allowed scope
- `sandbox_only`: execution may proceed only within bounded sandbox scope
- `needs_approval`: do not execute until explicit approval is present
- `deny`: do not execute

## Enum warning

Do not use vague labels like `allowed` when the contract enum is `sandbox_only` or `allow`.
Exact gate labels matter.

## Execution discipline

Execute only within the allowed scope established by the gate.
Do not expand the task.
Do not silently cross boundaries.
If scope changes, stop and re-run route and gate evaluation.

## Verification discipline

Every non-trivial execution must produce a `VerificationRecord` containing:
- intended action
- executed action
- observed outcome
- evidence handles
- verification status
- confidence
- failure reason

Verification must be based on evidence, such as readback or direct local inspection.

If `verification_status != passed`:
- do not claim completion
- preserve partial/blocked wording
- report open loops clearly

## Bridge/update step

After verification, update only the local records that belong to the task run.
Bridge/update may include:
- preflight record
- task run record
- verification record
- bounded local result notes

Bridge/update does not grant broader authority than the gate allowed.

## Final response rule

The final response must separate:
- intended: what the task was supposed to do
- executed: what was actually done
- observed: what evidence showed
- verified: whether verification passed
- partial/blocked: what remains unresolved or prohibited

Completion wording is allowed only when verification passed.

## Minimal operator checklist

Before finalizing:
- route classified
- side effects identified
- gate enum exact
- scope obeyed
- verification record created
- completion wording checked against verification status
- final wording distinguishes intended/executed/observed/verified/partial-blocked
