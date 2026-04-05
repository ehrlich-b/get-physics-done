"""Regression coverage for malformed runtime bridge invocations."""

from __future__ import annotations

import pytest

import gpd.runtime_cli as runtime_cli


def test_runtime_cli_rejects_missing_bridge_arguments_without_argparse_abort(
    capsys: pytest.CaptureFixture[str],
) -> None:
    exit_code = runtime_cli.main(["state", "load"])

    captured = capsys.readouterr()
    assert exit_code == 127
    assert "GPD runtime bridge rejected malformed bridge invocation." in captured.err
    assert "the following arguments are required: --runtime, --config-dir, --install-scope" in captured.err
    assert "usage:" not in captured.err.lower()


@pytest.mark.parametrize(
    "argv, expected_fragment",
    [
        (
            [
                "--runtime",
                "codex",
                "--config-dir",
                "/tmp/GPD",
                "--install-scope",
                "sideways",
                "state",
                "load",
            ],
            "invalid choice: 'sideways' (choose from 'local', 'global')",
        ),
        (
            [
                "--runtime",
                "codex",
                "--config-dir",
                "/tmp/GPD",
                "--install-scope",
            ],
            "argument --install-scope: expected one argument",
        ),
        (
            [
                "--runtime",
                "codex",
                "--config-dir",
                "/tmp/GPD",
                "--install-scope",
                "local",
                "--runtime",
            ],
            "argument --runtime: expected one argument",
        ),
        (
            [
                "--runtime",
                "codex",
                "--config-dir",
                "/tmp/GPD",
                "--install-scope",
                "local",
                "--bogus",
                "state",
                "load",
            ],
            "unrecognized forwarded gpd root flag: --bogus",
        ),
        (
            [
                "--runtime",
                "codex",
                "--config-dir",
                "/tmp/GPD",
                "--install-scope",
                "local",
                "--configdir",
                "/tmp/GPD",
                "state",
                "load",
            ],
            "unrecognized forwarded gpd root flag: --configdir",
        ),
    ],
)
def test_runtime_cli_rejects_malformed_bridge_invocations(
    argv: list[str],
    expected_fragment: str,
    capsys: pytest.CaptureFixture[str],
) -> None:
    exit_code = runtime_cli.main(argv)

    captured = capsys.readouterr()
    assert exit_code == 127
    assert "GPD runtime bridge rejected malformed bridge invocation." in captured.err
    assert expected_fragment in captured.err
    assert "usage:" not in captured.err.lower()
