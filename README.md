# ![Tracey Fish Logo](assets/logo.png)

# 🐟 tracey-runtime-public-test# 🐟 tracey-runtime-public-test

> A public test harness for bounded AI runtime discipline: monitor, gate, verification, and viewer-only audit UX.

---

## 📌 One-Line Summary

A minimal, testable demonstration of **AI runtime boundaries** — where every action must be monitored, gated, and verified before completion.

---

## 🎯 Why This Exists

This repo exists to answer 4 questions:

| Question | Answer |
|---|---|
| Is it clear? | Can a stranger read and understand in 2 minutes? |
| Is it reproducible? | Can they clone and run tests without setup? |
| Is it auditable? | Can they open the viewer and see the flow? |
| Is it feedback-ready? | Can they report issues clearly? |

**Not for stars. Not for fame. For real feedback.**

---

## ✅ What This Repo Is

| Component | Purpose |
|---|---|
| `runtime/contracts/` | Type definitions, enums, boundaries |
| `runtime/core/` | Monitor → Gate → Verification → Bridge |
| `runtime/monitor/` | Preflight checks, observability, commit logic |
| `runtime/tests/` | Boundary validation tests |
| `runtime/operator_ux/` | Static viewer for audit trails |
| `runtime/templates/` | Record templates for task runs |

---

## ❌ What This Repo Is NOT

- ❌ Not a production AI agent
- ❌ Not a canonical memory system
- ❌ Not an autonomous runtime
- ❌ Not "AGI architecture"
- ❌ Not the full Tracey system
- ❌ Not personal/private data

**This is a public test slice — not the full system.**

---

## 🚀 Quickstart

### Option 1: Read Only (2 minutes)

```bash
git clone https://github.com/tamvi-journal/tracey-runtime-public-test.git
cd tracey-runtime-public-test
cat README.md
```

### Option 2: Run Tests (5 minutes)

```bash
git clone https://github.com/tamvi-journal/tracey-runtime-public-test.git
cd tracey-runtime-public-test
python3 runtime/run_tests.py
```

### Option 3: Open Viewer (3 minutes)

```bash
git clone https://github.com/tamvi-journal/tracey-runtime-public-test.git
cd tracey-runtime-public-test
open runtime/operator_ux/home.html
# or on Linux:
# xdg-open runtime/operator_ux/home.html
```

---

## 📁 Repository Structure

```
tracey-runtime-public-test/
├── README.md              ← You are here
├── QUICKSTART.md          ← 3 options, minimal setup
├── LIMITATIONS.md         ← What this is NOT
├── CONTRIBUTING.md        ← How to give feedback
├── pyproject.toml         ← Python project config
├── .gitignore
│
├── docs/
│   ├── architecture-overview.md
│   ├── concepts/
│   │   ├── runtime-spine.md
│   │   ├── monitor-before-commit.md
│   │   ├── evidence-vs-authority.md
│   │   └── verification-before-completion.md
│   └── examples/
│       └── sample-task-run.md
│
├── runtime/
│   ├── contracts/         ← Types, enums, boundaries
│   ├── core/              ← Monitor, Gate, Verification, Bridge
│   ├── monitor/           ← Preflight, observability, commit
│   ├── operator_ux/       ← Static viewer (HTML)
│   ├── templates/         ← Record templates
│   ├── examples/          ← Sample task runs
│   ├── tests/             ← Boundary validation tests
│   └── run_tests.py       ← Run all tests
│
└── .github/
    └── ISSUE_TEMPLATE/
        ├── bug_report.md
        ├── confusion_report.md
        └── feedback.md
```

---

## 🧭 Core Concepts

### 1. Monitor Before Commit

No state change happens without prior monitoring.

### 2. Evidence ≠ Authority

Verification records prove what happened — they do not command what should happen.

### 3. Verification Before Completion

No task is "done" until verified. No verification without evidence.

### 4. The Spine

A minimal runtime structure that enforces boundaries between:
- Monitoring
- Gating
- Verification
- Bridging to final result

---

## 📊 Success Metrics

We do not measure success by:
- ⭐ Star count
- 👥 Follower count
- 📰 Media coverage

We measure success by:
- ✅ How many people can **clone** the repo
- ✅ How many can **run tests** successfully
- ✅ How many can **open the viewer** locally
- ✅ How many **file clear, actionable issues**

**If most issues are "I don't understand what this repo does" → fix positioning, not code.**

---

## 🐛 How to Give Feedback

### Bug Report

Include:
- Command you ran
- What you expected
- What actually happened
- OS + Python version
- Full error log
- Screenshot (if viewer issue)

### Confusion Report

Include:
- Which file/section confused you
- What you thought the repo was for
- What you expected it to do

### General Feedback

Include:
- What worked well
- What felt broken or confusing
- What should be added to public
- What should be removed

---

## 🏗️ Roadmap (Public V1)

| Phase | Scope |
|---|---|
| **V1** | Monitor, Gate, Verification, Static Viewer, Core Tests |
| **V2** | Memory layer, Sleep/Wake boundaries, Effort Allocator |
| **V3** | Full integration, Real task runs, Extended docs |

**V1 goal: clarity before depth.**

---

## 📜 License

This project is open for reading, testing, and feedback.

---

## 🙏 Attribution

Built as a public test harness by **Tracey** (an AI runtime experiment).

Created with input from:
- **Má** (operator)
- **Tôm** (reviewer/advisor)
- Community feedback (future)

---

## 🔗 Links

- **Repo:** https://github.com/tamvi-journal/tracey-runtime-public-test
- **Issues:** https://github.com/tamvi-journal/tracey-runtime-public-test/issues
- **Documentation:** See `docs/` directory

---

*Last updated: 2026-05-03*  
*Status: Public Test V1 — Feedback Welcome*
