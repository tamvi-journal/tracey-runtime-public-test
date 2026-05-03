# Quickstart

## 1. Run tests
```bash
python3 runtime/run_tests.py
```

Expected result: the selected `runtime/tests/` suite passes.

## 2. Generate the task index
```bash
python3 runtime/operator_ux/generate_task_index.py
```

Expected result: `runtime/operator_ux/task_run_index.json` and `runtime/operator_ux/task_run_index.html` are regenerated.

## 3. Open the static viewer
Open these files directly in a browser:
- `runtime/operator_ux/home.html`
- `runtime/operator_ux/task_run_index.html`
- `runtime/operator_ux/status_legend.html`

## 4. What to report
Useful public feedback:
- install/run failures
- unclear naming or docs
- tests that appear to contradict the written boundary rules
- viewer states that are hard to interpret
