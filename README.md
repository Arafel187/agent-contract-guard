# AgentContract Guard (`PA-002`)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-blue.svg)](https://modelcontextprotocol.io)

**Deterministic Tool Execution Contract Validation & Schema Enforcement for Autonomous Agent Networks.**

AgentContract Guard provides fast, verifiable contract conformance checking and schema drift detection for heterogeneous AI agents (Autonolas Mechs, Nevermined gateways, LangGraph, AutoGen, CrewAI).

---

## The Problem
When autonomous AI agents dynamically discover and invoke remote micro-tools or multi-agent pipelines:
- Schema drift silently corrupts downstream processing.
- Missing required fields cause fatal agent execution crashes.
- Heterogeneous runtimes format responses inconsistently.

AgentContract Guard provides an independent verification gate before payment settlement, state persistence, or next-action dispatch.

---

## Quick Start

### 1. Installation
```bash
pip install -r requirements.txt
```

### 2. Run MCP Server
```bash
python server.py
```

### 3. Claude Desktop / Agent Runtime Configuration
Add to your `claude_desktop_config.json` or agent runner:
```json
{
  "mcpServers": {
    "agent-contract-guard": {
      "command": "python",
      "args": ["-m", "server"],
      "cwd": "/path/to/agent-contract-guard"
    }
  }
}
```

---

## Tool API: `validate_agent_contract`

### Input Parameters
```json
{
  "schema": {
    "type": "object",
    "required": ["agent_id", "status"],
    "properties": {
      "agent_id": {"type": "string"},
      "status": {"type": "string"}
    }
  },
  "payload": {
    "agent_id": "mech_01",
    "status": "completed"
  }
}
```

### Output Response
```json
{
  "verdict": "CONFORMANT",
  "is_valid": true,
  "schema_drift_detected": false,
  "errors": [],
  "payload_hash": "a1b2c3d4e5f67890",
  "latency_ms": 0.04,
  "timestamp": "2026-09-21T10:30:00Z"
}
```

---

## Verdict Categories
- `CONFORMANT`: Payload strictly matches schema with zero drift.
- `CONFORMANT_WITH_SCHEMA_DRIFT`: Payload meets required fields, but contains undeclared extra properties.
- `CONTRACT_VIOLATION`: Payload fails required fields or contains type mismatches.
- `INVALID_PAYLOAD`: Input is malformed or not a valid JSON object.

---

## License
MIT
