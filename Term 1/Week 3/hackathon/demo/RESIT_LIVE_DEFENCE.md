# Hackathon 3 resit live defence

Record a single 5–7 minute take with both teammates' real voices. A simple screen recording with microphones is enough. The purpose is to prove understanding, not production quality.

Do not use the old generated caption video as the main resit evidence. Do not use AI narration. Trimming the start and end is fine; avoid scripted overlays and montage editing.

## Before recording

- Both teammates have completed and signed `TEAM_RESIT_LOG.md`.
- Each teammate has changed and tested code in the area they present.
- The API key is loaded locally but never shown.
- The test suite passes.
- Use fictional input only.

## Recording order

### 1. Feedback and claim, together, 30 seconds

State plainly:

- The original submission did not prove the required AI tool, SDG link, scope, balanced work, or understanding well enough.
- The resit will show those points directly in the live product and code.

Do not read a polished paragraph. Each person should speak in their own words.

### 2. K2 and user need, Quinten, 50 seconds

Show the SDG slide and the named sources. Explain the causal link:

```text
limited Dutch and unfamiliar government structure
less ability to find and sequence public information
less equal access to registration and services
MigrationHelp gives a first route and original official links
```

Also state the boundary: this prototype does not decide asylum or residence cases.

### 3. Source selection and safety, Quinten, 90 seconds

Open `knowledge_base.py` and explain one `Source` record, `TOPIC_ALIASES`, and the score in `select_sources()`.

Then open `safety.py` and explain why a standalone nine-digit number is blocked before the API call.

Run one routing or safety test that Quinten added or improved. Explain what would fail if the code were wrong.

### 4. K1 direct Gemini call, Maximilian, 90 seconds

Open `assistant.py` and follow these functions in order:

1. `prepare_request()`
2. `build_generation_config()`
3. `call_gemini()`
4. `_parse_answer()`

Point at the actual `api_client.models.generate_content(...)` line. Explain the values in `contents` and `config`, what Gemini contributes, and why the result returns to Python for validation.

Run the API/configuration test or output-validation test that Maximilian reviewed or changed.

### 5. K3 end-to-end scope, both, 90 seconds

Run the app and submit:

```text
I arrived for a one-year job. I have not registered yet. How do I get a BSN and what should I arrange after that?
```

Show:

- the live connection indicator;
- ordered steps and preparation items;
- the limitation message;
- official source links; and
- the expanded evidence trail with the Gemini model and validated source IDs.

Then enter `My BSN is 123456789. What should I do?` and show that Python blocks it before Gemini.

### 6. Checks, limits, and work split, both, 60 seconds

Maximilian explains one output check and what happens when Gemini fails. Quinten explains one limitation that the tests do not solve, such as an outdated source or unequal translation quality.

Show the completed contribution log briefly. Each person names the file and test they own.

## Questions the assessor may interrupt with

Both teammates should be ready to answer:

- Which exact line uses Gemini?
- What would still work if the Gemini call were removed?
- Why does a JSON schema not guarantee truth?
- How does the program stop an invented citation?
- Why is SDG 10 a better fit than a general statement that migration is difficult?
- What part of the code did you personally change for the resit?

## Recording acceptance checklist

- [ ] Both real voices are audible.
- [ ] Both students explain code, not only features.
- [ ] The direct Gemini call appears on screen.
- [ ] One live Gemini result appears on screen.
- [ ] One local blocked-input case appears on screen.
- [ ] The SDG 10 causal link and named user are stated.
- [ ] Each student runs or explains a test they own.
- [ ] No key, private data, or real user case appears.
- [ ] The video is understandable without generated overlays.
