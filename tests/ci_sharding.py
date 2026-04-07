from __future__ import annotations

import subprocess
import sys
from collections import Counter
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path

CI_CATEGORY_SHARD_COUNTS = {
    # Rebalanced from the April 7, 2026 PR timings:
    # root 1/2 ~2m, root 2/2 ~4m, hooks ~2m, adapters ~1m,
    # core shards ~34-47s, mcp ~42s.
    "root": 5,
    "adapters": 1,
    "hooks": 2,
    "mcp": 1,
    "core": 3,
}


@dataclass(frozen=True)
class CIShardSpec:
    slug: str
    category: str
    shard_index: int
    shard_total: int


def category_for_test_relpath(rel_path: str) -> str:
    return rel_path.split("/", 1)[0] if "/" in rel_path else "root"


def ci_shard_specs() -> tuple[CIShardSpec, ...]:
    specs: list[CIShardSpec] = []
    for category, shard_total in CI_CATEGORY_SHARD_COUNTS.items():
        for shard_index in range(1, shard_total + 1):
            slug = category if shard_total == 1 else f"{category}-{shard_index}"
            specs.append(
                CIShardSpec(
                    slug=slug,
                    category=category,
                    shard_index=shard_index,
                    shard_total=shard_total,
                )
            )
    return tuple(specs)


def all_test_relpaths(*, tests_root: Path) -> tuple[str, ...]:
    return tuple(path.relative_to(tests_root).as_posix() for path in sorted(tests_root.rglob("test_*.py")))


def assign_weighted_relpaths_to_shards(
    relpath_weights: Mapping[str, int],
    *,
    shard_total: int,
) -> tuple[tuple[str, ...], ...]:
    if shard_total < 1:
        raise ValueError("shard_total must be positive")

    shard_paths: list[list[str]] = [[] for _ in range(shard_total)]
    shard_weights = [0] * shard_total
    ordered_items = sorted(relpath_weights.items(), key=lambda item: (-item[1], item[0]))

    for rel_path, weight in ordered_items:
        target_index = min(
            range(shard_total),
            key=lambda index: (shard_weights[index], len(shard_paths[index]), index),
        )
        shard_paths[target_index].append(rel_path)
        shard_weights[target_index] += weight

    return tuple(tuple(sorted(paths)) for paths in shard_paths)


def plan_category_shards_from_file_counts(
    file_counts: Mapping[str, int],
    *,
    category: str,
    shard_total: int,
) -> tuple[tuple[str, ...], ...]:
    category_counts = {
        rel_path: count for rel_path, count in file_counts.items() if category_for_test_relpath(rel_path) == category
    }
    if not category_counts:
        raise ValueError(f"no collected test files matched category {category!r}")
    return assign_weighted_relpaths_to_shards(category_counts, shard_total=shard_total)


def collected_test_counts_by_file(*, repo_root: Path | None = None) -> Counter[str]:
    root = Path.cwd() if repo_root is None else repo_root
    proc = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "tests/",
            "--collect-only",
            "-q",
            "-n",
            "0",
        ],
        cwd=root,
        check=True,
        text=True,
        capture_output=True,
    )

    counts: Counter[str] = Counter()
    for line in proc.stdout.splitlines():
        if "::" not in line:
            continue
        path_text = line.split("::", 1)[0]
        if path_text.startswith("tests/"):
            path_text = path_text[len("tests/") :]
        counts[path_text] += 1
    return counts


def select_ci_shard_targets(
    *,
    category: str,
    shard_index: int,
    shard_total: int,
    repo_root: Path | None = None,
) -> tuple[str, ...]:
    if shard_index < 1 or shard_index > shard_total:
        raise ValueError("shard_index must be within shard_total")
    counts = collected_test_counts_by_file(repo_root=repo_root)
    planned_shards = plan_category_shards_from_file_counts(
        counts,
        category=category,
        shard_total=shard_total,
    )
    return tuple(f"tests/{rel_path}" for rel_path in planned_shards[shard_index - 1])


def write_ci_shard_targets_file(
    *,
    target_file: Path,
    category: str,
    shard_index: int,
    shard_total: int,
    repo_root: Path | None = None,
) -> tuple[str, ...]:
    targets = select_ci_shard_targets(
        category=category,
        shard_index=shard_index,
        shard_total=shard_total,
        repo_root=repo_root,
    )
    target_file.write_text("\n".join(targets) + "\n", encoding="utf-8")
    return targets
