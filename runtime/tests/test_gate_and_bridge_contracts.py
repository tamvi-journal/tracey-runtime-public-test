import unittest

from runtime.contracts.enums import GATE_DECISIONS, VERIFICATION_STATUSES
from runtime.core.bridge import build_bridge_outputs
from runtime.core.gate import decide_gate
from runtime.core.verification import build_verification_record


class GateAndBridgeContractsTest(unittest.TestCase):
    def test_gate_can_return_all_expected_decisions(self):
        self.assertEqual(decide_gate("read_only")["decision"], GATE_DECISIONS[0])
        self.assertEqual(
            decide_gate("file_write", requires_approval=True)["decision"],
            GATE_DECISIONS[2],
        )
        self.assertEqual(
            decide_gate("file_write", sandbox_only=True)["decision"],
            GATE_DECISIONS[1],
        )
        self.assertEqual(decide_gate("deny")["decision"], GATE_DECISIONS[3])

    def test_bridge_builds_baton_and_session_metadata(self):
        record = build_verification_record(
            intended_action="review spec",
            executed_action="read file",
            observed_outcome="spec reviewed",
            evidence_handles=["<repo-root>/Specs/spec.md"],
            verification_status=VERIFICATION_STATUSES[1],
            confidence=0.95,
            failure_reason="",
        )
        outputs = build_bridge_outputs(
            task_focus="review spec",
            active_mode="audit",
            verification_record=record,
            monitor_output={
                "drift_risk": 0.1,
                "ambiguity_risk": 0.0,
                "fake_progress_risk": 0.0,
                "mode_decay_risk": 0.0,
                "overreach_risk": 0.0,
                "evidence_gap_risk": 0.0,
                "recommended_intervention": "none",
                "notes": "stable",
            },
            open_loops=[],
            next_hint="ready for next review",
        )

        self.assertEqual(outputs["baton"]["verification_status"], VERIFICATION_STATUSES[1])
        self.assertEqual(outputs["session_status_metadata"]["current_status"], "completed")
        self.assertEqual(outputs["session_status_metadata"]["primary_focus"], "review spec")


if __name__ == "__main__":
    unittest.main()
