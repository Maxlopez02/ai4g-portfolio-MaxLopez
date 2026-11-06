# How MigrationHelp works

The code separates deterministic safety and evidence handling from the one
task that uses Gemini.

| File | Responsibility |
|---|---|
| `app.py` | Reads the form and decides what the user sees |
| `migrationhelp/safety.py` | Blocks unsafe or unsuitable input before an API call |
| `migrationhelp/knowledge_base.py` | Stores reviewed facts and selects relevant sources |
| `migrationhelp/assistant.py` | Prepares the Gemini request, calls the API and validates the JSON response |

For a question about getting a BSN after moving to The Hague, the flow is:

1. `check_question()` and `is_emergency()` run first. A likely identity number
   or urgent-danger phrase stops the AI flow.
2. `select_sources()` scores the question against the reviewed source pack and
   keeps at most four relevant sources.
3. `prepare_request()` combines the chosen language, stay length, city,
   question and selected facts into testable input.
4. `call_gemini()` makes the direct API request with a strict response schema,
   low temperature and output limit.
5. `_parse_answer()` validates required fields and rejects source IDs that were
   not present in the prepared source pack.
6. `app.py` displays a valid route or, on failure, hides generated guidance and
   keeps official links visible.

Gemini performs the non-trivial language and sequencing step. Python controls
the boundary around it. Validation reduces risk, but it cannot prove that every
sentence is a perfect interpretation of the source, which is why limitations
and official links remain visible.
