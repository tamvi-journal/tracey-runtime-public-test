from runtime.contracts.enums import OBSIDIAN_NON_AUTHORITATIVE, VERIFICATION_PASSED
from runtime.contracts.types import MirrorBridge, ObsidianVaultWrite, SessionStatusMetadata, VerificationRecord
from runtime.core.baton import build_baton
from runtime.core.verification import finalize_mainbrain_result


def build_mirror_bridge(monitor_output: dict[str, object]) -> MirrorBridge:
    risk_fields = {
        "drift": float(monitor_output.get("drift_risk", 0.0)),
        "ambiguity": float(monitor_output.get("ambiguity_risk", 0.0)),
        "fake_progress": float(monitor_output.get("fake_progress_risk", 0.0)),
        "mode_decay": float(monitor_output.get("mode_decay_risk", 0.0)),
        "overreach": float(monitor_output.get("overreach_risk", 0.0)),
        "evidence_gap": float(monitor_output.get("evidence_gap_risk", 0.0)),
    }
    primary_risk = max(risk_fields, key=risk_fields.get)
    risk_level = risk_fields[primary_risk]
    return {
        "primary_risk": primary_risk,
        "risk_level": risk_level,
        "recommended_intervention": str(monitor_output.get("recommended_intervention", "none")),
        "state_annotation": "expected change may not be verified yet" if primary_risk == "fake_progress" else str(monitor_output.get("notes", "")),
    }


def build_session_status_metadata(
    *,
    primary_focus: str,
    verification_record: VerificationRecord,
    mirror_bridge: MirrorBridge,
    open_loops: list[str],
    next_hint: str,
) -> SessionStatusMetadata:
    status = "completed" if verification_record["verification_status"] == VERIFICATION_PASSED else "active"
    return {
        "current_status": status,
        "primary_focus": primary_focus,
        "open_loops": open_loops,
        "last_verified_outcomes": [verification_record["observed_outcome"]] if verification_record["verification_status"] == VERIFICATION_PASSED else [],
        "recent_decisions": [],
        "relevant_entities": [],
        "active_skills": [],
        "risk_notes": [mirror_bridge["primary_risk"]],
        "next_hint": next_hint,
    }


def build_bridge_outputs(
    *,
    task_focus: str,
    active_mode: str,
    verification_record: VerificationRecord,
    monitor_output: dict[str, object],
    open_loops: list[str],
    next_hint: str,
) -> dict[str, object]:
    mirror_bridge = build_mirror_bridge(monitor_output)
    baton = build_baton(
        task_focus=task_focus,
        active_mode=active_mode,
        verification_record=verification_record,
        mirror_bridge=mirror_bridge,
        open_loops=open_loops,
        next_hint=next_hint,
    )
    session_status_metadata = build_session_status_metadata(
        primary_focus=task_focus,
        verification_record=verification_record,
        mirror_bridge=mirror_bridge,
        open_loops=open_loops,
        next_hint=next_hint,
    )
    return {
        "mirror_bridge": mirror_bridge,
        "baton": baton,
        "session_status_metadata": session_status_metadata,
    }


def build_obsidian_vault_write(
    *,
    vault_path: str,
    note_type: str,
    title: str,
    tags: list[str],
    summary: str,
    body_markdown: str,
    source_session_id: str,
    verification_status: str,
    canonical_status: str = OBSIDIAN_NON_AUTHORITATIVE,
) -> ObsidianVaultWrite:
    return {
        "vault_path": vault_path,
        "note_type": note_type,
        "title": title,
        "tags": tags,
        "summary": summary,
        "body_markdown": body_markdown,
        "source_session_id": source_session_id,
        "verification_status": verification_status,
        "canonical_status": canonical_status,
    }


def compose_final_result(
    *,
    mainbrain_text: str,
    verification_record: VerificationRecord,
    tool_outputs: list[dict[str, object]],
    delegate_outputs: list[dict[str, object]],
) -> dict[str, object]:
    final_result = finalize_mainbrain_result(
        mainbrain_text=mainbrain_text,
        verification_record=verification_record,
    )
    final_result["evidence_summary"] = {
        "tool_outputs": tool_outputs,
        "delegate_outputs": delegate_outputs,
    }
    return final_result
