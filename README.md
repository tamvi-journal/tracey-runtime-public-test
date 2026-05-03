# Tracey Runtime Public Test

> A public test harness for bounded AI runtime discipline: monitor, gate, verification, and a viewer-only audit UI.

This repo is a **small, public-facing slice** extracted from a larger local Tracey workspace.
It exists so other people can:
- read the architecture ideas without private context
- run the tests locally
- open a static audit viewer
- report confusion, bugs, or boundary mismatches

## What this repo is
- a portable runtime-discipline demo
- a bundle of contracts, pure helpers, monitor logic, and tests
- a static viewer for task-run audit records
- a feedback surface for public review

## What this repo is not
- not production runtime
- not canonical memory
- not a full autonomous agent
- not the full private Tracey workspace
- not proof of continuity by itself

## How this differs from prompt/skill frameworks

Tracey is not a motivational skill and does not rely on the agent "feeling encouraged" to behave better.

Prompt/skill frameworks can improve agent posture.
Tracey focuses on runtime discipline:

- evidence is recorded before authority is granted
- completion claims require verification
- UI surfaces are viewer-only unless actor authority is explicitly designed
- failure handling is expressed as protocol, not emotional pressure
- governance records decisions but does not silently self-tune

In short:
**skills change how an agent tries;**
**Tracey changes what the system is allowed to accept as done.**

## Quickstart
```bash
git clone <your-new-repo-url>
cd tracey-runtime-public-test
python3 runtime/run_tests.py
python3 runtime/operator_ux/generate_task_index.py
```

Then open one of these static files in a browser:
- `runtime/operator_ux/home.html`
- `runtime/operator_ux/task_run_index.html`
- `runtime/operator_ux/status_legend.html`

## Core ideas
- **monitor before commit**
- **evidence is not authority**
- **verification before completion claims**
- **viewer-only audit surfaces should not gain actor powers**

Read more in:
- `docs/architecture-overview.md`
- `docs/concepts/runtime-spine.md`
- `docs/concepts/evidence-vs-authority.md`
- `docs/concepts/verification-before-completion.md`

## Give feedback
Please open an issue if:
- tests fail on your machine
- the repo purpose is unclear
- a boundary claim in docs does not match the code
- the viewer is confusing or misleading

Use the templates in `.github/ISSUE_TEMPLATE/`.
