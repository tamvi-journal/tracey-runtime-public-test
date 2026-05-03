from runtime.contracts.enums import (
    ROUTE_DIRECT_HOST_CHAT,
    ROUTE_KERNEL_CAPABILITY_PATH,
    ROUTE_KERNEL_DIRECT_REASONING,
)
from runtime.contracts.types import MonitorOutput
from runtime.monitor.preflight import evaluate_preflight


CASUAL_MARKERS = ("thanks", "thank you", "hi", "hello", "ok", "okay", "❤️", "🙏")


def inspect_turn(user_text: str) -> MonitorOutput:
    result = evaluate_preflight(
        user_text=user_text,
        has_tool_request=False,
        continuity_pressure=False,
        verification_pressure=False,
        scope_confirmed=len(user_text.strip().split()) > 2,
        evidence_inputs_available=True,
        stale_context=False,
        side_effect_intent=False,
        requires_approval=False,
    )
    return result["monitor_output"]


def classify_turn_route(
    *,
    user_text: str,
    has_tool_request: bool,
    continuity_pressure: bool,
    verification_pressure: bool,
) -> dict[str, object]:
    lowered = user_text.strip().lower()
    is_casual = any(marker in lowered for marker in CASUAL_MARKERS) and not has_tool_request

    if is_casual and not continuity_pressure and not verification_pressure:
        return {"route": ROUTE_DIRECT_HOST_CHAT, "kernel_required": False, "reason": "casual_turn"}
    if has_tool_request:
        return {"route": ROUTE_KERNEL_CAPABILITY_PATH, "kernel_required": True, "reason": "tool_or_delegation_path"}
    if continuity_pressure or verification_pressure:
        return {"route": ROUTE_KERNEL_DIRECT_REASONING, "kernel_required": True, "reason": "continuity_or_verification_pressure"}
    return {"route": ROUTE_KERNEL_DIRECT_REASONING, "kernel_required": True, "reason": "structured_reasoning"}
