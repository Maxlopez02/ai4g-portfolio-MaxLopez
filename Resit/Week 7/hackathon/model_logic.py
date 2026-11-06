"""Pure model-response parsing for Hogweed Guard NL."""

from __future__ import annotations

from typing import Any


CLASS_ALIASES = {
    "giant hogweed": "giant_hogweed",
    "giant-hogweed": "giant_hogweed",
    "heracleum mantegazzianum": "giant_hogweed",
    "common hogweed": "common_hogweed",
    "common-hogweed": "common_hogweed",
    "heracleum sphondylium": "common_hogweed",
    "cow parsley": "cow_parsley",
    "cow-parsley": "cow_parsley",
    "anthriscus sylvestris": "cow_parsley",
}


def normalise_label(label: str) -> str:
    """Map Roboflow label variants to stable class identifiers."""
    cleaned = label.strip().lower().replace("__", "_")
    cleaned = CLASS_ALIASES.get(cleaned, cleaned)
    return cleaned.replace("-", "_").replace(" ", "_")


def extract_predictions(payload: Any) -> list[tuple[str, float]]:
    """Parse common Roboflow direct-model and Workflow response shapes."""
    if isinstance(payload, list):
        if len(payload) == 1 and isinstance(payload[0], dict):
            return extract_predictions(payload[0])
        candidates = payload
    elif isinstance(payload, dict):
        candidates = payload.get("predictions", [])
        if isinstance(candidates, dict):
            if all(isinstance(value, (int, float)) for value in candidates.values()):
                candidates = [
                    {"class": label, "confidence": confidence}
                    for label, confidence in candidates.items()
                ]
            else:
                nested = extract_predictions(candidates)
                if nested:
                    return nested
        if not candidates and payload.get("top"):
            candidates = [
                {
                    "class": payload["top"],
                    "confidence": payload.get(
                        "confidence", payload.get("top_confidence", 0)
                    ),
                }
            ]
        if not candidates:
            for value in payload.values():
                nested = extract_predictions(value)
                if nested:
                    return nested
    else:
        candidates = []

    parsed: list[tuple[str, float]] = []
    for item in candidates:
        if not isinstance(item, dict):
            continue
        label = item.get("class") or item.get("label") or item.get("class_name")
        confidence = item.get("confidence", item.get("score", 0))
        if label is None:
            continue
        try:
            parsed.append((normalise_label(str(label)), float(confidence)))
        except (TypeError, ValueError):
            continue
    return sorted(parsed, key=lambda row: row[1], reverse=True)


def screening_decision(
    predictions: list[tuple[str, float]], threshold: float = 0.65
) -> tuple[str, float]:
    """Return a known class or an uncertainty outcome."""
    known = [
        (label, score)
        for label, score in predictions
        if label in {"giant_hogweed", "common_hogweed", "cow_parsley"}
    ]
    if not known:
        return "unrecognised", 0.0
    label, score = known[0]
    return (label if score >= threshold else "uncertain", score)
