import unittest

from runtime.contracts.enums import VERIFICATION_PASSED
from runtime.core.bridge import compose_final_result
from runtime.core.verification import build_verification_record


class MainBrainBoundaryTest(unittest.TestCase):
    def test_mainbrain_is_final_speaker(self):
        record = build_verification_record(
            intended_action="summarize findings",
            executed_action="read files",
            observed_outcome="summary drafted",
            evidence_handles=["<repo-root>/00_Index.md"],
            verification_status=VERIFICATION_PASSED,
            confidence=0.9,
            failure_reason="",
        )

        result = compose_final_result(
            mainbrain_text="MainBrain final answer.",
            verification_record=record,
            tool_outputs=[{"tool": "read_file", "output": "raw file text"}],
            delegate_outputs=[{"tool": "delegate", "output": "delegate claim"}],
        )

        self.assertEqual(result["speaker"], "MainBrain")
        self.assertEqual(result["final_text"], "MainBrain final answer.")
        self.assertEqual(result["verification_status"], VERIFICATION_PASSED)
        self.assertEqual(len(result["evidence_summary"]["tool_outputs"]), 1)
        self.assertEqual(len(result["evidence_summary"]["delegate_outputs"]), 1)


if __name__ == "__main__":
    unittest.main()
