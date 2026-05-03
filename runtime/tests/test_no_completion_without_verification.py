import unittest

from runtime.contracts.enums import VERIFICATION_PARTIAL
from runtime.core.verification import build_verification_record, finalize_mainbrain_result


class NoCompletionWithoutVerificationTest(unittest.TestCase):
    def test_completion_wording_is_blocked_when_verification_not_passed(self):
        record = build_verification_record(
            intended_action="write spec note",
            executed_action="write attempted",
            observed_outcome="file write attempted",
            evidence_handles=["/tmp/spec.md"],
            verification_status=VERIFICATION_PARTIAL,
            confidence=0.4,
            failure_reason="readback missing",
        )

        result = finalize_mainbrain_result(
            mainbrain_text="Done. Spec updated and published.",
            verification_record=record,
        )

        self.assertFalse(result["completion_claim_allowed"])
        self.assertEqual(result["verification_status"], VERIFICATION_PARTIAL)
        self.assertNotIn("done", result["final_text"].lower())
        self.assertNotIn("published", result["final_text"].lower())
        self.assertIn("not verified", result["final_text"].lower())


if __name__ == "__main__":
    unittest.main()
