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

These results prove the direct API path works. The recorded browser flow is included as [`MigrationHelp-demo.mp4`](MigrationHelp-demo.mp4); it shows a real question, the generated route, the high-risk label and the official source links.
