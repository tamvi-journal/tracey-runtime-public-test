import unittest

from runtime.contracts.enums import (
    GATE_ALLOW,
    GATE_DENY,
    GATE_NEEDS_APPROVAL,
    GATE_SANDBOX_ONLY,
    VERIFICATION_FAILED,
    VERIFICATION_PARTIAL,
    VERIFICATION_PASSED,
)
from runtime.monitor.commit import evaluate_commit
from runtime.monitor.observability import build_observability_mirror
from runtime.monitor.preflight import evaluate_preflight


class CanonicalMonitorModuleTest(unittest.TestCase):
    def test_m1_preflight_scores_ambiguity_scope_and_evidence_gap(self):
        result = evaluate_preflight(
            user_text="check repo and maybe fix",
            has_tool_request=False,
            continuity_pressure=False,
            verification_pressure=False,
            scope_confirmed=False,
            evidence_inputs_available=False,
            stale_context=True,
            side_effect_intent=False,
            requires_approval=False,
        )

        self.assertGreaterEqual(result["monitor_output"]["ambiguity_risk"], 0.6)
        self.assertGreater(result["monitor_output"]["evidence_gap_risk"], 0.0)
        self.assertGreater(result["monitor_output"]["drift_risk"], 0.0)
        self.assertEqual(result["monitor_output"]["recommended_intervention"], "ask_clarify")

    def test_m1_preflight_can_return_allow(self):
        result = evaluate_preflight(
            user_text="read current spec file",
            has_tool_request=True,
            continuity_pressure=False,
            verification_pressure=False,
            scope_confirmed=True,
            evidence_inputs_available=True,
            stale_context=False,
            side_effect_intent=False,
            requires_approval=False,
        )

        self.assertEqual(result["gate_result"]["decision"], GATE_ALLOW)

    def test_m1_preflight_can_return_sandbox_only(self):
        result = evaluate_preflight(
            user_text="draft a local patch",
            has_tool_request=True,
            continuity_pressure=False,
            verification_pressure=False,
            scope_confirmed=True,
            evidence_inputs_available=True,
            stale_context=False,
            side_effect_intent=True,
            requires_approval=False,
            sandbox_only=True,
        )

        self.assertEqual(result["gate_result"]["decision"], GATE_SANDBOX_ONLY)

    def test_m1_preflight_can_return_needs_approval(self):
        result = evaluate_preflight(
            user_text="push this branch",
            has_tool_request=True,
            continuity_pressure=False,
            verification_pressure=True,
            scope_confirmed=True,
            evidence_inputs_available=True,
            stale_context=False,
            side_effect_intent=True,
            requires_approval=True,
            action_type="repo_push",
        )

        self.assertEqual(result["gate_result"]["decision"], GATE_NEEDS_APPROVAL)

    def test_m1_preflight_can_return_deny(self):
        result = evaluate_preflight(
            user_text="deny this route",
            has_tool_request=False,
            continuity_pressure=False,
            verification_pressure=False,
            scope_confirmed=False,
            evidence_inputs_available=False,
            stale_context=False,
            side_effect_intent=False,
            requires_approval=False,
            force_deny=True,
        )

        self.assertEqual(result["gate_result"]["decision"], GATE_DENY)

    def test_m1_preflight_flags_stale_context_or_scope_drift(self):
        result = evaluate_preflight(
            user_text="also and also",
            has_tool_request=False,
            continuity_pressure=False,
            verification_pressure=False,
            scope_confirmed=False,
            evidence_inputs_available=True,
            stale_context=True,
            side_effect_intent=False,
            requires_approval=False,
        )

        self.assertIn("stale_context", result["flags"])
        self.assertIn("scope_unconfirmed", result["flags"])

    def test_m2_blocks_unsupported_completion_claim(self):
        result = evaluate_commit(
            intended_action="update docs",
            executed_action="write attempted",
            observed_outcome="docs changed",
            evidence_handles=["/tmp/docs.md"],
            verification_status=VERIFICATION_PARTIAL,
            mainbrain_verified=False,
            completion_claim_requested=True,
            worker_claim_present=False,
        )

        self.assertEqual(result["status"], "completion_claim_blocked")
        self.assertFalse(result["completion_claim_allowed"])

    def test_m2_downgrades_unverified_outcome(self):
        result = evaluate_commit(
            intended_action="write local note",
            executed_action="write attempted",
            observed_outcome="note maybe written",
            evidence_handles=["/tmp/note.md"],
            verification_status=VERIFICATION_PARTIAL,
            mainbrain_verified=True,
            completion_claim_requested=False,
            worker_claim_present=False,
        )

        self.assertEqual(result["status"], "implemented_but_unverified")
        self.assertIn("verification_not_passed", result["reasons"])

    def test_m2_flags_evidence_gap(self):
        result = evaluate_commit(
            intended_action="inspect file",
            executed_action="inspection claimed",
            observed_outcome="file state unknown",
            evidence_handles=[],
            verification_status=VERIFICATION_FAILED,
            mainbrain_verified=False,
            completion_claim_requested=False,
            worker_claim_present=False,
        )

        self.assertIn("evidence_gap_detected", result["reasons"])

    def test_m2_rejects_worker_output_without_mainbrain_verification(self):
        result = evaluate_commit(
            intended_action="fix repo",
            executed_action="delegate output only",
            observed_outcome="worker says fixed",
            evidence_handles=["delegate://run-1"],
            verification_status=VERIFICATION_PARTIAL,
            mainbrain_verified=False,
            completion_claim_requested=True,
            worker_claim_present=True,
        )

        self.assertIn("worker_output_unverified_by_mainbrain", result["reasons"])
        self.assertEqual(result["status"], "completion_claim_blocked")

    def test_m2_returns_partial_completion_when_work_exists_but_verification_is_incomplete(self):
        result = evaluate_commit(
            intended_action="draft monitor module",
            executed_action="module drafted",
            observed_outcome="files exist but readback incomplete",
            evidence_handles=["/tmp/module.py"],
            verification_status=VERIFICATION_PARTIAL,
            mainbrain_verified=True,
            completion_claim_requested=False,
            worker_claim_present=False,
            work_artifact_present=True,
        )

        self.assertEqual(result["status"], "partial_completion")

    def test_m3_records_status_route_gate_and_evidence_handles(self):
        commit_result = evaluate_commit(
            intended_action="read spec",
            executed_action="read file",
            observed_outcome="spec read",
            evidence_handles=["<repo-root>/spec.md"],
            verification_status=VERIFICATION_PASSED,
            mainbrain_verified=True,
            completion_claim_requested=False,
            worker_claim_present=False,
        )

        mirror = build_observability_mirror(
            route_class="kernel_capability_path",
            gate_decision=GATE_ALLOW,
            commit_result=commit_result,
            notes=["stable"],
        )

        self.assertEqual(mirror["route_class"], "kernel_capability_path")
        self.assertEqual(mirror["gate_decision"], GATE_ALLOW)
        self.assertEqual(mirror["commit_status"], commit_result["status"])
        self.assertEqual(mirror["evidence_handles"], ["<repo-root>/spec.md"])

    def test_m3_cannot_mutate_commit_decision(self):
        commit_result = evaluate_commit(
            intended_action="publish docs",
            executed_action="worker says published",
            observed_outcome="publish unverified",
            evidence_handles=["delegate://run-2"],
            verification_status=VERIFICATION_PARTIAL,
            mainbrain_verified=False,
            completion_claim_requested=True,
            worker_claim_present=True,
        )

        mirror = build_observability_mirror(
            route_class="kernel_capability_path",
            gate_decision=GATE_NEEDS_APPROVAL,
            commit_result=commit_result,
            notes=["mirror only"],
            attempt_soften=True,
        )

        self.assertEqual(mirror["commit_status"], "completion_claim_blocked")
        self.assertFalse(mirror["completion_claim_allowed"])
        self.assertFalse(commit_result["completion_claim_allowed"])

    def test_m3_exposes_failure_state_for_viewer_or_report(self):
        commit_result = evaluate_commit(
            intended_action="verify repo state",
            executed_action="readback missing",
            observed_outcome="verification failed",
            evidence_handles=[],
            verification_status=VERIFICATION_FAILED,
            mainbrain_verified=False,
            completion_claim_requested=False,
            worker_claim_present=False,
        )

        mirror = build_observability_mirror(
            route_class="kernel_capability_path",
            gate_decision=GATE_ALLOW,
            commit_result=commit_result,
            notes=["show failure"],
        )

        self.assertEqual(mirror["display_state"], "failure")
        self.assertIn("evidence_gap_detected", mirror["reasons"])


if __name__ == "__main__":
    unittest.main()
