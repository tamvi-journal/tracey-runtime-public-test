import unittest

from runtime.contracts.enums import VERIFICATION_PASSED, VERIFICATION_UNKNOWN
from runtime.core.evidence_ledger import create_evidence_entry, record_delegate_claim
from runtime.core.verification import build_verification_record


class DelegateEvidenceOnlyTest(unittest.TestCase):
    def test_delegate_output_remains_evidence_until_verified(self):
        entry = record_delegate_claim(
            claim="subagent says repo was fixed",
            evidence_handle="delegate://run-123",
        )
        record = build_verification_record(
            intended_action="fix repo",
            executed_action="delegate review",
            observed_outcome="delegate claims fix",
            evidence_handles=[entry["evidence_handle"]],
            verification_status=VERIFICATION_UNKNOWN,
            confidence=0.2,
            failure_reason="no readback verification",
        )

        self.assertEqual(entry["result_type"], "evidence")
        self.assertEqual(entry["tool"], "delegate")
        self.assertNotIn("reasoning", entry)
        self.assertEqual(record["verification_status"], VERIFICATION_UNKNOWN)

    def test_evidence_entry_stores_handle_not_reasoning(self):
        entry = create_evidence_entry(
            tool="read_file",
            purpose="verify file write",
            evidence_handle="<repo-root>/spec.md",
            verification_status=VERIFICATION_PASSED,
        )

        self.assertEqual(entry["evidence_handle"], "<repo-root>/spec.md")
        self.assertNotIn("chain_of_thought", entry)
        self.assertNotIn("full_transcript", entry)


if __name__ == "__main__":
    unittest.main()
