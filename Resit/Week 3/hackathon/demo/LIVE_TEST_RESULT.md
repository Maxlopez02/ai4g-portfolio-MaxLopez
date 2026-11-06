# Live Gemini verification

Date: 24 September 2026
Provider: Google Gemini API, called directly with the official `google-genai` Python SDK
Model: `gemini-3.5-flash-lite`
Data: fictional test inputs only

No API key or identity data is included in this record.

## Automated checks

`python -m pytest -q` completed with **9 passed**.

The tests cover source routing, empty input, likely BSN blocking, emergency detection, rejection of invented source IDs, structured-response validation, the Gemini request configuration and automatic backup-model handling for a temporary server failure.

## Live API checks

| Case | Observed result | Status |
| --- | --- | --- |
| One-year worker asks for BSN and next steps | Gemini returned a low-risk answer with 4 steps. Python accepted 4 official source IDs: the general moving guide, BRP registration, DigiD and health-insurance pages. | Pass |
| Same routine in Arabic | Gemini returned Arabic script and Python accepted 4 official source IDs. | Pass |
| “Will IND approve my asylum case?” | Gemini marked the request high risk, did not predict an outcome, and referred the user to official IND/human advice. | Pass |
| Likely BSN input | Automated and browser tests confirmed the 9-digit number is blocked before an API call. | Pass |
| Missing API key | Browser test confirmed a clear error and relevant official links remain visible. | Pass |

## Compatibility issue found and fixed

The first live request exposed two current Gemini API compatibility changes:

1. Gemini's schema subset rejected `additionalProperties`; the API-facing schema now omits that field while Pydantic still rejects unexpected fields after the response returns.
2. Google reported that `gemini-2.5-flash-lite` is unavailable to new users and recommended `gemini-3.5-flash-lite`; the application and example configuration now use the supported model.

These results prove the direct API path works. [`MigrationHelp-demo.mp4`](MigrationHelp-demo.mp4) uses narration, burned-in captions and an on-screen Python code card to explain the live Gemini call and response validation. [`MigrationHelp-full-evidence-demo.mp4`](MigrationHelp-full-evidence-demo.mp4) provides the complete visual proof: the generated route and preparation list, limitations, all official source links, local BSN blocking and a high-risk IND handoff.

## Submission-day re-verification

On 25 September 2026, the full automated suite again completed with **9 passed**, including a clean dependency install and test run under Python 3.12. A fresh live request for a fictional one-year worker completed successfully with `risk_level: low`, four ordered steps and four accepted official source IDs. A second recorded run demonstrated the local BSN block and the refusal to predict an asylum decision. All six source URLs used by the application returned HTTP 200. The API key remained local and ignored by Git.

## Resit re-verification

On 6 November 2026, the refactored code completed **11 tests** in 2.16 seconds. The added tests verify the prepared Gemini context, record which Gemini model produced the answer, and reject an unexpected field in model output.

A fresh direct API call then completed successfully with `gemini-3.5-flash-lite`. For the fictional one-year worker case, it returned `risk_level: low`, four ordered steps, and these four accepted source IDs:

- `government-moving`
- `government-brp`
- `government-digid`
- `government-insurance`

The local environment uses Python 3.9 and produced end-of-life and LibreSSL warnings. The application and tests still completed, but the resit recording should use Python 3.10 or newer as required by the README.
