# K1 evidence: an AI tool is essential to the MVP

## Tool and model

- **Platform:** Roboflow
- **Task:** three-class image classification
- **Model:** DINOv3 Small, trained in the Roboflow project
- **Runtime integration:** `InferenceHTTPClient.run_workflow()` in `app.py`
- **Input:** one uploaded plant photograph
- **Output:** confidence scores for giant hogweed, common hogweed and cow parsley

The model call is the central function. The interface has no rule-based fallback
and cannot produce a plant screening result when Roboflow is unavailable. The
code sends the uploaded image to the configured workflow and parses the returned
class scores. A 65% threshold withholds low-confidence results.

## Evidence in this folder

- `app.py`: real Roboflow Workflow call and visible model disclosure
- `model_logic.py`: response parsing and uncertainty decision
- `tests/test_model_logic.py`: tests for parsing and the threshold boundary
- `evidence/app-held-out-giant-hogweed.png`: completed app inference
- `evidence/roboflow-metrics.png`: Roboflow model evidence

Private API keys are intentionally excluded. `.env.example` documents every
required connection value without exposing credentials.
