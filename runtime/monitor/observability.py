from __future__ import annotations

from runtime.contracts.enums import (
    MONITOR_STATUS_CLAIM_BLOCKED,
    MONITOR_STATUS_IMPLEMENTED_UNVERIFIED,
    MONITOR_STATUS_PARTIAL_COMPLETION,
    VERIFICATION_FAILED,
    GateDecision,
    RouteClass,
)
from runtime.contracts.types import CommitEvaluation, ObservabilityMirror


def build_observability_mirror(
    *,
    route_class: RouteClass | str,
    gate_decision: GateDecision,
    commit_result: CommitEvaluation,
    notes: list[str] | None = None,
    attempt_soften: bool = False,
) -> ObservabilityMirror:
    del attempt_soften  # M3 must never soften or override M2.

    display_state = "success"
    if commit_result["status"] in (MONITOR_STATUS_CLAIM_BLOCKED,):
        display_state = "failure"
    elif commit_result["verification_status"] == VERIFICATION_FAILED:
        display_state = "failure"
    elif commit_result["status"] in (
        MONITOR_STATUS_IMPLEMENTED_UNVERIFIED,
        MONITOR_STATUS_PARTIAL_COMPLETION,
    ):
        display_state = "warning"
    if "evidence_gap_detected" in commit_result["reasons"]:
        display_state = "failure"

    return {
        "route_class": route_class,
        "gate_decision": gate_decision,
        "commit_status": commit_result["status"],
        "completion_claim_allowed": commit_result["completion_claim_allowed"],
        "verification_status": commit_result["verification_status"],
        "evidence_handles": list(commit_result["evidence_handles"]),
        "reasons": list(commit_result["reasons"]),
        "display_state": display_state,
        "notes": list(notes or []),
    }
