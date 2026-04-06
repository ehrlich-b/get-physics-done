"""Tiny dependency-free strings shared by model-visible prompt wrappers."""

from __future__ import annotations

__all__ = [
    "agent_visibility_note",
    "command_visibility_note",
    "review_contract_visibility_note",
]


def agent_visibility_note() -> str:
    return "Model-visible agent requirements. Follow this YAML directly."


def command_visibility_note() -> str:
    return "Model-visible execution constraints. Follow this YAML directly."


def review_contract_visibility_note() -> str:
    return "Model-visible review contract. Command preflight and validation use the same schema."
