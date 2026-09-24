# Rubric evidence map

This file points assessors to visible evidence. It is not a claim that points are automatic; the team must run and explain the work.

## Knockout criteria

| Criterion | Evidence in this repository |
| --- | --- |
| K1 — AI tool | `migrationhelp/migrationhelp/assistant.py` makes a live call to Google's Gemini API using the official Python SDK. The LLM translates and adapts several official facts into a user-specific route. `demo/LIVE_TEST_RESULT.md` records successful live calls. |
| K2 — SDG relevance | The README defines the administrative information gap, connects it to SDG 10, identifies recent adult newcomers with limited Dutch, and supports scale/context with CBS and National Ombudsman sources. |
| K3 — Scope | The working app handles five real administrative topics, six answer languages, source routing, structured answers, verified citations, privacy checks, emergency routing and API failure. |

## Scored criteria (10 points)

| Criterion | Evidence for “fully met” |
| --- | --- |
| 1. Problem definition (2) | README section “The specific inequality”: what (administrative information gap), whom (recent adult newcomers with limited Dutch), where (Netherlands), when (first administrative steps after arrival), significance (3 million foreign-born residents; 10.2% with little/no Dutch), and official sources. |
| 2. User group (2) | README “Intended users — and who is left out”: situation, needs, phone/simple-language conditions, supported languages, and explicit exclusions. |
| 3. Solution description (2) | README seven-step input-to-output flow and architecture diagram; `HOW_THE_CODE_WORKS.md` explains the exact API call in beginner-friendly language; slide 5 contains the real `generate_content()` code and explains each argument; source files show deterministic retrieval, direct Gemini call, structured JSON, validation and interface output. |
| 4. Problem–solution fit (1) | README links the information/language gap to multilingual sequencing. A static link list cannot adapt wording, language and order to the user's stay length and question; the LLM does that while sources remain constrained. |
| 5. Working prototype (1) | `streamlit run app.py` gives an end-to-end UI. `demo/LIVE_TEST_RESULT.md` records successful routine, Arabic and high-risk Gemini calls. `demo/MigrationHelp-demo.mp4` records a real browser request and validated answer. Nine automated tests verify deterministic controls and temporary-error fallback. |
| 6. Ethical reasoning (2) | `ETHICAL_REFLECTION.md` names a prototype-specific risk, concrete harms, unequal impact, safeguards already implemented, residual limitations and next actions. |

## Final pre-submission proof

- [x] Add both team members' names and honest contribution split.
- [x] Run all automated tests and capture the passing result.
- [x] Run at least the three live manual cases in `demo/DEMO_SCRIPT.md`.
- [x] Record an end-to-end live API response with the URL and sources visible.
- [x] Add the screen recording under `demo/` (under GitHub's file limit).
- [x] Add the team slides.
- [x] Confirm that the live demo uses the direct Gemini API path required by the brief.
- [x] Replace team placeholders.
- [ ] Verify every public URL on submission day.
- [x] Make sure `.env` is ignored and no key is included in the repository files.
