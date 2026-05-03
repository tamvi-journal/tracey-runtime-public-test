import unittest
from pathlib import Path


class PublicExamplesLoadTest(unittest.TestCase):
    def test_sample_task_runs_exist(self):
        repo_root = Path(__file__).resolve().parents[2]
        task_runs = repo_root / "runtime" / "task_runs"
        self.assertTrue((task_runs / "task_001_ux_target_map").exists())
        self.assertTrue((task_runs / "task_002_minimal_operator_ux").exists())
        self.assertTrue((task_runs / "task_016_canonical_monitor_module").exists())


if __name__ == "__main__":
    unittest.main()
