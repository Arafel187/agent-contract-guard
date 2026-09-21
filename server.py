#!/usr/bin/env python3
"""
AgentContract Guard MCP Server
==============================
Provides MCP tool interface for autonomous agents and orchestration frameworks
to validate tool schemas, detect payload drift, and enforce execution contracts.
"""

from typing import Dict, Any, List
from mcp.server.fastmcp import FastMCP
from agent_contract_guard import validate_agent_contract

mcp = FastMCP("AgentContract Guard", dependencies=["mcp", "pydantic"])


@mcp.tool(
    name="validate_agent_contract",
    description="Validate an agent tool execution payload against a JSON schema. Returns conformance verdict, validation errors, payload hash, and schema drift detection."
)
def validate_contract_tool(schema: Dict[str, Any], payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validates payload against schema deterministically.

    :param schema: Expected JSON schema definition (with 'type', 'required', 'properties')
    :param payload: Actual input or output payload produced/consumed by an AI agent
    :return: Validation verdict, conformance status, errors list, payload hash, and latency
    """
    return validate_agent_contract(schema, payload)


if __name__ == "__main__":
    mcp.run()
