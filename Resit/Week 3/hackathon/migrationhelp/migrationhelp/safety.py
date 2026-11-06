"""Deterministic input and output safeguards."""

import re
from dataclasses import dataclass

from .knowledge_base import SOURCE_BY_ID, Source


MAX_QUESTION_LENGTH = 1_200


@dataclass(frozen=True)
class SafetyResult:
    allowed: bool
    message: str = ""


def check_question(question: str) -> SafetyResult:
    cleaned = question.strip()
    if not cleaned:
        return SafetyResult(False, "Enter a question before asking for a route.")
    if len(cleaned) > MAX_QUESTION_LENGTH:
        return SafetyResult(False, f"Keep the question under {MAX_QUESTION_LENGTH:,} characters.")

    # A Dutch BSN is nine digits. This deliberately over-blocks some numbers:
    # preventing identity-data disclosure matters more than perfect recall here.
    if re.search(r"(?<!\d)\d{9}(?!\d)", cleaned):
        return SafetyResult(
            False,
            "Remove the 9-digit number before continuing. It may be a BSN. Describe the situation without identity numbers.",
        )

    sensitive_terms = (
        "passport number",
        "document number",
        "residence card number",
        "my bsn is",
        "bsn:",
    )
    if any(term in cleaned.casefold() for term in sensitive_terms):
        return SafetyResult(
            False,
            "Remove passport, residence-card or BSN details. MigrationHelp does not need them.",
        )
    return SafetyResult(True)


def is_emergency(question: str) -> bool:
    text = question.casefold()
    emergency_terms = (
        "immediate danger",
        "emergency",
        "being attacked",
        "someone is attacking",
        "can't breathe",
        "cannot breathe",
        "suicide",
        "kill myself",
        "112",
    )
    return any(term in text for term in emergency_terms)


def validate_source_ids(source_ids: list[str], allowed_sources: list[Source]) -> list[str]:
    allowed_ids = {source.id for source in allowed_sources}
    valid: list[str] = []
    for source_id in source_ids:
        if source_id in allowed_ids and source_id in SOURCE_BY_ID and source_id not in valid:
            valid.append(source_id)
    if not valid:
        raise ValueError("The AI response did not cite an allowed official source.")
    return valid
