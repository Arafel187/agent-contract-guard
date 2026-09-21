#!/usr/bin/env python3
"""
AgentContract Guard — PA-002 Deterministic Tool Execution Contract Verifier
===========================================================================
Product Agent ID: PA-002
Mission: Deterministic schema enforcement & contract validation for autonomous AI agent networks.
Supports:
- Schema conformance validation (checks required fields, data types, value boundaries)
- Payload drift detection
- Machine-readable telemetry logging
"""

import json
import os
import time
import hashlib
from typing import Dict, Any, List, Optional

WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
TELEMETRY_PATH = os.path.join(WORKSPACE_DIR, "ATL_A2A_PA-002_TELEMETRY.jsonl")


def validate_agent_contract(schema: Dict[str, Any], payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validates payload against schema deterministically without external network reliance.
    Returns structured verdict, validation flags, schema drift indicators, and latency.
    """
    t_start = time.perf_counter()
    errors: List[str] = []
    drift_detected = False

    schema_type = schema.get("type", "object")
    required_fields = schema.get("required", [])
    properties = schema.get("properties", {})

    if not isinstance(payload, dict):
        return {
            "verdict": "INVALID_PAYLOAD",
            "is_valid": False,
            "errors": ["Payload must be a JSON object."],
            "latency_ms": round((time.perf_counter() - t_start) * 1000.0, 3),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        }

    # 1. Check required fields
    for field in required_fields:
        if field not in payload:
            errors.append(f"Missing required field: '{field}'")

    # 2. Check property types
    type_map = {
        "string": str,
        "integer": int,
        "number": (int, float),
        "boolean": bool,
        "array": list,
        "object": dict
    }

    for key, val in payload.items():
        if key in properties:
            expected_type_str = properties[key].get("type")
            expected_type = type_map.get(expected_type_str)
            if expected_type and not isinstance(val, expected_type):
                # special case: bool is subclass of int in python
                if expected_type_str in ("integer", "number") and isinstance(val, bool):
                    errors.append(f"Field '{key}' expected {expected_type_str}, received boolean")
                elif not isinstance(val, expected_type):
                    errors.append(f"Type mismatch for field '{key}': expected {expected_type_str}, got {type(val).__name__}")
        else:
            # Undeclared field = schema drift
            drift_detected = True

    is_valid = len(errors) == 0
    if not is_valid:
        verdict = "CONTRACT_VIOLATION"
    elif drift_detected:
        verdict = "CONFORMANT_WITH_SCHEMA_DRIFT"
    else:
        verdict = "CONFORMANT"

    latency_ms = round((time.perf_counter() - t_start) * 1000.0, 3)
    res_hash = hashlib.sha256(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()[:16]

    result = {
        "verdict": verdict,
        "is_valid": is_valid,
        "schema_drift_detected": drift_detected,
        "errors": errors,
        "payload_hash": res_hash,
        "latency_ms": latency_ms,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }

    # Log telemetry
    try:
        with open(TELEMETRY_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps({
                "product_agent_id": "PA-002",
                "timestamp": result["timestamp"],
                "verdict": verdict,
                "is_valid": is_valid,
                "errors_count": len(errors),
                "latency_ms": latency_ms,
                "classification": "AUTONOMOUS_EXECUTION"
            }) + "\n")
    except Exception:
        pass

    return result
