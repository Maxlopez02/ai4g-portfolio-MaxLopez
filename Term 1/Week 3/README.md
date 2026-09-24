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

> Your tool and your SDG for this hackathon are announced at the **start of Friday's class**.
> Write them down here once you know them.

**Project title:**

MigrationHelp — a source-grounded migration information navigator

**My pair partner:**

_Add your randomly assigned partner's name before submission._

**Tool we had to use:**

Google Gemini API called directly from Python (Streamlit application)

**SDG we had to address:**

SDG 10 — Reduced Inequalities

**What problem does it solve, and for whom?**
_Name a real, specific user. "Everyone" is not a user._

Recently arrived adults in the Netherlands with limited Dutch must quickly navigate multiple public organisations. MigrationHelp reduces this administrative information gap by turning reviewed official information into a short route in the user's language. It is not for asylum decisions, emergencies, legal representation or medical advice.

**What did you build?**
_Two or three sentences. What can a user actually do with it?_

A user selects a language and stay length, asks a routine migration-administration question, and receives ordered next steps plus clickable Government.nl or IND sources. The Python app makes a live Google Gemini API call, validates its structured answer and citations, blocks likely identity details, and fails safely when the AI output cannot be verified.

**Link to the live thing (if any):**
_Deployed URL, workflow export, video demo - whatever proves it works._

See the [working product, documentation and demo materials](hackathon/), including the [recorded live demo](hackathon/demo/MigrationHelp-demo.mp4).

**How do I run it?**
_Short instructions so someone else can start it._

From `hackathon/migrationhelp`: create a Python virtual environment, install `requirements.txt`, copy `.env.example` to `.env`, add `GEMINI_API_KEY`, and run `streamlit run app.py`. Full steps are in the project README.

**Who did what?**
_Be honest about the split of work between you and your partner._

- Maximilian Lopez: Python and Streamlit implementation, Gemini API integration, validation and safety controls, testing, demo, documentation and presentation preparation.
- Quinten van Ingen: Project concept and initial idea.
- AI assistance: OpenAI Codex helped draft, test and document the prototype and prepare the presentation; the team reviewed the working app and must be able to explain it.

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
