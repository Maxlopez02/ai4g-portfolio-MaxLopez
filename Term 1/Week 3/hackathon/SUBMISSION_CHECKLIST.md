# MigrationHelp submission checklist

The technical submission package is complete and aligned to the Hackathon 3 rubric.

## Ready to submit

- [x] Working Python/Streamlit product in [`migrationhelp/`](migrationhelp/)
- [x] Direct live Gemini API call through the official `google-genai` Python SDK
- [x] Setup and run instructions in [`README.md`](README.md)
- [x] Beginner-friendly code explanation in [`HOW_THE_CODE_WORKS.md`](HOW_THE_CODE_WORKS.md)
- [x] Source-backed problem definition and SDG 10 link in [`README.md`](README.md)
- [x] Specific user group and explicit exclusions
- [x] Edge-case handling for sensitive data, emergencies, invalid AI output and API failure
- [x] Honest ethical reflection in [`ETHICAL_REFLECTION.md`](ETHICAL_REFLECTION.md)
- [x] Rubric evidence map in [`RUBRIC_EVIDENCE.md`](RUBRIC_EVIDENCE.md)
- [x] Nine passing automated tests recorded in [`demo/LIVE_TEST_RESULT.md`](demo/LIVE_TEST_RESULT.md)
- [x] Live API demo recording with narration, burned-in captions and a Python API-call code card in [`demo/MigrationHelp-demo.mp4`](demo/MigrationHelp-demo.mp4)
- [x] Eight-slide presentation, including the real Python API call, in [`presentation/MigrationHelp-Hackathon-3-final.pptx`](presentation/MigrationHelp-Hackathon-3-final.pptx)
- [x] `.env` is ignored and the API key is not included in submission files

## Team details completed

- [x] Maximilian Lopez and Quinten van Ingen are named in both README files and on the presentation cover.
- [x] Contributions state that Quinten developed the concept and initial idea, while Maximilian completed the implementation and technical submission work.

Check for remaining placeholders with:

```bash
rg -n "add name|replace with the work|actual contribution" . ../README.md
```

## Final hand-in steps

1. Run `python -m pytest -q` once more from `migrationhelp/`.
2. Push this Week 3 folder to the GitHub repository.
3. Open the GitHub links while logged out to confirm the README, MP4 and PPTX are accessible.
4. Submit the GitHub repository link in the HHS submission sheet.

Do not commit `migrationhelp/.env` or paste the Gemini key into screenshots, documentation, issues or commits.
