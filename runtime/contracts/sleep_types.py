from typing import Literal, NotRequired, TypedDict

ResumeDecision = Literal[
    "resume_full",
    "resume_with_refresh",
    "resume_with_clarification",
    "resume_read_only",
    "restart_required",
]

WakeCheckStatus = Literal["pass", "warn", "fail"]


class AgentIdentity(TypedDict):
    agent_name: str
    agent_role: str
    lineage: str
    version: str


class AxisState(TypedDict):
    truth_before_fluency: bool
    axis_before_capability: bool
    mainbrain_speaks_last: bool
    boundary_before_mirroring: bool


class LiveState(TypedDict):
    coherence: float
    uncertainty: float
    level: str
    verification_status: str
    current_focus: str


class DeltaState(TypedDict):
    changed_since_last_snapshot: list[str]
    last_success: str | None
    last_failure: str | None
    last_blocker: str | None
    next_safe_action: str


class MemoryHandoff(TypedDict):
    semantic_memory_candidates: list[str]
    state_memory_handles: list[str]
    canonical_memory_refs: list[str]
    notes: str


class WakeRequirements(TypedDict):
    refresh_stale_handles: bool
    require_identity_match: bool
    require_task_scope_match: bool
    require_gate_compatibility: bool
    require_verification_refresh: bool


class SleepSnapshot(TypedDict):
    snapshot_id: str
    created_at: str
    agent_identity: AgentIdentity
    task_id: str
    route_class: str
    gate_decision: str
    active_mode: str
    axis_state: AxisState
    live_state: LiveState
    delta_state: DeltaState
    open_loops: list[str]
    evidence_handles: list[str]
    stale_sensitive_handles: list[str]
    memory_handoff: MemoryHandoff
    wake_requirements: WakeRequirements
    forbidden_claims: list[str]
    metadata: NotRequired[dict[str, object]]


class WakeSanityResult(TypedDict):
    resume_decision: ResumeDecision
    status: WakeCheckStatus
    reasons: list[str]
    required_refreshes: list[str]
    held_claims: list[str]
    confidence: float
