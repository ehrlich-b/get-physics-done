"""Shared update-cache resolution for hook surfaces."""

from __future__ import annotations

from collections.abc import Callable
import json
from pathlib import Path

import gpd.hooks.install_context as hook_layout
from gpd.core.observability import resolve_project_root

DebugLogger = Callable[[str], None]


def _read_update_cache(cache_file: Path, *, debug: DebugLogger) -> dict[str, object] | None:
    if not cache_file.exists():
        return None
    try:
        cache = json.loads(cache_file.read_text(encoding="utf-8"))
    except Exception as exc:
        debug(f"Failed to parse update cache {cache_file}: {exc}")
        return None
    if not isinstance(cache, dict):
        debug(f"Ignoring non-object update cache {cache_file}")
        return None
    return cache


def latest_update_cache(
    *,
    hook_file: str | Path,
    cwd: str | Path | None,
    debug: DebugLogger,
) -> tuple[dict[str, object] | None, object | None]:
    """Return the highest-priority valid update cache and its candidate metadata."""
    from gpd.hooks.runtime_detect import (
        RUNTIME_UNKNOWN,
        detect_active_runtime_with_gpd_install,
        detect_runtime_install_target,
        get_update_cache_candidates,
        should_consider_update_cache_candidate,
    )

    workspace_path = resolve_project_root(cwd) if cwd else None
    active_installed_runtime = detect_active_runtime_with_gpd_install(cwd=workspace_path)
    self_install = hook_layout.detect_self_owned_install(hook_file)
    active_install_target = (
        detect_runtime_install_target(active_installed_runtime, cwd=workspace_path)
        if active_installed_runtime not in (None, "", RUNTIME_UNKNOWN)
        else None
    )
    if hook_layout.should_prefer_self_owned_install(
        self_install,
        active_install_target=active_install_target,
        workspace_path=workspace_path,
    ):
        if self_install is not None:
            cache = _read_update_cache(self_install.cache_file, debug=debug)
            if cache is not None:
                return cache, hook_layout.self_owned_update_cache_candidate(self_install)

    preferred_runtime = active_installed_runtime if workspace_path is not None else None
    fallback_hit: tuple[dict[str, object], object] | None = None
    for candidate in get_update_cache_candidates(cwd=workspace_path, preferred_runtime=preferred_runtime):
        if not should_consider_update_cache_candidate(
            candidate,
            active_installed_runtime=active_installed_runtime,
            cwd=workspace_path,
        ):
            continue
        cache = _read_update_cache(candidate.path, debug=debug)
        if cache is None:
            continue
        if getattr(candidate, "runtime", None):
            return cache, candidate
        if fallback_hit is None:
            fallback_hit = (cache, candidate)

    return fallback_hit if fallback_hit is not None else (None, None)


def update_command_for_candidate(
    candidate: object | None,
    *,
    hook_file: str | Path,
    cwd: str | Path | None,
) -> str | None:
    """Return the repair/update command for one resolved update-cache candidate."""
    from gpd.hooks.runtime_detect import (
        RUNTIME_UNKNOWN,
        _runtime_dir_has_gpd_install,
        detect_active_runtime_with_gpd_install,
        detect_install_scope,
        update_command_for_runtime,
    )

    workspace_path = resolve_project_root(cwd) if cwd else None
    self_install = hook_layout.detect_self_owned_install(hook_file)
    candidate_path = getattr(candidate, "path", None)
    if self_install is not None and candidate_path == self_install.cache_file:
        return self_install.update_command

    runtime = getattr(candidate, "runtime", None) or RUNTIME_UNKNOWN
    scope = getattr(candidate, "scope", None)
    if runtime != RUNTIME_UNKNOWN and not _runtime_dir_has_gpd_install(runtime, cwd=workspace_path):
        runtime = RUNTIME_UNKNOWN
        scope = None
    if runtime == RUNTIME_UNKNOWN:
        runtime = detect_active_runtime_with_gpd_install(cwd=workspace_path)
    if scope is None and runtime != RUNTIME_UNKNOWN:
        scope = detect_install_scope(runtime, cwd=workspace_path)
    return update_command_for_runtime(runtime, scope=scope)
