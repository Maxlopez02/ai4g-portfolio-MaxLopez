# Term 1 - Week 2: Loops & Functions

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

**Project title:** Prompt Coach

**My pair partner:** Newly assigned - add their name and GitHub username before submission.

**Tool we had to use:** Lovable

**SDG we had to address:** UN Sustainable Development Goal 4 - Quality Education

**What problem does it solve, and for whom?**
Beginner college and university students often ask AI broad questions and receive generic help, but do not yet know how to improve their request. Prompt Coach gives these learners guided practice in making a study prompt clearer.

**What did you build?**
The learner writes a goal and first prompt, receives AI feedback on Goal, Context, Constraints and Output, revises the prompt in their own words, and compares both drafts. The coach explains the prompt instead of completing the student's assignment.

**Link to the live thing (if any):**
[Complete portfolio submission](hackathon), including the working product, slides, ethical reflection and a captured end-to-end demo. The [Lovable-connected source mirror](https://github.com/Maxlopez02/prompt-coach-ai4g) keeps the original project integrated with Lovable.

**How do I run it?**
From the repository root, run `cd "Term 1/Week 2/hackathon/prompt-coach"`, `npm install`, then `npm run dev`. The runtime AI call needs the `LOVABLE_API_KEY` provided inside the connected Lovable environment; never commit this key.

**Who did what?**
Max built the first working Lovable prototype before a teammate was assigned, then used Codex to refine the source-code design, responsive behavior, motion, validation and accessibility. The new teammate's contribution has not happened yet and must be added here honestly once work is divided.

**Ethical reflection - what are the risks of your tool? Who could it harm?**
The feedback can be wrong, inconsistent or biased, so the interface labels it as guidance rather than a grade and asks learners to use their own judgment. Prompts are sent to an AI service, which could expose private information if a student enters names, student numbers or confidential coursework; the app warns against this. It currently requires internet access, a connected device, English and some familiarity with AI chat tools, so it can exclude learners with limited connectivity, lower digital confidence, accessibility incompatibilities or other language needs. A learner could also reuse the advice to request prohibited work from another tool. The coach reduces that risk by modelling explanations, hints and practice rather than finished answers, but course rules and disclosure are still necessary.

### Checklist
- [x] Prototype code (or export / workflow file) is in `hackathon/`
- [x] This week's slides are in `hackathon/`
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
Making an educational AI tool useful is not only about getting an AI response. The interaction needs to make the learner do something with the feedback and notice what changed.

**Where does this connect to "AI for Good"?**
Prompt Coach supports SDG 4 by giving beginner students structured practice in AI literacy: they draft, revise and reflect instead of outsourcing their work. It does not solve unequal access to education, and its learning effectiveness still needs testing with students.
