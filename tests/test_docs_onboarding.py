"""Focused regression coverage for beginner onboarding docs."""

from __future__ import annotations

from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def _assert_fragments(content: str, fragments: tuple[str, ...]) -> None:
    for fragment in fragments:
        assert fragment in content


def _assert_in_order(content: str, fragments: tuple[str, ...]) -> None:
    positions = [content.index(fragment) for fragment in fragments]
    assert positions == sorted(positions)


def _markdown_section(content: str, heading: str) -> str:
    marker = f"{heading}\n"
    start = content.index(marker)
    next_heading = content.find("\n## ", start + len(marker))
    if next_heading == -1:
        return content[start:]
    return content[start:next_heading]


@pytest.mark.parametrize(
    ("doc_name", "fragments"),
    [
        (
            "claude-code.md",
            (
                "/gpd:help",
                "/gpd:start",
                "/gpd:tour",
                "/gpd:new-project --minimal",
                "/gpd:map-research",
                "/gpd:resume-work",
            ),
        ),
        (
            "codex.md",
            (
                "$gpd-help",
                "$gpd-start",
                "$gpd-tour",
                "$gpd-new-project --minimal",
                "$gpd-map-research",
                "$gpd-resume-work",
            ),
        ),
        (
            "gemini-cli.md",
            (
                "/gpd:help",
                "/gpd:start",
                "/gpd:tour",
                "/gpd:new-project --minimal",
                "/gpd:map-research",
                "/gpd:resume-work",
            ),
        ),
        (
            "opencode.md",
            (
                "/gpd-help",
                "/gpd-start",
                "/gpd-tour",
                "/gpd-new-project --minimal",
                "/gpd-resume-work",
                "/gpd-map-research",
            ),
        ),
    ],
)
def test_runtime_quickstarts_surface_the_beginner_next_steps(
    doc_name: str, fragments: tuple[str, ...]
) -> None:
    content = _read(f"docs/{doc_name}")
    _assert_fragments(content, fragments)
    _assert_in_order(content, fragments[:3])
    assert "Back to the onboarding hub: [GPD Onboarding Hub](./README.md)." in content


@pytest.mark.parametrize(
    "doc_name",
    ["macos.md", "windows.md", "linux.md"],
)
def test_os_quickstarts_link_runtime_guides_and_post_install_help(doc_name: str) -> None:
    content = _read(f"docs/{doc_name}")

    _assert_fragments(
        content,
        (
            "Confirm success",
            "gpd --help",
            "Not sure which path fits this folder",
            "Want a guided overview",
            "/gpd:start",
            "$gpd-start",
            "/gpd-start",
            "/gpd:tour",
            "$gpd-tour",
            "/gpd-tour",
            "Start a new project",
            "Map an existing folder",
            "Reopen work from your normal terminal",
            "resume-work",
        ),
    )
    assert "Back to the onboarding hub: [GPD Onboarding Hub](./README.md)." in content

    for guide in ("claude-code.md", "codex.md", "gemini-cli.md", "opencode.md"):
        assert f"./{guide}" in content


def test_docs_onboarding_hub_links_os_and_runtime_guides() -> None:
    content = _read("docs/README.md")

    _assert_fragments(
        content,
        (
            "# GPD Onboarding Hub",
            "Your **normal terminal**",
            "Your **runtime**",
            "`help -> start -> tour -> new-project / map-research -> resume-work`",
            "Common beginner terms",
            "**API credits**",
            "**`--local`**",
            "**`gpd resume`**",
            "**`resume-work`**",
            "./macos.md",
            "./windows.md",
            "./linux.md",
            "./claude-code.md",
            "./codex.md",
            "./gemini-cli.md",
            "./opencode.md",
            "npx -y get-physics-done --claude --local",
            "npx -y get-physics-done --codex --local",
            "npx -y get-physics-done --gemini --local",
            "npx -y get-physics-done --opencode --local",
            "/gpd:...",
            "$gpd-...",
            "/gpd-...",
        ),
    )
    _assert_in_order(
        content,
        (
            "`help -> start -> tour -> new-project / map-research -> resume-work`",
            "`help` shows the command list.",
            "## Choose your OS",
            "## Choose your runtime",
            "## How to use the guides",
        ),
    )


def test_root_readme_start_here_links_to_docs_onboarding_hub() -> None:
    content = _read("README.md")
    start_here = _markdown_section(content, "## Start Here")

    _assert_fragments(
        start_here,
        (
            "[Beginner Onboarding Hub](./docs/README.md)",
            "There are two places you type commands:",
            "In your normal system terminal:",
            "Inside your AI runtime:",
        ),
    )


def test_runtime_quickstarts_keep_current_provider_specific_setup_notes() -> None:
    claude = _read("docs/claude-code.md")
    gemini = _read("docs/gemini-cli.md")
    opencode = _read("docs/opencode.md")

    assert "Pro, Max, Teams, Enterprise, or Console account" in claude
    assert "GOOGLE_CLOUD_PROJECT" in gemini
    assert "/connect" in opencode
