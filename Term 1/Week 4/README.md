# Term 1 - Week 4: Strings, Text & Files

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
Through the Glass

**My pair partner:**
Pair submission. My partner created the core ComfyUI workflow; I prepared the documented demo and repository submission.

**Tool we had to use:**
ComfyUI with SDXL, ControlNet and an image-to-video workflow.

**SDG we had to address:**
SDG 13: Climate Action, especially Target 13.3 on climate education and awareness.

**What problem does it solve, and for whom?**
_Name a real, specific user. "Everyone" is not a user._

Climate change can feel too distant to motivate action. The project turns a long environmental timeline into a 31-second visual story for European higher-education students aged 18–24 who understand climate science but feel anxious or powerless.

**What did you build?**
_Two or three sentences. What can a user actually do with it?_

We built a short AI-generated climate film that holds one interior window view steady while the exterior changes from a healthy landscape to industry, renewable energy, destruction and a lifeless future. We also documented the two-stage ComfyUI pipeline and produced a captioned walkthrough that explains how the key frame and motion clip were generated.

**Link to the live thing (if any):**
_Deployed URL, workflow export, video demo - whatever proves it works._

- [Final film on Google Drive](https://drive.google.com/file/d/1OYYY5sTjCbcKAET1KyUjYqCMclCL7Ka3/view?usp=sharing)
- [Captioned workflow demo](hackathon/demo/through-the-glass-workflow-demo-captioned-final.mp4)
- [Corrected presentation](hackathon/Hackathon%204%20Presentation%20-%20corrected.pptx)
- [Complete project documentation](hackathon/README.md)

**How do I run it?**
_Short instructions so someone else can start it._

Open `hackathon/workflow/text-to-image.json` in ComfyUI, install the reported custom nodes and model files, and load the reference window image. Run the text-to-image stage, then open `hackathon/workflow/image-to-video.json`, load the approved frame and run the motion prompt. Full settings and reproduction notes are in the [hackathon README](hackathon/README.md).

**Who did what?**
_Be honest about the split of work between you and your partner._

My partner built and tested the ComfyUI text-to-image and image-to-video workflows. I prepared the README, checked the factual claims and citations, corrected the workflow slides, wrote and recorded the demo narration, and produced the captioned demo video.

**Ethical reflection - what are the risks of your tool? Who could it harm?**
_Every hackathon requires this. One honest paragraph beats three vague ones._

The film uses speculative AI imagery, not documentary footage, so it must be labelled clearly to avoid misleading viewers. Its destructive ending may also reinforce climate fatalism, especially for younger or climate-anxious viewers. We therefore exclude children under 12, retain a renewable-energy scene as a visible alternative, avoid identifiable people, and document the model settings and estimated energy use so the work is transparent and reproducible.

### Checklist
- [x] Prototype workflow exports are in `hackathon/workflow/`
- [x] This week's slides are in `hackathon/`
- [x] The prototype actually runs, and I wrote down how to run it
- [x] Ethical reflection written above

---

## 3. Presentation -> [`presentation/`](presentation/)

*Only fill this in for the week your group was selected to present. You need at least **one** of these across the whole term.*

- [ ] My group presented in this week
- [x] Slides are included with the hackathon submission
- [x] Proof of the demo is included as a captioned MP4

**How did it go? What would I do differently next time?**

The fixed viewpoint made the environmental progression easy to follow and helped the short film feel cohesive. Next time I would export and test the workflow JSON before the presentation deadline, lock the voiceover script earlier, and add the AI-generated-content disclosure directly to the final film from the first edit.

---

## 4. Reflection

**What is the most important thing I learned this week?**

Reproducibility is part of the product, not an afterthought: a convincing output is not enough unless the workflow, models, prompts, settings and limitations are documented clearly.

**Where does this connect to "AI for Good"?**
_One concrete link to ethics, sustainability or social impact._

The project uses generative AI for climate communication while explicitly addressing transparency, emotional harm, audience fit and the environmental cost of repeated generation. Its purpose is to make long-term climate consequences easier to understand without presenting synthetic scenes as real evidence.
