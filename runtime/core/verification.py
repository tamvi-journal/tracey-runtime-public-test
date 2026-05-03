from runtime.contracts.enums import VERIFICATION_PASSED, VerificationStatus
from runtime.contracts.types import FinalResult, VerificationRecord


FORBIDDEN_COMPLETION_TERMS = (
    "done",
    "completed",
    "fixed",
    "sent",
    "created",
    "updated",
    "merged",
    "published",
)


def build_verification_record(
    *,
    intended_action: str,
    executed_action: str,
    observed_outcome: str,
    evidence_handles: list[str],
    verification_status: VerificationStatus,
    confidence: float,
    failure_reason: str,
) -> VerificationRecord:
    return {
        "intended_action": intended_action,
        "executed_action": executed_action,
        "observed_outcome": observed_outcome,
        "evidence_handles": evidence_handles,
        "verification_status": verification_status,
        "confidence": confidence,
        "failure_reason": failure_reason,
    }


def completion_claim_allowed(verification_record: VerificationRecord) -> bool:
    return verification_record["verification_status"] == VERIFICATION_PASSED


def finalize_mainbrain_result(
    *,
    mainbrain_text: str,
    verification_record: VerificationRecord,
) -> FinalResult:
    allowed = completion_claim_allowed(verification_record)
    final_text = mainbrain_text
    lowered = mainbrain_text.lower()

    if not allowed and any(term in lowered for term in FORBIDDEN_COMPLETION_TERMS):
        final_text = f"Attempted but not verified: {verification_record['observed_outcome']}."

    return {
        "speaker": "MainBrain",
        "final_text": final_text,
        "completion_claim_allowed": allowed,
        "verification_status": verification_record["verification_status"],
        "evidence_handles": verification_record["evidence_handles"],
    }
