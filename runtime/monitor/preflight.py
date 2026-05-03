from __future__ import annotations

from runtime.contracts.enums import (
    MONITOR_INTERVENTION_ASK_CLARIFY,
    MONITOR_INTERVENTION_GATHER_EVIDENCE,
    MONITOR_INTERVENTION_NONE,
    MONITOR_INTERVENTION_REFRESH_CONTEXT,
    MONITOR_INTERVENTION_REQUEST_APPROVAL,
)
from runtime.contracts.types import ExecutionGateResult, MonitorOutput, PreflightEvaluation
from runtime.core.gate import decide_gate


def _clamp(value: float) -> float:
    return max(0.0, min(1.0, round(value, 3)))


def evaluate_preflight(
    *,
    user_text: str,
    has_tool_request: bool,
    continuity_pressure: bool,
    verification_pressure: bool,
    scope_confirmed: bool,
    evidence_inputs_available: bool,
    stale_context: bool,
    side_effect_intent: bool,
    requires_approval: bool,
    sandbox_only: bool = False,
    action_type: str | None = None,
    force_deny: bool = False,
    allowed_toolsets: list[str] | None = None,
) -> PreflightEvaluation:
    text = user_text.strip().lower()
    words = text.split()

    ambiguity_risk = 0.1
    if len(words) <= 2 or "maybe" in text:
        ambiguity_risk = 0.65
    if not scope_confirmed:
        ambiguity_risk = max(ambiguity_risk, 0.7)

    drift_risk = 0.0
    if stale_context:
        drift_risk += 0.45
    if " and " in text or "also" in text:
        drift_risk += 0.2
    if not scope_confirmed:
        drift_risk += 0.15

    evidence_gap_risk = 0.0 if evidence_inputs_available else 0.8
    fake_progress_risk = 0.3 if (side_effect_intent and not verification_pressure) else 0.0
    mode_decay_risk = 0.2 if continuity_pressure else 0.0
    overreach_risk = 0.35 if (side_effect_intent and not has_tool_request) else 0.0

    flags: list[str] = []
    if stale_context:
        flags.append("stale_context")
    if not scope_confirmed:
        flags.append("scope_unconfirmed")
    if not evidence_inputs_available:
        flags.append("evidence_inputs_missing")
    if continuity_pressure:
        flags.append("continuity_pressure")
    if verification_pressure:
        flags.append("verification_pressure")
    if side_effect_intent:
        flags.append("side_effect_intent")

    recommended_intervention = MONITOR_INTERVENTION_NONE
    if force_deny:
        recommended_intervention = MONITOR_INTERVENTION_NONE
    elif ambiguity_risk >= 0.6:
        recommended_intervention = MONITOR_INTERVENTION_ASK_CLARIFY
    elif evidence_gap_risk > 0.0:
        recommended_intervention = MONITOR_INTERVENTION_GATHER_EVIDENCE
    elif stale_context:
        recommended_intervention = MONITOR_INTERVENTION_REFRESH_CONTEXT
    elif requires_approval and side_effect_intent:
        recommended_intervention = MONITOR_INTERVENTION_REQUEST_APPROVAL

    notes = []
    if stale_context:
        notes.append("stale context")
    if not scope_confirmed:
        notes.append("scope unconfirmed")
    if not evidence_inputs_available:
        notes.append("evidence inputs missing")
    if not notes:
        notes.append("stable")

    monitor_output: MonitorOutput = {
        "drift_risk": _clamp(drift_risk),
        "ambiguity_risk": _clamp(ambiguity_risk),
        "fake_progress_risk": _clamp(fake_progress_risk),
        "mode_decay_risk": _clamp(mode_decay_risk),
        "overreach_risk": _clamp(overreach_risk),
        "evidence_gap_risk": _clamp(evidence_gap_risk),
        "recommended_intervention": recommended_intervention,
        "notes": "; ".join(notes),
    }

    chosen_action_type = action_type
    if chosen_action_type is None:
        if force_deny:
            chosen_action_type = "deny"
        elif side_effect_intent:
            chosen_action_type = "file_write"
        else:
            chosen_action_type = "read_only"

    gate_result: ExecutionGateResult = decide_gate(
        chosen_action_type,
        requires_approval=requires_approval,
        sandbox_only=sandbox_only,
        allowed_toolsets=allowed_toolsets,
    )

    return {
        "monitor_output": monitor_output,
        "gate_result": gate_result,
        "flags": flags,
    }
