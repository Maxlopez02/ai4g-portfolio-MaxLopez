# Team resit responsibility and evidence log

## Why this log exists

The original split was not balanced: Maximilian built almost the whole prototype while Quinten contributed the initial idea. The resit must add real work from both students. This file must describe completed work only; a planned task is not a contribution.

Codex prepared technical drafts on 6 November 2026. Those drafts count as AI assistance, not as student work, until a student reviews, changes, tests, and explains them.

## Balanced resit responsibilities

| Area | Maximilian | Quinten |
| --- | --- | --- |
| Product code | Own `assistant.py`: prepared request, Gemini call, fallback, and output validation | Own `knowledge_base.py` and `safety.py`: source records, keyword routing, privacy and emergency rules |
| Tests | Explain and maintain API/configuration and output-validation tests | Add and maintain routing and safety tests, including one case found during manual testing |
| Evidence | Demonstrate K1 with the live API call and explain why the model is necessary | Demonstrate K2 and K3 with source evidence, the user route, and a blocked or out-of-scope case |
| Ethics | Explain residual model risk and fail-closed behaviour | Explain unequal impact, source maintenance, and human referral |
| Presentation | Present the Gemini and validation code | Present the SDG evidence, source selection, and safety code |

## Required contribution evidence

Do not tick a row until the named person did the work.

| Person | Evidence required | Status | Link, commit, or dated note |
| --- | --- | --- | --- |
| Maximilian | Read `assistant.py`, make one justified change, and run the relevant tests | [ ] | |
| Maximilian | Explain the direct Gemini call and one rejected output without notes | [ ] | |
| Quinten | Recheck at least two official sources and record whether facts changed | [ ] | |
| Quinten | Add or improve one routing/safety test, then make it pass | [ ] | |
| Quinten | Explain `select_sources()` and `check_question()` without notes | [ ] | |
| Both | Run the whole test suite together and discuss one limitation the tests cannot catch | [ ] | |
| Both | Record the one-take live defence using real voices | [ ] | |

## Work session notes

Add short factual notes here. Include the date, person, file or test, what changed, and why.

| Date | Person | File or test | Change and reason |
| --- | --- | --- | --- |
| | | | |

## Final declaration

Before submission, both students should replace the blank lines below with their own words.

**Maximilian:** I can explain _______________________________________________.

**Quinten:** I can explain __________________________________________________.

**Shared limitation we still accept:** _______________________________________.
