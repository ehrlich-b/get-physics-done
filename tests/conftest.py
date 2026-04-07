from __future__ import annotations

import os
from collections.abc import Iterator

import pytest


@pytest.fixture(scope="session", autouse=True)
def _isolate_machine_local_gpd_data(tmp_path_factory) -> Iterator[None]:
    """Give each pytest worker its own machine-local data root.

    Many state and CLI paths project advisory data into the machine-local
    recent-project cache. Under xdist, sharing one cache root across workers
    creates avoidable lock contention that dominates suite wall time without
    adding coverage value.
    """

    previous = os.environ.get("GPD_DATA_DIR")
    data_root = tmp_path_factory.getbasetemp() / "gpd-data"
    data_root.mkdir(parents=True, exist_ok=True)
    os.environ["GPD_DATA_DIR"] = str(data_root)
    try:
        yield
    finally:
        if previous is None:
            os.environ.pop("GPD_DATA_DIR", None)
        else:
            os.environ["GPD_DATA_DIR"] = previous


def pytest_report_header(config) -> str:
    return "test suite mode: full (default)"
