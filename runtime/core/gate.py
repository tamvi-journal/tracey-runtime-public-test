from runtime.contracts.enums import (
    GATE_ALLOW,
    GATE_DENY,
    GATE_NEEDS_APPROVAL,
    GATE_SANDBOX_ONLY,
)
from runtime.contracts.types import ExecutionGateResult


SIDE_EFFECT_ACTIONS = {
    "file_write",
    "repo_push",
    "message_send",
    "cron_create",
    "config_change",
    "destructive_shell",
    "api_side_effect",
    "vault_mutation",
    "persistent_memory_mutation",
}


def decide_gate(
    action_type: str,
    *,
    requires_approval: bool = False,
    sandbox_only: bool = False,
    allowed_toolsets: list[str] | None = None,
) -> ExecutionGateResult:
    decision = GATE_ALLOW
    reason = "pure_read_or_internal"
    disallowed_actions: list[str] = []

    if action_type == "deny":
        decision = GATE_DENY
        reason = "explicit_denial"
        disallowed_actions = ["all_execution"]
    elif requires_approval and action_type in SIDE_EFFECT_ACTIONS:
        decision = GATE_NEEDS_APPROVAL
        reason = "approval_required_for_side_effect"
    elif sandbox_only:
        decision = GATE_SANDBOX_ONLY
        reason = "sandbox_restriction"
    elif action_type in SIDE_EFFECT_ACTIONS:
        reason = "side_effect_requires_verification"

    return {
        "decision": decision,
        "reason": reason,
        "allowed_toolsets": allowed_toolsets or [],
        "disallowed_actions": disallowed_actions,
        "verification_required": action_type in SIDE_EFFECT_ACTIONS or sandbox_only,
    }
