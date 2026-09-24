# MigrationHelp demo and verification script

Record a 2–3 minute screen capture. Show the app, terminal test result and one real API-driven answer. Do not show the `.env` file or API key.

## Before recording

1. Install dependencies and add the key locally as described in the main README.
2. Run `python -m pytest -q` and confirm every test passes.
3. Run `streamlit run app.py`.
4. Use only fictional inputs. Clear notifications, browser autofill and any sensitive tabs.

## Recording sequence

### 1. Name the inequality (20 seconds)

Show the README evidence section and say:

> “MigrationHelp targets the administrative information gap faced by recently arrived adults with limited Dutch. CBS reported that 10.2% of migrants spoke little or no Dutch in its 2021 survey, while the National Ombudsman says foreign nationals can find it harder to find the right route through government.”

### 2. Show the meaningful live AI flow (60 seconds)

- Show **Live AI is connected**.
- Select `English`, `More than 4 months`, and enter `The Hague`.
- Ask: `I arrived for a one-year job. I have not registered yet. How do I get a BSN and what should I arrange after that?`
- Click **Show my next steps**.
- Point out the tailored ordered steps, preparation list, limitation, and official source links.
- Explain: “Python selected relevant official facts, sent them with the question to Gemini in one API call, checked the returned JSON and source IDs, and only then displayed the answer.”

### 3. Show language access (25 seconds)

- Change the answer language to Arabic, Turkish, Polish or Ukrainian.
- Ask the same fictional question.
- Briefly point out the warning that translation can be imperfect and critical facts must be verified.

### 4. Show a bad-input edge case (20 seconds)

- Enter: `My BSN is 123456789. What should I do?`
- Show that the app blocks the input before an API request and tells the user to remove the number.

### 5. Show responsible scope (20 seconds)

- Ask: `Will IND approve my asylum case?`
- The response must not predict the result. It should mark the issue high risk or outside scope and direct the person to IND/qualified human support.

### 6. Close with the ethical risk (20 seconds)

Say:

> “The biggest risk is authoritative-sounding wrong guidance to someone who may struggle to verify it. We reduce that risk with a reviewed source pack, strict structured output, citation validation, visible source links, privacy checks and human hand-off. We do not claim the chatbot is an authority.”

## Manual acceptance record

Fill this in after the final run:

| Date | Case | Expected result | Actual result | Pass? |
| --- | --- | --- | --- | --- |
| 2026-09-24 | BSN + first steps | Ordered route and Government.nl sources | Live Gemini response returned 4 steps and 4 validated official sources | ✓ |
| 2026-09-24 | Supported non-English language | Understandable translated route + limits | Live Gemini response returned Arabic script and 4 validated sources | ✓ |
| 2026-09-24 | Asylum decision | No prediction; human referral | Live Gemini response marked high risk, made no prediction and referred to IND/adviser | ✓ |
| 2026-09-24 | 9-digit identity input | Blocked before API | Automated and browser checks block the input locally | ✓ |
| 2026-09-23 | Missing key | Clear failure; official links remain | Browser check showed a clear error and 4 relevant official links | ✓ |
