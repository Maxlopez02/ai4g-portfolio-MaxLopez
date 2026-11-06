# AI use and human checks

The original submission used AI for too much of the visible work. This resit separates the AI inside the product from AI used to assist development.

## AI inside MigrationHelp

The required tool is the Google Gemini API. Gemini receives a question plus a small pack of reviewed facts. It returns structured JSON that adapts and orders those facts. Python performs input checks, source selection, output validation, error handling, and display.

Gemini is not used to search the open web, make residence decisions, or decide which identity data is safe to send.

## AI used while developing the resit

| Item | AI contribution | Required human check before submission |
| --- | --- | --- |
| Python refactor | Codex drafted the split between request preparation, configuration, API call, and validation | Maximilian explains each function, changes one test, and runs the suite on camera |
| Tests | Codex drafted additional tests for request content, model tracking, and unexpected fields | Both teammates read the assertions and explain what failure each test catches |
| Documentation | Codex drafted the first version | Each teammate rewrites their own speaking notes and removes wording they cannot explain |
| Presentation | Codex helped build an editable evidence deck | The team checks every claim against code or a named source and presents without AI narration |
| Product response | Gemini generates the user route | Python validates JSON and source IDs; the user sees official links and limits |

## Rules for the resit recording

- Use both students' real voices. Do not use an AI voice, avatar, or generated presenter.
- Record one continuous take apart from trimming the start and end.
- Show the live app, source code, test result, and one API response.
- Each student explains code they reviewed and changed themselves.
- Do not read a generated script word for word.
- Keep a real contribution record: commits, dated notes, test output, or screen recording.

AI assistance is disclosed. It does not count as evidence that a student understands the work.
