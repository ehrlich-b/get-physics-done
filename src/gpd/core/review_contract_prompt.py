"""Helpers for surfacing review contracts inside model-visible prompt bodies."""

from __future__ import annotations

from collections.abc import Mapping

import yaml

_REVIEW_CONTRACT_FIELD_ORDER = (
    "schema_version",
    "review_mode",
    "required_outputs",
    "required_evidence",
    "blocking_conditions",
    "preflight_checks",
    "stage_ids",
    "stage_artifacts",
    "final_decision_output",
    "requires_fresh_context_per_stage",
    "max_review_rounds",
    "required_state",
)
_REVIEW_CONTRACT_WRAPPER_KEYS = ("review_contract", "review-contract")
_REVIEW_CONTRACT_DEFAULTS: dict[str, object] = {
    "required_outputs": [],
    "required_evidence": [],
    "blocking_conditions": [],
    "preflight_checks": [],
    "stage_ids": [],
    "stage_artifacts": [],
    "final_decision_output": "",
    "requires_fresh_context_per_stage": False,
    "max_review_rounds": 0,
    "required_state": "",
}


def extract_frontmatter_block(frontmatter: str, field_name: str) -> str:
    """Return one top-level YAML frontmatter block, preserving raw formatting."""

    lines = frontmatter.split("\n")
    prefix = f"{field_name}:"
    collected: list[str] = []
    collecting = False

    for line in lines:
        stripped = line.strip()
        is_top_level = line == line.lstrip()
        if not collecting:
            if is_top_level and stripped.startswith(prefix):
                collected.append(line.rstrip())
                collecting = True
            continue
        if is_top_level and stripped:
            break
        collected.append(line.rstrip())

    while collected and not collected[-1]:
        collected.pop()
    return "\n".join(collected)


def _normalize_review_contract_payload(review_contract: object) -> dict[str, object]:
    """Return a canonical typed payload for rendering a review contract section."""

    if review_contract is None:
        return {}
    if isinstance(review_contract, str):
        block = review_contract.strip()
        if not block:
            return {}
        loaded = yaml.safe_load(block)
    elif isinstance(review_contract, Mapping):
        loaded = dict(review_contract)
    else:
        raise ValueError("review contract must be provided as YAML text or a mapping")

    if loaded is None:
        return {}
    if not isinstance(loaded, dict):
        raise ValueError(f"review contract must parse to a mapping, got {type(loaded).__name__}")

    for key in _REVIEW_CONTRACT_WRAPPER_KEYS:
        wrapped = loaded.get(key)
        if isinstance(wrapped, Mapping):
            loaded = dict(wrapped)
            break

    payload: dict[str, object] = {}
    for key in _REVIEW_CONTRACT_FIELD_ORDER:
        if key in loaded:
            payload[key] = loaded[key]
        elif key in _REVIEW_CONTRACT_DEFAULTS:
            payload[key] = _REVIEW_CONTRACT_DEFAULTS[key]
    for key, value in loaded.items():
        if key not in payload:
            payload[key] = value
    return payload


def render_review_contract_prompt(review_contract: object) -> str:
    """Render a canonical model-visible review-contract section."""

    payload = _normalize_review_contract_payload(review_contract)
    if not payload:
        return ""
    rendered = yaml.safe_dump(
        {"review_contract": payload},
        sort_keys=False,
        allow_unicode=False,
    ).rstrip()
    return (
        "## Review Contract\n\n"
        "This command is enforced against the following hard review contract. "
        "Satisfy it directly in the generated artifacts.\n\n"
        f"```yaml\n{rendered}\n```"
    )


def prepend_review_contract_prompt(body: str, yaml_block: str) -> str:
    """Front-load a review contract ahead of the substantive prompt body."""

    section = render_review_contract_prompt(yaml_block)
    if not section:
        return body
    if not body:
        return section
    return f"{section}\n\n{body}"
