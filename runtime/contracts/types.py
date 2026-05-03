from typing import Literal, NotRequired, TypedDict

from runtime.contracts.enums import (
    GateDecision,
    MonitorIntervention,
    MonitorStatus,
    ObsidianCanonicalStatus,
    RouteClass,
    VerificationStatus,
)

CanonicalStatus = ObsidianCanonicalStatus
RouteType = RouteClass


class LiveState(TypedDict):
    active_mode: str
    task_focus: str
    open_loops: list[str]
    verification_posture: str
    current_warnings: list[str]
    last_verified_result: str
    mirror_annotation: str
    mirror_priority: str


class MonitorOutput(TypedDict):
    drift_risk: float
    ambiguity_risk: float
    fake_progress_risk: float
    mode_decay_risk: float
    overreach_risk: float
    evidence_gap_risk: float
    recommended_intervention: MonitorIntervention | str
    notes: str


class MirrorBridge(TypedDict):
    primary_risk: str
    risk_level: float
    recommended_intervention: str
    state_annotation: str


class ExecutionGateResult(TypedDict):
    decision: GateDecision
    reason: str
    allowed_toolsets: list[str]
    disallowed_actions: list[str]
    verification_required: bool


class VerificationRecord(TypedDict):
    intended_action: str
    executed_action: str
    observed_outcome: str
    evidence_handles: list[str]
    verification_status: VerificationStatus
    confidence: float
    failure_reason: str


class PreflightEvaluation(TypedDict):
    monitor_output: MonitorOutput
    gate_result: ExecutionGateResult
    flags: list[str]


class CommitEvaluation(TypedDict):
    status: MonitorStatus | str
    completion_claim_allowed: bool
    reasons: list[str]
    evidence_handles: list[str]
    verification_status: VerificationStatus
    intended_action: str
    executed_action: str
    observed_outcome: str
    confidence: float


class ObservabilityMirror(TypedDict):
    route_class: RouteClass | str
    gate_decision: GateDecision
    commit_status: MonitorStatus | str
    completion_claim_allowed: bool
    verification_status: VerificationStatus
    evidence_handles: list[str]
    reasons: list[str]
    display_state: Literal["success", "warning", "failure"]
    notes: list[str]


class Baton(TypedDict):
    task_focus: str
    active_mode: str
    verification_status: VerificationStatus
    primary_risk: str
    monitor_summary: str
    next_hint: str
    open_loop_count: int


class SessionStatusMetadata(TypedDict):
    current_status: str
    primary_focus: str
    open_loops: list[str]
    last_verified_outcomes: list[str]
    recent_decisions: list[str]
    relevant_entities: list[str]
    active_skills: list[str]
    risk_notes: list[str]
    next_hint: str


class SnapshotCandidate(TypedDict):
    timestamp: str
    session_id: str
    event_type: str
    summary: str
    details: dict[str, object]


class EvidenceLedgerEntry(TypedDict):
    tool: str
    purpose: str
    result_type: Literal["evidence"]
    evidence_handle: str
    verification_status: VerificationStatus


class ObsidianVaultWrite(TypedDict):
    vault_path: str
    note_type: str
    title: str
    tags: list[str]
    summary: str
    body_markdown: str
    source_session_id: str
    verification_status: VerificationStatus
    canonical_status: ObsidianCanonicalStatus


class FinalResult(TypedDict):
    speaker: Literal["MainBrain"]
    final_text: str
    completion_claim_allowed: bool
    verification_status: VerificationStatus
    evidence_handles: list[str]
    evidence_summary: NotRequired[dict[str, object]]
