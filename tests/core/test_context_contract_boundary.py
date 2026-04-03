from __future__ import annotations

import json
from pathlib import Path

from gpd.contracts import ResearchContract
from gpd.core import context as context_module

FIXTURES_DIR = Path(__file__).resolve().parents[1] / "fixtures" / "stage0"


def _load_contract_fixture() -> ResearchContract:
    payload = json.loads((FIXTURES_DIR / "project_contract.json").read_text(encoding="utf-8"))
    return ResearchContract.model_validate(payload)


def test_canonicalize_project_contract_surfaces_recoverable_salvage_findings(monkeypatch) -> None:
    contract = _load_contract_fixture()

    def _recoverable_merge(
        existing: dict[str, object],
        derived: dict[str, object] | None,
        *,
        allowed_subject_ids: set[str],
    ) -> dict[str, object]:
        del allowed_subject_ids
        merged = dict(existing)
        if derived is not None:
            merged["aliases"] = "benchmark-anchor"
        return merged

    monkeypatch.setattr(context_module, "_merge_contract_reference_payload", _recoverable_merge)

    canonical, warnings = context_module._canonicalize_project_contract(
        contract,
        active_references=[reference.model_dump(mode="json") for reference in contract.references],
        effective_reference_intake=contract.context_intake.model_dump(mode="json"),
    )

    assert canonical is not None
    assert canonical.references[0].aliases == ["benchmark-anchor"]
    assert any("canonical project_contract merge required salvage" in warning for warning in warnings)
