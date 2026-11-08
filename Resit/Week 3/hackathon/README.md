# MigrationHelp — individual Hackathon 3 resit

- **Student:** Maximilian Lopez
- **Theme:** Equal access
- **SDG:** 10 — Reduced Inequalities

MigrationHelp is a Python and Streamlit prototype for newcomers who need help
finding their first steps in Dutch public administration. It uses the Google
Gemini API to turn a small set of official Government.nl and IND facts into a
short answer in the user's chosen language.

## Submitted work

- [Application code](migrationhelp/)
- [Demo video](demo/MigrationHelp-demo.mp4)
- [Presentation](presentation/MigrationHelp-Hackathon-3-Individual-Resit.pptx)
- [Ethical reflection](ETHICAL_REFLECTION.md)

## Run the app

```bash
cd "Resit/Week 3/hackathon/migrationhelp"
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
```

Add a Google Gemini API key to the local `.env` file before starting the app.
The key is not included in this repository.

The app checks the question, selects relevant official facts, asks Gemini to
format them into clear steps, and validates the response before showing it. It
provides general information only and does not replace the municipality, IND,
an insurer, or professional legal or medical advice.

Codex assisted with code review, testing suggestions, documentation wording,
and presentation editing. I remain responsible for the submission and for
being able to explain the code and design choices.
