from runtime.contracts.types import Baton, MirrorBridge, VerificationRecord


def build_baton(
    *,
    task_focus: str,
    active_mode: str,
    verification_record: VerificationRecord,
    mirror_bridge: MirrorBridge,
    open_loops: list[str],
    next_hint: str,
) -> Baton:
    return {
        "task_focus": task_focus,
        "active_mode": active_mode,
        "verification_status": verification_record["verification_status"],
        "primary_risk": mirror_bridge["primary_risk"],
        "monitor_summary": mirror_bridge["state_annotation"],
        "next_hint": next_hint,
        "open_loop_count": len(open_loops),
    }
