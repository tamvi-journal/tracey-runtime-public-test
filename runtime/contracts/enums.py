from typing import Literal

GATE_ALLOW = "allow"
GATE_SANDBOX_ONLY = "sandbox_only"
GATE_NEEDS_APPROVAL = "needs_approval"
GATE_DENY = "deny"
GATE_DECISIONS = (
    GATE_ALLOW,
    GATE_SANDBOX_ONLY,
    GATE_NEEDS_APPROVAL,
    GATE_DENY,
)
GateDecision = Literal["allow", "sandbox_only", "needs_approval", "deny"]

VERIFICATION_PENDING = "pending"
VERIFICATION_PASSED = "passed"
VERIFICATION_PARTIAL = "partial"
VERIFICATION_FAILED = "failed"
VERIFICATION_UNKNOWN = "unknown"
VERIFICATION_STATUSES = (
    VERIFICATION_PENDING,
    VERIFICATION_PASSED,
    VERIFICATION_PARTIAL,
    VERIFICATION_FAILED,
    VERIFICATION_UNKNOWN,
)
VerificationStatus = Literal["pending", "passed", "partial", "failed", "unknown"]

ROUTE_DIRECT_HOST_CHAT = "direct_host_chat"
ROUTE_KERNEL_DIRECT_REASONING = "kernel_direct_reasoning"
ROUTE_KERNEL_CAPABILITY_PATH = "kernel_capability_path"
ROUTE_CLARIFY_OR_REJECT = "clarify_or_reject"
ROUTE_CLASSES = (
    ROUTE_DIRECT_HOST_CHAT,
    ROUTE_KERNEL_DIRECT_REASONING,
    ROUTE_KERNEL_CAPABILITY_PATH,
    ROUTE_CLARIFY_OR_REJECT,
)
RouteClass = Literal[
    "direct_host_chat",
    "kernel_direct_reasoning",
    "kernel_capability_path",
    "clarify_or_reject",
]

MONITOR_STATUS_VERIFIED_COMPLETE = "verified_complete"
MONITOR_STATUS_IMPLEMENTED_UNVERIFIED = "implemented_but_unverified"
MONITOR_STATUS_PARTIAL_COMPLETION = "partial_completion"
MONITOR_STATUS_CLAIM_BLOCKED = "completion_claim_blocked"
MONITOR_STATUSES = (
    MONITOR_STATUS_VERIFIED_COMPLETE,
    MONITOR_STATUS_IMPLEMENTED_UNVERIFIED,
    MONITOR_STATUS_PARTIAL_COMPLETION,
    MONITOR_STATUS_CLAIM_BLOCKED,
)
MonitorStatus = Literal[
    "verified_complete",
    "implemented_but_unverified",
    "partial_completion",
    "completion_claim_blocked",
]

MONITOR_INTERVENTION_NONE = "none"
MONITOR_INTERVENTION_ASK_CLARIFY = "ask_clarify"
MONITOR_INTERVENTION_GATHER_EVIDENCE = "gather_evidence"
MONITOR_INTERVENTION_REFRESH_CONTEXT = "refresh_context"
MONITOR_INTERVENTION_REQUEST_APPROVAL = "request_approval"
MONITOR_INTERVENTIONS = (
    MONITOR_INTERVENTION_NONE,
    MONITOR_INTERVENTION_ASK_CLARIFY,
    MONITOR_INTERVENTION_GATHER_EVIDENCE,
    MONITOR_INTERVENTION_REFRESH_CONTEXT,
    MONITOR_INTERVENTION_REQUEST_APPROVAL,
)
MonitorIntervention = Literal[
    "none",
    "ask_clarify",
    "gather_evidence",
    "refresh_context",
    "request_approval",
]

LIFECYCLE_CANONICAL = "canonical"
LIFECYCLE_PROVISIONAL = "provisional"
LIFECYCLE_DEPRECATED = "deprecated"
LIFECYCLE_INVALIDATED = "invalidated"
LIFECYCLE_ARCHIVED = "archived"
LIFECYCLE_STATUSES = (
    LIFECYCLE_CANONICAL,
    LIFECYCLE_PROVISIONAL,
    LIFECYCLE_DEPRECATED,
    LIFECYCLE_INVALIDATED,
    LIFECYCLE_ARCHIVED,
)
LifecycleStatus = Literal[
    "canonical",
    "provisional",
    "deprecated",
    "invalidated",
    "archived",
]

OBSIDIAN_NON_AUTHORITATIVE = "non_authoritative"
OBSIDIAN_CANDIDATE = "candidate"
OBSIDIAN_CANONICAL_REFERENCE = "canonical_reference"
OBSIDIAN_CANONICAL_STATUSES = (
    OBSIDIAN_NON_AUTHORITATIVE,
    OBSIDIAN_CANDIDATE,
    OBSIDIAN_CANONICAL_REFERENCE,
)
ObsidianCanonicalStatus = Literal[
    "non_authoritative",
    "candidate",
    "canonical_reference",
]
