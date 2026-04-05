"""Focused regressions for protocol routing reliability."""

from __future__ import annotations

import anyio


def _route_protocol(query: str) -> dict[str, object]:
    from gpd.mcp.servers.protocols_server import route_protocol

    result = route_protocol(query)
    assert isinstance(result, dict)
    return result


def _route_protocol_tool_schema() -> dict[str, object]:
    from gpd.mcp.servers.protocols_server import mcp

    async def _load() -> dict[str, object]:
        tools = await mcp.list_tools()
        tool = next(tool for tool in tools if tool.name == "route_protocol")
        return tool.inputSchema

    return anyio.run(_load)


def test_route_protocol_rejects_blank_queries_up_front() -> None:
    result = _route_protocol("")

    assert result == {"error": "computation_type must be a non-empty string", "schema_version": 1}


def test_route_protocol_does_not_substring_match_short_or_common_tokens() -> None:
    result = _route_protocol("needs a benchmark comparison")
    names = [protocol["name"] for protocol in result["protocols"]]

    assert "de-sitter-space" not in names
    assert "large-n-expansion" not in names


def test_route_protocol_requires_contiguous_multiword_matches() -> None:
    result = _route_protocol("need group and theory notes plus sign and tracking reminders")
    names = [protocol["name"] for protocol in result["protocols"]]

    assert "group-theory" not in names
    assert "derivation-discipline" not in names


def test_route_protocol_publishes_non_blank_contract_in_tool_schema() -> None:
    schema = _route_protocol_tool_schema()
    computation_type = schema["properties"]["computation_type"]

    assert computation_type["type"] == "string"
    assert computation_type["minLength"] == 1
    assert computation_type["pattern"] == r"\S"
    assert schema["required"] == ["computation_type"]
