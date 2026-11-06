# How MigrationHelp works

This explanation follows one question through the actual Python code. It is meant for a live code walkthrough, not as a feature summary.

## The example

The user enters:

```text
Language: English
Stay: More than 4 months
City: The Hague
Question: I arrived for a one-year job. How do I get a BSN and what should I arrange next?
```

The program has four modules with different jobs:

| File | Responsibility | Does it use AI? |
| --- | --- | --- |
| `app.py` | Reads form values and decides what to show | No |
| `migrationhelp/safety.py` | Blocks empty input, likely identity numbers and emergencies | No |
| `migrationhelp/knowledge_base.py` | Stores reviewed facts and scores sources against the question | No |
| `migrationhelp/assistant.py` | Prepares the request, calls Gemini and validates its JSON | Only the `generate_content()` call |

## 1. Python checks the question before any API call

`app.py` calls `check_question(question)` and `is_emergency(question)`.

```python
safety = check_question(question)
if not safety.allowed:
    st.error(safety.message)
elif is_emergency(question):
    st.error("This sounds urgent ... call 112.")
else:
    answer = answer_question(...)
```

For the example question, `check_question()` returns `SafetyResult(True)`. For `My BSN is 123456789`, a regular expression detects a standalone nine-digit number and the function returns `SafetyResult(False, ...)`. Because the API call sits in the `else` branch, blocked input never reaches Gemini.

This filter is intentionally imperfect. It can block an innocent nine-digit number and it can miss other personal information. The interface therefore also tells the user not to enter private data.

## 2. Python chooses a small source pack

`select_sources()` converts the question to lowercase, expands recognised topic words, and gives each source one point for every matching term. The general moving guide receives one baseline point.

```python
normalised = question.casefold()
expanded_terms = set(normalised.split())

for topic, aliases in TOPIC_ALIASES.items():
    if any(alias in normalised for alias in aliases):
        expanded_terms.add(topic)
        expanded_terms.update(aliases)
```

The example contains `arrived`, `job`, and `BSN`. These terms make the moving guide and BRP page relevant. Related facts can also bring in DigiD and health insurance. Python keeps at most four sources.

The model does not choose these web pages and it does not browse the internet. The source list and facts are ordinary Python data in `knowledge_base.py`. A maintainer must review and update them.

## 3. Python builds the exact Gemini input

`prepare_request()` returns two values:

```python
sources, user_context = prepare_request(
    question, language, stay_length, municipality
)
```

`sources` is a list of `Source` objects. `user_context` is one string containing the requested language, stay length, city, question, and selected official facts. The question is wrapped in `<user_question>` tags so it remains clearly separated from the source pack.

This split matters because the prepared request can be tested without an API key. The test `test_prepared_request_contains_user_context_and_selected_sources` checks that the context contains the form values and every chosen source ID.

## 4. Python constrains the model output

`build_generation_config()` creates the settings used for every request:

```python
return types.GenerateContentConfig(
    system_instruction=SYSTEM_INSTRUCTIONS,
    response_mime_type="application/json",
    response_schema=GEMINI_RESPONSE_SCHEMA,
    max_output_tokens=700,
    temperature=0.2,
)
```

- The system instruction limits Gemini to the supplied facts and requires human referral for high-risk cases.
- The JSON schema requires six named fields.
- The token limit keeps the answer short.
- A low temperature reduces wording variation. It does not make the output automatically true.

## 5. This line performs the required AI task

`call_gemini()` makes the direct Google Gemini API call:

```python
response = api_client.models.generate_content(
    model=model,
    contents=user_context,
    config=config,
)
```

Gemini performs the part that ordinary keyword rules do not: it combines several selected facts, rewrites them in the requested language, and orders them for the specific question.

If the provider returns a temporary server error, the function tries one configured backup model. It does not retry forever. It returns both the response text and the model name so the interface can show which model produced the answer.

## 6. Python checks the answer after the API call

`_parse_answer()` uses Pydantic to read the JSON and reject missing or unexpected fields. It then applies checks that are specific to this product:

```python
valid_source_ids = validate_source_ids(data["source_ids"], sources)
```

`validate_source_ids()` compares the model's source IDs with the sources supplied in step 2. An invented ID leaves no valid citation and raises an error. The UI catches that error, hides the generated answer, and shows relevant official links instead.

The checks can verify structure and source membership. They cannot prove that every sentence is a correct interpretation of the source. That remaining risk is why official links and limitations stay visible.

## What is AI and what is normal Python?

| Action | Owner |
| --- | --- |
| Block a possible BSN | Python rule |
| Detect emergency phrases | Python rule |
| Score and select sources | Python lists, dictionaries and string matching |
| Translate and order the selected facts | Gemini |
| Require JSON fields | Gemini schema, then Python validation |
| Reject an invented source ID | Python rule |
| Decide what appears in the browser | Streamlit/Python |

## Evidence that the explanation matches the code

Run:

```bash
python -m pytest -q
```

The current suite has 11 tests. It covers input safety, emergency detection, source routing, request preparation, structured output, unexpected fields, invented citations, the direct Gemini request settings, and the single fallback attempt.

A live test on 6 November 2026 used `gemini-3.5-flash-lite`. It returned four steps and four source IDs for the example question. Python accepted only the IDs that were part of the prepared source pack.

## Questions each teammate must answer without reading this page

1. Why does the question not reach Gemini when a nine-digit number is present?
2. What is the difference between selecting sources and generating an answer?
3. Which exact line calls Gemini?
4. Why do we validate source IDs after asking Gemini for structured JSON?
5. What can still go wrong after all checks pass?
6. Which change would you make to add a new topic, and which test would you add first?

If either teammate cannot answer these questions or make a small tested change, the resit is not ready.
