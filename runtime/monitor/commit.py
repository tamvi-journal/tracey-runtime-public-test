from __future__ import annotations

from runtime.contracts.enums import (
    MONITOR_STATUS_CLAIM_BLOCKED,
    MONITOR_STATUS_IMPLEMENTED_UNVERIFIED,
    MONITOR_STATUS_PARTIAL_COMPLETION,
    MONITOR_STATUS_VERIFIED_COMPLETE,
    VERIFICATION_PASSED,
    VerificationStatus,
)
from runtime.contracts.types import CommitEvaluation


def evaluate_commit(
    *,
    intended_action: str,
    executed_action: str,
    observed_outcome: str,
    evidence_handles: list[str],
    verification_status: VerificationStatus,
    mainbrain_verified: bool,
    completion_claim_requested: bool,
    worker_claim_present: bool,
    work_artifact_present: bool = False,
) -> CommitEvaluation:
    reasons: list[str] = []

    has_evidence = len(evidence_handles) > 0
    verification_passed = verification_status == VERIFICATION_PASSED

    if not has_evidence:
        reasons.append("evidence_gap_detected")
    if verification_status != VERIFICATION_PASSED:
        reasons.append("verification_not_passed")
    if worker_claim_present and not mainbrain_verified:
        reasons.append("worker_output_unverified_by_mainbrain")
    if completion_claim_requested and not verification_passed:
        reasons.append("completion_claim_without_verification")
    if completion_claim_requested and not mainbrain_verified:
        reasons.append("completion_claim_without_mainbrain_verification")

    completion_claim_allowed = verification_passed and mainbrain_verified and has_evidence and not worker_claim_present

    if completion_claim_requested and not completion_claim_allowed:
        status = MONITOR_STATUS_CLAIM_BLOCKED
    elif verification_passed and mainbrain_verified and has_evidence:
        status = MONITOR_STATUS_VERIFIED_COMPLETE
    elif work_artifact_present and verification_status != VERIFICATION_PASSED:
        status = MONITOR_STATUS_PARTIAL_COMPLETION
    else:
        status = MONITOR_STATUS_IMPLEMENTED_UNVERIFIED

    confidence = 1.0 if status == MONITOR_STATUS_VERIFIED_COMPLETE else 0.45
    if status == MONITOR_STATUS_PARTIAL_COMPLETION:
        confidence = 0.6
    if status == MONITOR_STATUS_CLAIM_BLOCKED:
        confidence = 0.25

    return {
        "status": status,
        "completion_claim_allowed": completion_claim_allowed,
        "reasons": reasons,
        "evidence_handles": list(evidence_handles),
        "verification_status": verification_status,
        "intended_action": intended_action,
        "executed_action": executed_action,
        "observed_outcome": observed_outcome,
        "confidence": confidence,
    }
