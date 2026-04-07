from __future__ import annotations

from pathlib import Path

import yaml

from tests.ci_sharding import (
    CI_CATEGORY_SHARD_COUNTS,
    all_test_relpaths,
    category_for_test_relpath,
    ci_shard_specs,
    collected_test_counts_by_file,
    plan_category_shards_from_file_counts,
)


def _read(relpath: str) -> str:
    return (Path(__file__).resolve().parent / relpath).read_text(encoding="utf-8")


def _repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _workflow_data() -> dict[str, object]:
    return yaml.safe_load((_repo_root() / ".github" / "workflows" / "test.yml").read_text(encoding="utf-8"))


def _workflow_job_steps(workflow: dict[str, object], job_name: str) -> list[dict[str, object]]:
    jobs = workflow["jobs"]
    assert isinstance(jobs, dict)
    job = jobs[job_name]
    assert isinstance(job, dict)
    steps = job["steps"]
    assert isinstance(steps, list)
    assert all(isinstance(step, dict) for step in steps)
    return steps


def test_root_conftest_keeps_default_collection_as_full_suite() -> None:
    root_conftest = _read("conftest.py")
    core_conftest = _read("core/conftest.py")

    assert "_isolate_machine_local_gpd_data" in root_conftest
    assert "test suite mode: full (default)" in root_conftest
    assert "FAST_SUITE_EXCLUDES" not in root_conftest
    assert "--full-suite" not in root_conftest
    assert "GPD_TEST_FULL" not in root_conftest
    assert "pytest_ignore_collect" not in root_conftest
    assert "collect_ignore" not in core_conftest


def test_default_collection_matches_all_checked_in_test_files() -> None:
    repo_root = _repo_root()
    all_relpaths = all_test_relpaths(tests_root=repo_root / "tests")
    collected_counts = collected_test_counts_by_file(repo_root=repo_root)

    assert tuple(sorted(collected_counts)) == all_relpaths
    assert all(count > 0 for count in collected_counts.values())


def test_ci_and_test_readme_document_default_full_suite_and_sharded_ci() -> None:
    repo_root = _repo_root()
    workflow = _workflow_data()
    pyproject = (repo_root / "pyproject.toml").read_text(encoding="utf-8")
    tests_readme = (repo_root / "tests" / "README.md").read_text(encoding="utf-8")
    jobs = workflow["jobs"]
    assert isinstance(jobs, dict)
    pytest_steps = _workflow_job_steps(workflow, "pytest")
    pytest_step_names = [str(step.get("name", "")) for step in pytest_steps]
    pytest_run_steps = {
        str(step.get("name", "")): str(step.get("run", ""))
        for step in pytest_steps
        if "run" in step
    }
    pytest_job = jobs["pytest"]
    assert isinstance(pytest_job, dict)
    strategy = pytest_job["strategy"]
    assert isinstance(strategy, dict)
    matrix = strategy["matrix"]
    assert isinstance(matrix, dict)
    include = matrix["include"]
    assert isinstance(include, list)

    assert jobs["pytest"].get("needs") is None
    trigger_job = jobs["trigger-staging-rebuild"]
    assert isinstance(trigger_job, dict)
    assert trigger_job["needs"] == ["pytest"]

    assert strategy["fail-fast"] is False
    assert {
        category: sum(1 for entry in include if entry["category"] == category)
        for category in CI_CATEGORY_SHARD_COUNTS
    } == CI_CATEGORY_SHARD_COUNTS
    assert tuple(
        (
            str(entry["category"]),
            int(entry["shard_index"]),
            int(entry["shard_total"]),
        )
        for entry in include
    ) == tuple((spec.category, spec.shard_index, spec.shard_total) for spec in ci_shard_specs())

    assert "Set up Node.js" in pytest_step_names
    assert pytest_step_names.index("Set up Node.js") < pytest_step_names.index("Install dependencies")
    assert 'addopts = "-n auto --dist=worksteal"' in pyproject
    assert 'pytest-xdist>=3.8.0' in pyproject
    resolve_targets_command = pytest_run_steps["Resolve pytest shard targets"]
    pytest_shard_command = pytest_run_steps["Run pytest shard"]
    assert "from tests.ci_sharding import write_ci_shard_targets_file" in resolve_targets_command
    assert 'mapfile -t PYTEST_TARGETS < "$PYTEST_SHARD_TARGET_FILE"' in pytest_shard_command
    assert 'uv run pytest -q "${PYTEST_TARGETS[@]}"' in pytest_shard_command
    assert "--full-suite" not in pytest_shard_command
    assert "Default `uv run pytest` runs the full checked-in suite" in tests_readme
    assert "`uv run pytest -q` does the same with quieter output" in tests_readme
    assert "override that default explicitly with `uv run pytest -n 0`" in tests_readme
    assert "GitHub Actions workflow runs that same full suite as twelve balanced shards" in tests_readme
    assert "uses `tests/ci_sharding.py` to bucket files by collected test counts" in tests_readme


def test_ci_shard_layout_covers_every_test_file_without_overlap() -> None:
    all_relpaths = all_test_relpaths(tests_root=_repo_root() / "tests")
    file_counts = dict.fromkeys(all_relpaths, 1)
    assigned: list[str] = []

    for spec in ci_shard_specs():
        planned_shards = plan_category_shards_from_file_counts(
            file_counts,
            category=spec.category,
            shard_total=spec.shard_total,
        )
        assigned.extend(planned_shards[spec.shard_index - 1])

    assert sorted(assigned) == list(all_relpaths)
    assert len(set(assigned)) == len(all_relpaths)
    assert {
        category: sum(1 for rel_path in all_relpaths if category_for_test_relpath(rel_path) == category)
        for category in CI_CATEGORY_SHARD_COUNTS
    } == {
        category: sum(1 for rel_path in assigned if category_for_test_relpath(rel_path) == category)
        for category in CI_CATEGORY_SHARD_COUNTS
    }
