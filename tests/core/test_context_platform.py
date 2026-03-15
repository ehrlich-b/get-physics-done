"""Regression tests for runtime platform detection in gpd.core.context."""

from __future__ import annotations

import importlib
import os
from pathlib import Path
from unittest.mock import patch

import pytest

import gpd.core.context as context_module


def _clear_runtime_env(monkeypatch: pytest.MonkeyPatch) -> None:
    """Remove runtime detection env vars so each test controls the signal."""
    for key in list(os.environ):
        if key.startswith(("CLAUDE_CODE", "CODEX", "GEMINI", "OPENCODE")) or key == "GPD_ACTIVE_RUNTIME":
            monkeypatch.delenv(key, raising=False)


@pytest.mark.parametrize(
    ("env_var", "expected"),
    [
        ("CLAUDE_CODE_SESSION", "claude-code"),
        ("CODEX_SESSION", "codex"),
        ("GEMINI_CLI", "gemini"),
        ("OPENCODE_SESSION", "opencode"),
    ],
)
def test_init_context_uses_active_runtime_signal(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, env_var: str, expected: str
) -> None:
    with monkeypatch.context() as runtime_env:
        _clear_runtime_env(runtime_env)
        runtime_env.setenv(env_var, "active")

        module = importlib.reload(context_module)
        ctx = module.init_new_project(tmp_path)
        assert ctx["platform"] == expected

    importlib.reload(context_module)


def test_init_context_uses_runtime_detect_directory_fallback(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    with monkeypatch.context() as runtime_env:
        _clear_runtime_env(runtime_env)
        (tmp_path / ".codex").mkdir()

        with patch("gpd.hooks.runtime_detect.Path.home", return_value=tmp_path), \
             patch("gpd.hooks.runtime_detect.Path.cwd", return_value=tmp_path):
            module = importlib.reload(context_module)
            ctx = module.init_new_project(tmp_path)
            assert ctx["platform"] == "codex"

    importlib.reload(context_module)


def test_init_context_prefers_explicit_gpd_runtime_override(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    with monkeypatch.context() as runtime_env:
        _clear_runtime_env(runtime_env)
        runtime_env.setenv("GPD_ACTIVE_RUNTIME", "codex")
        (tmp_path / ".claude" / "get-physics-done").mkdir(parents=True)
        (tmp_path / ".codex" / "get-physics-done").mkdir(parents=True)

        with patch("gpd.hooks.runtime_detect.Path.home", return_value=tmp_path), \
             patch("gpd.hooks.runtime_detect.Path.cwd", return_value=tmp_path):
            module = importlib.reload(context_module)
            ctx = module.init_progress(tmp_path)
            assert ctx["platform"] == "codex"

    importlib.reload(context_module)


def test_resolve_model_delegates_runtime_specific_lookup_to_config_helper(tmp_path: Path) -> None:
    calls: dict[str, object] = {}

    def _fake_resolve_model(project_dir: Path, agent_name: str, runtime: str | None = None) -> str | None:
        calls["project_dir"] = project_dir
        calls["agent_name"] = agent_name
        calls["runtime"] = runtime
        return "delegated-model"

    with patch.object(context_module, "_resolve_model_canonical", side_effect=_fake_resolve_model):
        result = context_module._resolve_model(
            tmp_path,
            "gpd-planner",
            {"model_profile": "review", "model_overrides": {"codex": {"tier-1": "do-not-read-directly"}}},
            runtime="codex",
        )

    assert result == "delegated-model"
    assert calls == {"project_dir": tmp_path, "agent_name": "gpd-planner", "runtime": "codex"}
