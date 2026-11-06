# MigrationHelp — individual Hackathon 3 resit

- **Student:** Maximilian Lopez
- **Theme:** Equal access
- **SDG:** 10 — Reduced Inequalities

MigrationHelp is a Python and Streamlit prototype for adults who recently
arrived in the Netherlands and need a first route through routine public
administration. It uses the Google Gemini API to turn a small, reviewed pack of
official facts into short steps in the user's chosen language.

This is an **individual submission**. Maximilian designed the solution, built
and tested the Python application, prepared the evidence, and is responsible
for explaining the code and design decisions. Development assistance from AI
is disclosed in [AI_USE_REGISTER.md](AI_USE_REGISTER.md).

## Submission package

- [Working application and tests](migrationhelp/)
- [Individual presentation](presentation/MigrationHelp-Hackathon-3-Individual-Resit.pptx)
- [Full browser evidence walkthrough](demo/MigrationHelp-full-evidence-demo.mp4)
- [Short application demo](demo/MigrationHelp-demo.mp4)
- [Live Gemini verification record](demo/LIVE_TEST_RESULT.md)
- [Code walkthrough](HOW_THE_CODE_WORKS.md)
- [Ethical reflection](ETHICAL_REFLECTION.md)
- [Rubric evidence map](RUBRIC_EVIDENCE.md)
- [Submission checklist](SUBMISSION_CHECKLIST.md)

## Problem and intended user

New arrivals must deal with several Dutch organisations while language,
deadlines and the order of steps all matter. The prototype is for an adult who
recently moved to the Netherlands for work, study or family, has limited Dutch,
and needs general information about registration, a BSN, DigiD, health
insurance or a residence-permit route.

It is not for asylum decisions, appeals, emergencies, medical or legal advice,
or case-specific eligibility decisions. Those questions must go to a qualified
human or the responsible authority.

## How the product works

1. The user chooses a language and enters a practical question.
2. Python blocks empty, oversized, sensitive or urgent input before any API
   call.
3. A deterministic router selects relevant facts from reviewed Government.nl
   and IND pages.
4. Gemini transforms those facts into a short, structured route.
5. Python validates the JSON and rejects source IDs that were not supplied.
6. The interface shows the answer, limitations and official links. If the API
   or validation fails, the generated answer stays hidden and the links remain.

The AI explains and sequences reviewed information; it does not decide whether
someone qualifies for a service or permit.

## Run locally

Requires Python 3.10+ and a Google Gemini API key. The key must remain in a
local `.env` file and must never be committed.

```bash
cd "Resit/Week 3/hackathon/migrationhelp"
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
```

## Tests

```bash
cd "Resit/Week 3/hackathon/migrationhelp"
python -m pytest -q
```

The suite contains 11 tests covering source routing, input safety, emergency
handling, request preparation, structured output, unexpected fields, invented
citations, direct Gemini configuration, model reporting and temporary-error
fallback.

## Important limitation

The official-source pack is curated rather than retrieved live. It is
auditable, but it can become outdated. A real deployment would require regular
source review, multilingual user testing, professional review, accessibility
testing and a maintained human-referral route.
