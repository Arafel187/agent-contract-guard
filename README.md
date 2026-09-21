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

## Quick Start & Delivery Modes

### Option A: Zero-Install Hosted Remote MCP (Recommended for Agents)
Directly invoke `validate_agent_contract` over HTTPS without local package installation:
- **Canonical Hosted Endpoint**: `https://agentground.atlether.trade/mcp`
- **Protocol**: Streamable HTTP MCP (2026-07-28 & 2024-11-05)
- **Tool Name**: `validate_agent_contract`

In your MCP client or agent orchestrator:
```json
{
  "mcpServers": {
    "agent-contract-guard-hosted": {
      "url": "https://agentground.atlether.trade/mcp"
    }
  }
}
```

### Option B: Local Stdio Package
```bash
pip install -r requirements.txt
python server.py
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

## Commercial Pricing & Real Settlement (USDC / USDT)

AgentContract Guard provides mission-critical preflight validation with transparent commercial pricing.

| Tier | Price (Hypothesis) | Allowance / Rate | Features & Delivery |
| :--- | :--- | :--- | :--- |
| **Free Evaluation** | $0.00 | 60 requests/minute | Public evaluation via hosted gateway (`https://agentground.atlether.trade/mcp`). |
| **Metered Prepaid** | $0.0005 / check | 2,000 checks per $1.00 USDC/USDT (min pack $5.00) | Pay-as-you-go balance, priority queue, programmatic invoice generation (Pricing Hypothesis). |
| **Pro Fleet** | 20 USDC / month | 100,000 validations/month included ($0.0004 overage) | Schema drift alerts, cached schema compilation (Pricing Hypothesis). |
| **Enterprise Pilot** | 200 USDC | 90-day pilot | Dedicated validator instance, custom domain schema suites, runtime integration hooks (Negotiable Pilot Scope). |

> *Note on Pricing:* All tiers represent commercial pricing hypotheses open to discussion and tailoring for specific customer workflows. No contractual uptime SLAs are offered without explicit prior approval from the eligible adult account holder.

### Programmatic Invoice & Credit Orders
Agents can request an invoice directly via our automated gateway:
```bash
curl -X POST https://agentground.atlether.trade/api/v1/request-invoice \
  -H "Content-Type: application/json" \
  -d '{
    "customer_ref": "your-agent-or-runtime-id",
    "product_id": "PA-002",
    "tier": "METERED_PREPAID",
    "currency": "USDC",
    "amount_usd": 10.0
  }'
```

> **Financial Boundary Notice:** In accordance with our security policy, all settlement instructions are reviewed and confirmed by an eligible adult account holder. Autonomous agents do not hold private keys or execute unauthorized fund transfers.

---

## License
MIT
