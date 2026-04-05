from __future__ import annotations

import json
from pathlib import Path

from gpd.core.state import (
    _blank_session_payload,
    default_state_dict,
    load_state_json,
    save_state_json,
    save_state_markdown,
    state_load,
)


def test_save_state_json_does_not_backfill_canonical_continuation_from_session_only_fields(
    tmp_path: Path, state_project_factory
) -> None:
    cwd = state_project_factory(tmp_path)
    state = json.loads((cwd / "GPD" / "state.json").read_text(encoding="utf-8"))
    state["session"].update(
        {
            "last_date": "2026-04-01T12:00:00+00:00",
            "stopped_at": "Legacy stop",
            "resume_file": "legacy-session.md",
            "hostname": "legacy-host",
            "platform": "LegacyOS",
        }
    )

    save_state_json(cwd, state)

    stored = load_state_json(cwd)
    assert stored is not None
    assert stored["continuation"]["handoff"] == {
        "recorded_at": None,
        "stopped_at": None,
        "resume_file": None,
        "recorded_by": None,
        "last_result_id": None,
    }
    assert stored["continuation"]["machine"] == {
        "recorded_at": None,
        "hostname": None,
        "platform": None,
    }
    assert stored["session"] == _blank_session_payload()


def test_save_state_markdown_does_not_promote_session_edits_into_canonical_continuation(
    tmp_path: Path, state_project_factory
) -> None:
    cwd = state_project_factory(tmp_path)
    markdown_path = cwd / "GPD" / "STATE.md"
    edited_markdown = (
        markdown_path.read_text(encoding="utf-8")
        .replace("**Last session:** —", "**Last session:** 2026-04-01T12:00:00+00:00", 1)
        .replace("**Stopped at:** —", "**Stopped at:** Legacy stop", 1)
        .replace("**Resume file:** —", "**Resume file:** legacy-session.md", 1)
        .replace("**Hostname:** —", "**Hostname:** legacy-host", 1)
        .replace("**Platform:** —", "**Platform:** LegacyOS", 1)
    )

    stored = save_state_markdown(cwd, edited_markdown)
    rewritten_markdown = markdown_path.read_text(encoding="utf-8")

    assert stored["continuation"]["handoff"]["resume_file"] is None
    assert stored["continuation"]["machine"]["hostname"] is None
    assert stored["session"] == _blank_session_payload()
    assert "legacy-session.md" not in rewritten_markdown
    assert "**Resume file:** —" in rewritten_markdown
    assert "**Hostname:** —" in rewritten_markdown


def test_state_load_ignores_backup_only_session_values_when_canonical_continuation_is_blank(
    tmp_path: Path, state_project_factory
) -> None:
    cwd = state_project_factory(tmp_path)
    gpd_dir = cwd / "GPD"
    primary_path = gpd_dir / "state.json"
    backup_path = gpd_dir / "state.json.bak"

    backup_state = default_state_dict()
    backup_state["session"].update(
        {
            "last_date": "2026-04-01T12:00:00+00:00",
            "stopped_at": "Backup-only stop",
            "resume_file": "backup-only.md",
            "hostname": "backup-host",
            "platform": "BackupOS",
        }
    )
    backup_path.write_text(json.dumps(backup_state, indent=2) + "\n", encoding="utf-8")

    primary_state = default_state_dict()
    primary_state["session"] = "malformed"
    primary_path.write_text(json.dumps(primary_state, indent=2) + "\n", encoding="utf-8")

    result = state_load(cwd)

    assert result.state["continuation"]["handoff"]["resume_file"] is None
    assert result.state["continuation"]["machine"]["hostname"] is None
    assert result.state["session"] == _blank_session_payload()
