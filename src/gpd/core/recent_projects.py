"""Machine-local recent-project index helpers for cross-project recovery.

The recent-project index is advisory only. It lives outside any single project
under the resolved GPD data root and helps users find likely repos to reopen.
"""

from __future__ import annotations

import os
from pathlib import Path

from pydantic import AliasChoices, BaseModel, ConfigDict, Field, field_validator, model_validator

from gpd.core.constants import (
    ENV_DATA_DIR,
    HOME_DATA_DIR_NAME,
    RECENT_PROJECTS_DIR_NAME,
    RECENT_PROJECTS_INDEX_FILENAME,
)
from gpd.core.utils import atomic_write, file_lock, safe_read_file

__all__ = [
    "RecentProjectEntry",
    "RecentProjectIndex",
    "RecentProjectsError",
    "list_recent_projects",
    "load_recent_projects_index",
    "recent_projects_index_path",
    "recent_projects_root",
    "record_recent_project",
]


class RecentProjectsError(ValueError):
    """Raised when the recent-project advisory cache cannot be parsed."""


class RecentProjectEntry(BaseModel):
    """One machine-local recent-project record."""

    model_config = ConfigDict(frozen=True, extra="ignore")

    schema_version: int = Field(default=1, ge=1)
    project_root: str = Field(validation_alias=AliasChoices("project_root", "workspace_root", "cwd", "path"))
    last_session_at: str | None = None
    last_seen_at: str | None = None
    stopped_at: str | None = None
    resume_file: str | None = None
    resume_file_available: bool | None = None
    resume_file_reason: str | None = None
    hostname: str | None = None
    platform: str | None = None
    source_kind: str | None = None
    source_session_id: str | None = None
    source_segment_id: str | None = None
    source_transition_id: str | None = None
    source_event_id: str | None = None
    source_recorded_at: str | None = None
    recovery_phase: str | None = None
    recovery_plan: str | None = None
    resumable: bool = False
    available: bool = True
    availability_reason: str | None = None

    @field_validator(
        "last_session_at",
        "last_seen_at",
        "stopped_at",
        "resume_file",
        "resume_file_reason",
        "hostname",
        "platform",
        "source_kind",
        "source_session_id",
        "source_segment_id",
        "source_transition_id",
        "source_event_id",
        "source_recorded_at",
        "recovery_phase",
        "recovery_plan",
        "availability_reason",
        mode="before",
    )
    @classmethod
    def _normalize_optional_text(cls, value: object) -> str | None:
        return _normalize_recent_text(value)

    @field_validator("project_root", mode="before")
    @classmethod
    def _normalize_project_root(cls, value: object) -> str:
        normalized = _normalize_recent_text(value)
        if normalized is None:
            raise ValueError("project_root is required")
        return Path(normalized).expanduser().resolve(strict=False).as_posix()


class RecentProjectIndex(BaseModel):
    """Persisted recent-project advisory index."""

    model_config = ConfigDict(frozen=True, extra="ignore")

    rows: list[RecentProjectEntry] = Field(default_factory=list)

    @model_validator(mode="before")
    @classmethod
    def _normalize_payload(cls, value: object) -> object:
        if value is None:
            return {"rows": []}
        if isinstance(value, dict) and not value:
            return {"rows": []}
        return {"rows": _extract_recent_project_rows(value)}


def recent_projects_root(explicit_data_dir: Path | None = None) -> Path:
    """Resolve the machine-local recent-project root.

    Precedence: explicit data dir > ``GPD_DATA_DIR`` env > ``~/.gpd/recent-projects``.
    """
    if explicit_data_dir is not None:
        return explicit_data_dir.expanduser() / RECENT_PROJECTS_DIR_NAME

    data_dir = os.environ.get(ENV_DATA_DIR, "").strip()
    if data_dir:
        return Path(data_dir).expanduser() / RECENT_PROJECTS_DIR_NAME
    return Path.home() / HOME_DATA_DIR_NAME / RECENT_PROJECTS_DIR_NAME


def recent_projects_index_path(data_root: Path | None = None) -> Path:
    """Return the index.json path for the recent-project cache."""
    base = recent_projects_root(data_root)
    return base / RECENT_PROJECTS_INDEX_FILENAME


def _sort_rows(rows: list[RecentProjectEntry]) -> list[RecentProjectEntry]:
    return sorted(
        rows,
        key=lambda row: (_recent_project_sort_stamp(row), row.project_root),
        reverse=True,
    )


def _dedupe_rows(rows: list[RecentProjectEntry]) -> list[RecentProjectEntry]:
    unique_rows: list[RecentProjectEntry] = []
    seen_roots: set[str] = set()
    for row in rows:
        if row.project_root in seen_roots:
            continue
        seen_roots.add(row.project_root)
        unique_rows.append(row)
    return unique_rows


def _recent_project_sort_stamp(row: RecentProjectEntry) -> str:
    return row.last_session_at or row.last_seen_at or row.source_recorded_at or ""


def _availability_for(project_root: str) -> tuple[bool, str | None]:
    root = Path(project_root).expanduser()
    if not root.exists():
        return False, "project root missing"
    return root.is_dir(), None if root.is_dir() else "project root is not a directory"


def _resume_file_availability(project_root: str, resume_file: str | None) -> tuple[bool | None, str | None]:
    if not isinstance(resume_file, str) or not resume_file.strip():
        return None, None

    root = Path(project_root).expanduser()
    if not root.exists() or not root.is_dir():
        return None, None

    resolved_root = root.resolve(strict=False)
    candidate = Path(resume_file).expanduser()
    if candidate.is_absolute():
        resolved_target = candidate.resolve(strict=False)
    else:
        resolved_target = (root / candidate).resolve(strict=False)

    try:
        resolved_target.relative_to(resolved_root)
    except ValueError:
        return False, "resume file outside project root"

    if not resolved_target.exists():
        return False, "resume file missing"
    if not resolved_target.is_file():
        return False, "resume file is not a file"
    return True, None


def _normalize_recent_text(value: object) -> str | None:
    if isinstance(value, Path):
        value = value.as_posix()
    elif not isinstance(value, str):
        return None
    stripped = value.strip()
    if not stripped or stripped in {"—", "[Not set]"} or stripped.casefold() in {"none", "null"}:
        return None
    return stripped


def _extract_recent_project_rows(value: object) -> list[object]:
    if isinstance(value, list):
        return value
    if not isinstance(value, dict):
        raise ValueError("recent-project index must be a mapping or list of rows")

    for key in ("rows", "projects"):
        if key in value:
            return _extract_recent_project_rows(value[key])

    if any(key in value for key in ("project_root", "workspace_root", "cwd", "path")):
        return [value]

    raise ValueError("recent-project index payload does not contain rows")


def _session_text(session_data: dict[str, object], *keys: str) -> str | None:
    for key in keys:
        if key in session_data:
            return _normalize_recent_text(session_data.get(key))
    return None


def _updated_text(
    session_data: dict[str, object],
    existing_value: str | None,
    *keys: str,
) -> str | None:
    updated = _session_text(session_data, *keys)
    return updated if updated is not None or any(key in session_data for key in keys) else existing_value


def _annotate_availability(entry: RecentProjectEntry) -> RecentProjectEntry:
    available, reason = _availability_for(entry.project_root)
    resume_file_available, resume_file_reason = _resume_file_availability(entry.project_root, entry.resume_file)
    return entry.model_copy(
        update={
            "available": available,
            "availability_reason": reason,
            "resume_file_available": resume_file_available,
            "resume_file_reason": resume_file_reason,
            "resumable": bool(entry.resume_file) and available and resume_file_available is True,
        }
    )


def load_recent_projects_index(data_root: Path | None = None) -> RecentProjectIndex:
    index_path = recent_projects_index_path(data_root)
    content = safe_read_file(index_path)
    if content is None:
        return RecentProjectIndex()
    try:
        index = RecentProjectIndex.model_validate_json(content)
    except ValueError as exc:
        raise RecentProjectsError(f"Malformed recent-project index at {index_path}: {exc}") from exc
    return index.model_copy(update={"rows": [_annotate_availability(row) for row in _sort_rows(list(index.rows))]})


def _save_index(data_root: Path | None, index: RecentProjectIndex) -> None:
    index_path = recent_projects_index_path(data_root)
    with file_lock(index_path):
        atomic_write(index_path, index.model_dump_json(indent=2) + "\n")


def record_recent_project(
    project_root: Path,
    *,
    session_data: dict[str, object],
    store_root: Path | None = None,
) -> RecentProjectEntry:
    """Insert or update one recent-project row."""
    resolved_root = project_root.expanduser().resolve(strict=False)
    data_root = store_root
    current = load_recent_projects_index(data_root)
    existing = next((row for row in current.rows if row.project_root == resolved_root.as_posix()), None)
    last_session_at = _updated_text(session_data, existing.last_session_at if existing is not None else None, "last_date", "last_session_at")
    last_seen_at = _updated_text(
        session_data,
        existing.last_seen_at if existing is not None else last_session_at,
        "last_seen_at",
        "last_date",
        "last_session_at",
    )
    normalized_resume_file = _updated_text(session_data, existing.resume_file if existing is not None else None, "resume_file")
    normalized_hostname = _updated_text(session_data, existing.hostname if existing is not None else None, "hostname")
    normalized_platform = _updated_text(session_data, existing.platform if existing is not None else None, "platform")
    source_kind = _updated_text(session_data, existing.source_kind if existing is not None else None, "source_kind", "provenance_kind")
    source_session_id = _updated_text(
        session_data,
        existing.source_session_id if existing is not None else None,
        "source_session_id",
        "session_id",
    )
    source_segment_id = _updated_text(
        session_data,
        existing.source_segment_id if existing is not None else None,
        "source_segment_id",
        "segment_id",
    )
    source_transition_id = _updated_text(
        session_data,
        existing.source_transition_id if existing is not None else None,
        "source_transition_id",
        "transition_id",
    )
    source_event_id = _updated_text(
        session_data,
        existing.source_event_id if existing is not None else None,
        "source_event_id",
        "event_id",
    )
    source_recorded_at = _updated_text(
        session_data,
        existing.source_recorded_at if existing is not None else None,
        "source_recorded_at",
        "recorded_at",
        "timestamp",
    )
    recovery_phase = _updated_text(
        session_data,
        existing.recovery_phase if existing is not None else None,
        "recovery_phase",
        "phase",
    )
    recovery_plan = _updated_text(
        session_data,
        existing.recovery_plan if existing is not None else None,
        "recovery_plan",
        "plan",
    )
    updated_entry = RecentProjectEntry(
        project_root=resolved_root.as_posix(),
        last_session_at=last_session_at,
        last_seen_at=last_seen_at,
        stopped_at=_updated_text(session_data, existing.stopped_at if existing is not None else None, "stopped_at"),
        resume_file=normalized_resume_file,
        hostname=normalized_hostname,
        platform=normalized_platform,
        source_kind=source_kind,
        source_session_id=source_session_id,
        source_segment_id=source_segment_id,
        source_transition_id=source_transition_id,
        source_event_id=source_event_id,
        source_recorded_at=source_recorded_at,
        recovery_phase=recovery_phase,
        recovery_plan=recovery_plan,
    )

    rows: list[RecentProjectEntry] = []
    replaced = False
    for current_row in current.rows:
        if current_row.project_root == updated_entry.project_root:
            rows.append(updated_entry)
            replaced = True
        else:
            rows.append(current_row)
    if not replaced:
        rows.append(updated_entry)

    _save_index(data_root, RecentProjectIndex(rows=_dedupe_rows(_sort_rows(rows))))
    return _annotate_availability(updated_entry)


def list_recent_projects(store_root: Path | None = None, *, last: int | None = None) -> list[RecentProjectEntry]:
    """Return recent-project rows sorted newest-first with availability annotations."""
    current = load_recent_projects_index(store_root)
    rows = [_annotate_availability(entry) for entry in _dedupe_rows(_sort_rows(list(current.rows)))]
    if last is not None and last > 0:
        rows = rows[:last]
    return rows
