from runtime.contracts.enums import VERIFICATION_UNKNOWN, VerificationStatus
from runtime.contracts.types import EvidenceLedgerEntry


def create_evidence_entry(
    *,
    tool: str,
    purpose: str,
    evidence_handle: str,
    verification_status: VerificationStatus,
) -> EvidenceLedgerEntry:
    return {
        "tool": tool,
        "purpose": purpose,
        "result_type": "evidence",
        "evidence_handle": evidence_handle,
        "verification_status": verification_status,
    }


def record_delegate_claim(*, claim: str, evidence_handle: str) -> EvidenceLedgerEntry:
    purpose = f"delegate_claim:{claim}"
    return create_evidence_entry(
        tool="delegate",
        purpose=purpose,
        evidence_handle=evidence_handle,
        verification_status=VERIFICATION_UNKNOWN,
    )
