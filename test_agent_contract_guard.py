#!/usr/bin/env python3
import pytest
from agent_contract_guard import validate_agent_contract


def test_conformant_payload():
    schema = {
        "type": "object",
        "required": ["agent_id", "status"],
        "properties": {
            "agent_id": {"type": "string"},
            "status": {"type": "string"}
        }
    }
    payload = {"agent_id": "mech_01", "status": "completed"}
    res = validate_agent_contract(schema, payload)
    assert res["is_valid"] is True
    assert res["verdict"] == "CONFORMANT"
    assert res["schema_drift_detected"] is False


def test_schema_drift():
    schema = {
        "type": "object",
        "required": ["agent_id"],
        "properties": {
            "agent_id": {"type": "string"}
        }
    }
    payload = {"agent_id": "mech_01", "unexpected_extra": 123}
    res = validate_agent_contract(schema, payload)
    assert res["is_valid"] is True
    assert res["verdict"] == "CONFORMANT_WITH_SCHEMA_DRIFT"
    assert res["schema_drift_detected"] is True


def test_contract_violation_missing_required():
    schema = {
        "type": "object",
        "required": ["agent_id", "task_id"],
        "properties": {
            "agent_id": {"type": "string"},
            "task_id": {"type": "string"}
        }
    }
    payload = {"agent_id": "mech_01"}
    res = validate_agent_contract(schema, payload)
    assert res["is_valid"] is False
    assert res["verdict"] == "CONTRACT_VIOLATION"
    assert any("task_id" in err for err in res["errors"])


def test_contract_violation_type_mismatch():
    schema = {
        "type": "object",
        "required": ["count"],
        "properties": {
            "count": {"type": "integer"}
        }
    }
    payload = {"count": "not_an_int"}
    res = validate_agent_contract(schema, payload)
    assert res["is_valid"] is False
    assert res["verdict"] == "CONTRACT_VIOLATION"


if __name__ == "__main__":
    test_conformant_payload()
    test_schema_drift()
    test_contract_violation_missing_required()
    test_contract_violation_type_mismatch()
    print("All PA-002 unit tests passed successfully.")
