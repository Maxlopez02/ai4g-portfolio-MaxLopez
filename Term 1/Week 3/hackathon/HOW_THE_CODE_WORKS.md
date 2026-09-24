# How the Python and Gemini API call work

## The 30-second explanation

> The user types a question in Streamlit. Python first blocks empty input, likely identity numbers and emergencies. It then selects a few relevant facts from our list of official Government.nl and IND sources. Python sends the question, chosen language and those facts to Gemini. Gemini returns JSON with an answer, steps, a risk level and source IDs. Python checks that the JSON has the expected fields and that every cited source ID exists in our source list. Only then does Streamlit show the answer and official links. If the API fails or validation fails, the app shows no AI answer.

## The one line that makes it AI powered

The actual API request is in `migrationhelp/migrationhelp/assistant.py`:

```python
response = api_client.models.generate_content(
    model=model,
    contents=user_context,
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_INSTRUCTIONS,
        response_mime_type="application/json",
        response_schema=GEMINI_RESPONSE_SCHEMA,
        max_output_tokens=700,
        temperature=0.2,
    ),
)
```

What each part means:

- `model`: which Gemini model to use.
- `contents`: the user's question plus the selected official facts.
- `system_instruction`: rules such as “do not guess” and “use only supplied facts.”
- `response_mime_type`: asks Gemini to return JSON instead of free-form text.
- `response_schema`: lists the exact fields the app expects.
- `max_output_tokens`: keeps answers short.
- `temperature=0.2`: reduces randomness.

If Gemini returns a temporary server error, Python makes one automatic call to a backup Gemini model. If that also fails, the app shows a safe error and keeps the official links visible.

## The simple data flow

```text
User question
    ↓
Python safety checks
    ↓
Python selects official source facts
    ↓
Python calls Gemini once
    ↓
Gemini returns structured JSON
    ↓
Python checks fields and source IDs
    ↓
Streamlit displays steps and official links
```

## What Gemini does

Gemini does two necessary jobs:

1. It rewrites official information in the selected language and in simpler words.
2. It orders the information into steps that fit the user's question.

Gemini does **not** search the internet, decide a residence case, create the source facts, or submit a government form.

## What normal Python does

- Reads the form values.
- Checks input length and possible private numbers.
- Uses lists and dictionaries to choose source facts.
- Builds the prompt.
- Sends the API request.
- Parses the JSON response.
- Rejects unknown source IDs or malformed output.
- Shows an error if the request fails.

## Five questions a teacher may ask

**Why use an API?**
The program sends input to a hosted Gemini model and receives a generated response. The model does not run on the laptop.

**Why not use Gemini's general knowledge?**
Migration rules can change and a confident wrong answer can harm someone. The prompt limits Gemini to a reviewed source pack.

**What happens when Gemini gives a bad response?**
Python validates the structure and source IDs. Invalid output is discarded and the app shows official links instead.

**Why is the API necessary?**
A static page could list links, but it could not adapt the explanation, order and language to each question in the same way.

**Does the app store personal data?**
The app does not write conversations to disk or keep chat history. Google still processes the API request, so the interface tells users not to enter identity or medical details.
