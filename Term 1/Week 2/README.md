# Term 1 - Week 2: Flow State & n8n Automation

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

**Project title:** AI Study Stress Coach

**My pair partner:** Lili Tarnok

**Tool we had to use:** n8n

**SDG we had to address:** SDG 3 - Good Health and Well-being, including mental health

**What problem does it solve, and for whom?**
University and applied-science students can feel overwhelmed by stress, poor sleep, workload, and approaching deadlines but may not know which manageable step to take first. The project provides a low-pressure check-in and immediate general guidance while keeping diagnosis and serious concerns with people.

**What did you build?**
I built a seven-node n8n workflow. A student submits a short form; the workflow cleans the input, calculates a transparent project stress score, classifies it as Low, Moderate, or High, asks an OpenAI node for short personalised guidance, emails a visual stress snapshot, and logs the result in Google Sheets.

**Link to the live thing (if any):**
- [Importable n8n workflow](hackathon/workflow/ai-study-stress-coach.json)
- [Corrected demo video](hackathon/demo/ai-study-stress-coach-demo.mp4)
- [Presentation deck](hackathon/presentation/ai-study-stress-coach-deck.pdf)
- [Full project documentation](hackathon/README.md)

**How do I run it?**
Import the workflow JSON into n8n, connect OpenAI, Gmail, and Google Sheets credentials, select a restricted Sheet and confirm the column mapping, test with fictional data, then publish the form and activate the workflow. Each form submission triggers the flow automatically. Detailed instructions are in the [project README](hackathon/README.md#how-to-run-it).

**Who did what?**
I designed and built the n8n flow, scoring rule, AI safety instructions, formatted email, Google Sheets logging, testing, and demo. Lili Tarnok created the PowerPoint presentation. AI tools supported the personalised response inside the product and helped polish supporting materials.

**Ethical reflection - what are the risks of your tool? Who could it harm?**
I would not trust this automation to make health decisions for me. Its score is a simple project rule, and the AI can misunderstand context or give advice that is generic, unsuitable, late, or unavailable. A student might mistake a High label for a diagnosis, while a failed email could create false reassurance because the form confirms submission before delivery finishes. Automation should stop at low-risk check-in, general study and self-care suggestions, and signposting. A trusted person, study counsellor, or healthcare professional should take over whenever someone feels unable to cope, may be at risk, needs a diagnosis or treatment, or asks for human help. Real use would also require execution monitoring, visible support options, restricted data access, and a deletion period.

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
I learned how to combine deterministic rules with generative AI in one automation. The rules keep the category and escalation logic visible, while AI is used only where adaptable wording adds value.

**Where does this connect to "AI for Good"?**
The project connects to SDG 3 by reducing friction around student well-being support, but it also shows why a beneficial AI system needs limits. The workflow gives general, low-risk guidance and directs higher-concern situations toward people instead of pretending that automation can replace professional care.
