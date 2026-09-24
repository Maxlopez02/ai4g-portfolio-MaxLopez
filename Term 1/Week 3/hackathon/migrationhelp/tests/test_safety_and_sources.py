import json

import pytest
from google.genai import errors

from migrationhelp.assistant import GEMINI_RESPONSE_SCHEMA, _parse_answer, answer_question
from migrationhelp.knowledge_base import select_sources
from migrationhelp.safety import check_question, is_emergency


def test_registration_question_routes_to_brp_source():
    source_ids = {source.id for source in select_sources("How do I register for a BSN at my gemeente?")}
    assert "government-brp" in source_ids


def test_health_question_routes_to_insurance_source():
    source_ids = {source.id for source in select_sources("Do I need Dutch health insurance for work?")}
    assert "government-insurance" in source_ids


def test_empty_question_is_rejected():
    result = check_question("   ")
    assert not result.allowed


def test_possible_bsn_is_rejected():
    result = check_question("My number is 123456789. What should I do?")
    assert not result.allowed
    assert "BSN" in result.message


def test_emergency_is_detected_without_ai():
    assert is_emergency("I am in immediate danger")


def test_uncited_ai_answer_is_rejected():
    sources = select_sources("How do I get a BSN?")
    payload = json.dumps(
        {
            "direct_answer": "Register.",
            "steps": ["Go online."],
            "what_to_prepare": [],
            "limits": "Check first.",
            "risk_level": "low",
            "source_ids": ["invented-source"],
        }
    )
    with pytest.raises(ValueError, match="official source"):
        _parse_answer(payload, sources)


def test_valid_structured_answer_is_accepted():
    sources = select_sources("How do I get a BSN?")
    valid_id = sources[0].id
    payload = json.dumps(
        {
            "direct_answer": "Start with the municipality.",
            "steps": ["Make an appointment."],
            "what_to_prepare": ["Ask the municipality which documents apply."],
            "limits": "Requirements depend on your situation.",
            "risk_level": "medium",
            "source_ids": [valid_id],
        }
    )
    answer = _parse_answer(payload, sources)
    assert answer.source_ids == [valid_id]


def test_api_call_requests_gemini_structured_output():
    class FakeModels:
        def __init__(self):
            self.request = None

        def generate_content(self, **kwargs):
            self.request = kwargs
            source_id = "government-brp"
            output = {
                "direct_answer": "Start with the municipality.",
                "steps": ["Make an appointment."],
                "what_to_prepare": [],
                "limits": "Confirm the documents with the municipality.",
                "risk_level": "low",
                "source_ids": [source_id],
            }
            return type("Response", (), {"text": json.dumps(output)})()

    class FakeClient:
        def __init__(self):
            self.models = FakeModels()

    client = FakeClient()
    answer = answer_question(
        "How do I register for a BSN?",
        "English",
        "More than 4 months",
        "The Hague",
        client=client,
    )

    assert answer.source_ids == ["government-brp"]
    assert client.models.request["config"].response_mime_type == "application/json"
    assert client.models.request["config"].response_schema == GEMINI_RESPONSE_SCHEMA
    assert "OFFICIAL_SOURCE_PACK" in client.models.request["contents"]


def test_temporary_gemini_failure_uses_backup_model():
    class FakeModels:
        def __init__(self):
            self.models_used = []

        def generate_content(self, **kwargs):
            self.models_used.append(kwargs["model"])
            if len(self.models_used) == 1:
                raise errors.ServerError(503, {"error": {"message": "temporarily unavailable"}})
            output = {
                "direct_answer": "Start with the municipality.",
                "steps": ["Make an appointment."],
                "what_to_prepare": [],
                "limits": "Confirm the documents with the municipality.",
                "risk_level": "low",
                "source_ids": ["government-brp"],
            }
            return type("Response", (), {"text": json.dumps(output)})()

    class FakeClient:
        def __init__(self):
            self.models = FakeModels()

    client = FakeClient()
    answer = answer_question(
        "How do I register for a BSN?",
        "English",
        "More than 4 months",
        "The Hague",
        client=client,
    )

    assert answer.direct_answer == "Start with the municipality."
    assert client.models.models_used == ["gemini-3.5-flash-lite", "gemini-3.8-flash"]
