"""Evaluate the trained Roboflow workflow on the untouched 36-image test set."""

from __future__ import annotations

import csv
import json
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

from app import run_inference


ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = ROOT / "dataset" / "images" / "held_out_test"
EVIDENCE = ROOT / "evidence"
CLASSES = ["giant_hogweed", "common_hogweed", "cow_parsley"]


def predict_with_retry(path: Path, attempts: int = 3) -> tuple[str, float]:
    last_error: Exception | None = None
    for attempt in range(attempts):
        try:
            with Image.open(path) as source:
                predictions = run_inference(source.convert("RGB"))
            if not predictions:
                raise RuntimeError("Workflow returned no recognised class predictions")
            return predictions[0]
        except Exception as exc:  # network retries are intentionally broad
            last_error = exc
            if attempt + 1 < attempts:
                time.sleep(2 ** attempt)
    raise RuntimeError(f"Inference failed for {path.name}: {last_error}")


def main() -> None:
    EVIDENCE.mkdir(exist_ok=True)
    rows: list[dict[str, object]] = []
    confusion = Counter()

    files = [
        (actual, path)
        for actual in CLASSES
        for path in sorted((TEST_ROOT / actual).glob("*"))
        if path.is_file()
    ]

    def classify(item: tuple[str, Path]) -> tuple[str, Path, str, float]:
        actual, path = item
        predicted, confidence = predict_with_retry(path)
        return actual, path, predicted, confidence

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(classify, item) for item in files]
        completed = as_completed(futures)
        outputs = []
        for index, future in enumerate(completed, start=1):
            actual, path, predicted, confidence = future.result()
            outputs.append((actual, path, predicted, confidence))
            print(
                f"[{index:02d}/{len(files)}] {actual:16s} -> {predicted:16s} "
                f"{confidence:6.1%} {'OK' if predicted == actual else 'MISS'}",
                flush=True,
            )

    for actual, path, predicted, confidence in sorted(
        outputs, key=lambda item: (CLASSES.index(item[0]), item[1].name)
    ):
        correct = predicted == actual
        confusion[(actual, predicted)] += 1
        rows.append(
            {
                "file_name": path.name,
                "actual": actual,
                "predicted": predicted,
                "confidence": round(confidence, 6),
                "correct": correct,
            }
        )

    csv_path = EVIDENCE / "held_out_results.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    per_class = {}
    for actual in CLASSES:
        class_rows = [row for row in rows if row["actual"] == actual]
        correct = sum(bool(row["correct"]) for row in class_rows)
        per_class[actual] = {
            "correct": correct,
            "total": len(class_rows),
            "accuracy": correct / len(class_rows),
        }

    correct_total = sum(bool(row["correct"]) for row in rows)
    summary = {
        "total_correct": correct_total,
        "total_images": len(rows),
        "accuracy": correct_total / len(rows),
        "per_class": per_class,
        "confusion_matrix": {
            actual: {predicted: confusion[(actual, predicted)] for predicted in CLASSES}
            for actual in CLASSES
        },
    }
    (EVIDENCE / "held_out_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )

    matrix = np.array(
        [[confusion[(actual, predicted)] for predicted in CLASSES] for actual in CLASSES]
    )
    labels = ["Giant hogweed", "Common hogweed", "Cow parsley"]
    fig, ax = plt.subplots(figsize=(7.2, 6.2))
    image = ax.imshow(matrix, cmap="Greens", vmin=0, vmax=max(12, int(matrix.max())))
    for row in range(len(CLASSES)):
        for column in range(len(CLASSES)):
            ax.text(column, row, matrix[row, column], ha="center", va="center", fontsize=16)
    ax.set_xticks(range(len(labels)), labels, rotation=25, ha="right")
    ax.set_yticks(range(len(labels)), labels)
    ax.set_xlabel("Predicted class")
    ax.set_ylabel("Actual class")
    ax.set_title(f"Held-out test confusion matrix — {correct_total}/{len(rows)} correct")
    fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04)
    fig.tight_layout()
    fig.savefig(EVIDENCE / "held_out_confusion_matrix.png", dpi=180)
    plt.close(fig)

    print(json.dumps(summary, indent=2), flush=True)


if __name__ == "__main__":
    main()
