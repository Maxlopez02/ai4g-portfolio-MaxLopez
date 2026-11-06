# Rubric evidence map

This file points assessors to visible evidence. It is not a claim that points are automatic; the team must run and explain the work.

## Knockout criteria

| Criterion | Evidence in this repository |
| --- | --- |
| K1 — AI tool | `migrationhelp/migrationhelp/assistant.py` makes a live call to Google's Gemini API using the official Python SDK. Gemini translates and orders selected official facts for the user's situation. The expanded evidence trail displays the model used and the source IDs Python accepted. `demo/LIVE_TEST_RESULT.md` records a fresh successful call on 6 November 2026. |
| K2 — SDG relevance | The README defines the administrative information gap, connects it to SDG 10, identifies recent adult newcomers with limited Dutch, and supports scale/context with CBS and National Ombudsman sources. |
| K3 — Scope | This is an end-to-end information-navigation workflow, not a prompt-and-response screen. It handles five administrative topics and six answer languages, then runs input checks, evidence selection, a live AI transformation, schema and source-ID validation, risk labelling, actionable output, official-link handoff and a safe failure path. |

## Scored criteria (10 points)

| Criterion | Evidence for “fully met” |
| --- | --- |
| 1. Problem definition (2) | README section “The specific inequality”: what (administrative information gap), whom (recent adult newcomers with limited Dutch), where (Netherlands), when (first administrative steps after arrival), significance (3 million foreign-born residents; 10.2% with little/no Dutch), and official sources. |
| 2. User group (2) | README “Intended users — and who is left out”: situation, needs, phone/simple-language conditions, supported languages, and explicit exclusions. |
| 3. Solution description (2) | README seven-step input-to-output flow and architecture diagram; `HOW_THE_CODE_WORKS.md` follows one example through the safety check, source score, prepared request, `generate_content()` call, JSON parsing and source-ID validation. The live defence requires each teammate to explain and test the code they own. |
| 4. Problem–solution fit (1) | README links the information/language gap to multilingual sequencing. A static link list cannot adapt wording, language and order to the user's stay length and question; the LLM does that while sources remain constrained. |
| 5. Working prototype (1) | `streamlit run app.py` gives an end-to-end UI. `demo/LIVE_TEST_RESULT.md` records successful live calls. Eleven automated tests verify deterministic controls, prepared context, output rejection, model tracking and temporary-error fallback. The new two-person resit recording must show the live app, code and tests in one take. |
| 6. Ethical reasoning (2) | `ETHICAL_REFLECTION.md` names a prototype-specific risk, concrete harms, unequal impact, safeguards already implemented, residual limitations and next actions. |

## Final pre-submission proof

The technical K1–K3 evidence exists. The resit still requires the unchecked human evidence in `RESIT_SUBMISSION_CHECKLIST.md`: balanced completed contributions, a one-take two-person code defence, and an updated source check. Those items cannot be replaced by generated documentation.
