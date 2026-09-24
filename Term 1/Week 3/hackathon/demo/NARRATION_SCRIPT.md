# MigrationHelp narrated demo

The final demo is a short screen recording with one live Gemini response, an on-screen Python code explanation, spoken narration and burned-in captions.

## Narration timeline

| Time | Narration |
| --- | --- |
| 00:00–00:09 | MigrationHelp helps newcomers understand Dutch paperwork. The user selects a language, expected stay and city, without entering identity numbers. |
| 00:09–00:20 | After one practical question, Python checks for private information and emergencies, then selects matching facts from official Dutch government sources. |
| 00:20–00:32 | One live Gemini API call sends the question and source pack. The code requests structured JSON with a direct answer, steps, risks and source IDs. |
| 00:32–00:48 | Python validates every required field and rejects invented sources before displaying anything. If the API fails, it hides the answer and keeps official links visible for verification. |

## Code shown in the video

```python
response = api_client.models.generate_content(
    model=model,
    contents=user_context,
    config=config,
)
answer = _parse_answer(response.text, sources)
```

`generate_content` makes the live Gemini call. `_parse_answer` checks the JSON fields, limits the result to four steps and rejects source IDs that were not in the supplied official source pack.

## Recording safety

- The example question is fictional.
- No API key, `.env` file, identity number or private account is shown.
- Captions are burned into the submitted MP4 so they remain visible in any video player.
