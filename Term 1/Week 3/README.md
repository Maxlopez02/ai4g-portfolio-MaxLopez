# Term 1 - Week 3: Lists & Dictionaries

---

## 1. Homework & workshop assignments -> [`homework/`](homework/)

**What was the assignment?**

**What did I hand in?**
_List the files, or link to them. Notebook exports, screenshots, scripts._

**What did I find difficult, and how did I solve it?**

### Checklist
- [ ] My workshop / homework files are in `homework/`
- [ ] Everything runs without errors, or I explained what does not and why

---


## 2. Hackathon prototype -> [`hackathon/`](hackathon/)

**Project title:**

MigrationHelp — a source-grounded migration information navigator

**My pair partner:**

Quinten van Ingen

**Tool we had to use:**

Google Gemini API called directly from Python (Streamlit application)

**SDG we had to address:**

SDG 10 — Reduced Inequalities

**What problem does it solve, and for whom?**

Recently arrived adults in the Netherlands with limited Dutch must quickly navigate multiple public organisations. MigrationHelp reduces this administrative information gap by turning reviewed official information into a short route in the user's language. It is not for asylum decisions, emergencies, legal representation or medical advice.

**What did you build?**

A user selects a language and stay length, asks a routine migration-administration question, and receives ordered next steps plus clickable Government.nl or IND sources. The Python app makes a live Google Gemini API call, validates its structured answer and citations, blocks likely identity details, and fails safely when the AI output cannot be verified.

**Proof that it works:**

See the [working product and resit materials](hackathon/). The technical evidence includes 11 passing tests and a fresh live Gemini call. A new two-person live defence is still required because the original generated/silent videos do not prove balanced work or code understanding.

**How do I run it?**
_Short instructions so someone else can start it._

From `hackathon/migrationhelp`: create a Python virtual environment, install `requirements.txt`, copy `.env.example` to `.env`, add `GEMINI_API_KEY`, and run `streamlit run app.py`. Full steps are in the project README.

**Who did what?**

- Original submission: Maximilian completed most implementation and submission work; Quinten contributed the initial concept. This split was not balanced.
- Resit: Both students must complete the responsibilities and evidence in [`hackathon/TEAM_RESIT_LOG.md`](hackathon/TEAM_RESIT_LOG.md) before submission.
- AI assistance: Codex drafted parts of the resit. The required disclosure and human checks are in [`hackathon/AI_USE_REGISTER.md`](hackathon/AI_USE_REGISTER.md).

**Ethical reflection - what are the risks of your tool? Who could it harm?**
_Every hackathon requires this. One honest paragraph beats three vague ones._

The biggest risk is authoritative-sounding wrong guidance to a newcomer who has less ability to verify it. A wrong deadline, route or translation could cost time or money, delay care, or harm a residence process. The prototype limits this by using a small reviewed official source pack, demanding structured output and valid source IDs, showing the original links, blocking likely identity details, referring case-specific and urgent questions to humans, and showing no answer when validation fails. These controls reduce harm but do not make the chatbot an authority; real deployment would require professional review, multilingual user testing, accessibility testing and scheduled source updates.

### Checklist
- [x] Prototype code (or export / workflow file) is in `hackathon/`
- [x] This week's slides are in `hackathon/presentation/`
- [x] The prototype actually runs, and I wrote down how to run it
- [x] Ethical reflection written above

---

## 3. Presentation -> [`presentation/`](presentation/)

*Only fill this in for the week your group was selected to present. You need at least **one** of these across the whole term.*

- [ ] My group presented in this week
- [ ] Slides are in `presentation/`
- [ ] Proof of the live demo is in `presentation/` (recording, screenshots, or link)

**How did it go? What would I do differently next time?**

---

## 4. Reflection

**What is the most important thing I learned this week?**

**Where does this connect to "AI for Good"?**
_One concrete link to ethics, sustainability or social impact._
