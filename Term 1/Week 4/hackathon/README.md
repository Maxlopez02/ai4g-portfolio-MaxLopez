# Through the Glass

**A 31-second climate short film generated through a ComfyUI image-to-video pipeline**

Through the Glass holds one viewpoint in place while the world outside changes. A healthy landscape becomes an industrial skyline, a renewable alternative appears, destruction follows, and the final view leaves Earth behind. The fixed window makes a long climate timeline feel immediate.

## Watch the film

- [Final film on Google Drive](https://drive.google.com/file/d/1OYYY5sTjCbcKAET1KyUjYqCMclCL7Ka3/view?usp=sharing)
- [Project presentation](https://docs.google.com/presentation/d/1sLXHBpgogrEhtBXTxbMtkuy05tf5DjgafnTE8wunlGU/edit?slide=id.p1#slide=id.p1)
- YouTube: **add the public or unlisted URL before submission**

Local copy: [`through-the-glass.mp4`](through-the-glass.mp4)

Corrected presentation copy: [`Hackathon 4 Presentation - corrected.pptx`](Hackathon%204%20Presentation%20-%20corrected.pptx). Slides 3 and 4 now show the workflow screenshots under the correct headings, and their speaker notes contain the demo narration.

## The climate issue

Climate change often feels distant in time, which can make action feel less urgent. The film compresses a long environmental timeline into half a minute and keeps the viewer in the same room. This makes the consequences of repeated choices visible without presenting the speculative scenes as footage of a real event.

The factual anchor is the IPCC Sixth Assessment Report. In modelled pathways that limit warming to 1.5°C with no or limited overshoot, net global greenhouse-gas emissions fall by 43% below 2019 levels by 2030. That is a pathway result, not a prediction that a single percentage guarantees a specific outcome. See the [IPCC AR6 Synthesis Report](https://www.ipcc.ch/site/assets/uploads/2023/03/Doc5_Adopted_AR6_SYR_Longer_Report.pdf) and the [IPCC Working Group III summary](https://www.ipcc.ch/report/ar6/wg3/chapter/summary-for-policymakers/).

## SDG relevance

The project addresses **Sustainable Development Goal 13: Climate Action**, with a direct connection to **Target 13.3**, which calls for better climate education, awareness, and human capacity. The film is designed as a short awareness piece that can begin a discussion about climate agency. See the [United Nations SDG 13 targets](https://sdgs.un.org/goals/goal13).

## Intended audience and placement

The primary audience is higher-education students in the European Union, especially students around ages 18–24 who accept climate science but feel anxious, powerless, or fatalistic about the future.

Planned placement:

- university digital screens during European climate-awareness weeks;
- Instagram Reels and YouTube Shorts shared by student organisations;
- the opening of a classroom discussion about climate action.

The film is **not designed for**:

- climate-science deniers, because a 31-second speculative film cannot resolve a factual dispute;
- children under 12, because the destructive imagery may cause unnecessary distress;
- viewers seeking documentary footage of a real place or event.

### Audience-size note

Eurostat reported about 18.6 million tertiary students in the EU in 2021. A separate global survey of 10,000 people aged 16–25 found that 56% agreed that humanity is doomed. Applying 56% to the EU tertiary-student count gives a rough communication-planning estimate of about 10.4 million people. This is **not a measured EU audience segment** because the two sources cover different populations and geographies.

Sources: [Eurostat Regional Yearbook 2023](https://ec.europa.eu/eurostat/documents/15234730/17582411/KS-HA-23-001-EN-N.pdf) and [Hickman et al., 2021, *The Lancet Planetary Health*](https://pubmed.ncbi.nlm.nih.gov/34895496/).

## Why the format fits the problem

The short runtime suits social feeds and university screens where attention is limited. The fixed window provides a visual reference across every shot, while the changing exterior compresses consequences that normally feel remote. The renewable-energy scene prevents the story from becoming a simple sequence of disaster images: it shows that another path exists before the destructive ending.

## Workflow overview

The submitted materials show two linked ComfyUI stages.

1. **Text to image.** Juggernaut XL creates a key frame from a positive and negative prompt. ControlNet holds the window structure in place while the environment changes.
2. **Image to video.** The selected frame is resized and sent to the MiniMax H3 image-to-video node. The motion prompt animates the exterior while asking the interior structure to remain still.

![Text-to-image workflow](assets/workflows/text-to-image.png)

![Image-to-video workflow](assets/workflows/image-to-video.png)

## Reproduce the workflow

### Requirements

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- the checkpoint and ControlNet model referenced by the exported workflow JSON;
- the custom nodes and image-to-video model referenced by the JSON;
- enough GPU memory for the selected resolution and video model;
- FFmpeg or another editor to assemble the rendered clips and soundtrack.

### Run

1. Clone or download this repository.
2. Install ComfyUI and the custom nodes reported as missing when the workflow opens.
3. Place the required checkpoints, ControlNet weights, VAE, and video-model files in the paths expected by ComfyUI.
4. Open `workflow/text-to-image.json` in ComfyUI.
5. Load the reference window image used by the workflow.
6. Run the text-to-image graph for each shot. Keep the window geometry fixed and change only the exterior description.
7. Open `workflow/image-to-video.json`, load the approved frame, and run the motion prompt.
8. Export each clip, assemble the six shots in the order below, and add the soundtrack.
9. Export H.264 video at 1920×1080. The current final cut is 31.05 seconds and uses AAC audio.

### Visible settings in the submitted screenshots

These values document the examples shown in the presentation. The exported JSON remains the source of truth for the final render.

| Stage | Setting | Value shown |
|---|---|---|
| Text to image | Resolution | 1344 × 768 |
| Text to image | KSampler seed | 100 |
| Text to image | Steps / CFG | 30 / 5.0 |
| Text to image | Sampler / scheduler | DPM++ 2M SDE GPU / Karras |
| Text to image | Denoise | 0.50 |
| Text to image | ControlNet strength | 0.70 |
| Image to video | Resized frame | 960 × 544, 0.50 MP |
| Image to video | Duration | 5.0 seconds |
| Image to video | Noise seed | 757358688076805 |
| Image to video | Turbo steps | 9 |

## Storyboard

The time ranges below follow the finished film. The prompt column is a concise record of the visual instruction. The exported workflow JSON should retain the complete prompt strings, model names, and seeds used for regeneration.

| Shot | Time | Story beat | Prompt summary | Frame |
|---:|:---:|---|---|---|
| 01 | 00:00–00:05 | Healthy landscape | Fixed interior window, green valley and forest, clear daylight, subtle natural movement | ![Shot 1](assets/storyboard/shot-01.jpg) |
| 02 | 00:05–00:10 | Industrial expansion | Same viewpoint, factories and smokestacks, dense grey pollution, darkened atmosphere | ![Shot 2](assets/storyboard/shot-02.jpg) |
| 03 | 00:10–00:16 | A possible alternative | Same viewpoint, wind turbines across a green landscape, warm sunlight, calm motion | ![Shot 3](assets/storyboard/shot-03.jpg) |
| 04 | 00:16–00:21 | Destructive escalation | Same window, distant blast and rolling smoke cloud, debris and atmospheric haze | ![Shot 4](assets/storyboard/shot-04.jpg) |
| 05 | 00:21–00:26 | Environmental collapse | Same viewpoint, barren dry terrain, dead trees, dust and orange haze | ![Shot 5](assets/storyboard/shot-05.jpg) |
| 06 | 00:26–00:31 | Lifeless future | Thick observation window, barren moonlike surface, stars and cold light, very slow exterior motion | ![Shot 6](assets/storyboard/shot-06.jpg) |

Common negative-prompt terms shown in the workflow screenshot: `people, faces, hands, text, letters, watermark, logo, cartoon, oversaturated, distorted window frame, deformed, blurry, low quality`.

## Demo narration

Short explanations for presentation slides 3 and 4 are included in [`DEMO_SCRIPT.md`](DEMO_SCRIPT.md). The final combined walkthrough uses slide-based pans and zooms to focus on the active ComfyUI nodes, includes the two narration tracks, and has burned-in English captions:

- [`demo/through-the-glass-workflow-demo-captioned-final.mp4`](demo/through-the-glass-workflow-demo-captioned-final.mp4)

The `demo/` folder also contains the separate narration tracks and a clean, uncaptioned reference cut.

## Ethical reflection

The film uses speculative AI imagery rather than documentary evidence. It does not depict a named neighbourhood, a real disaster, or a real person. No faces or identifiable human likenesses appear. The title, presentation, repository, and video description should state that the imagery is AI generated so viewers do not mistake it for recorded evidence. A visible on-screen disclosure should also be added if the final uploaded film does not already contain one.

The main communication risk is fatalism. A sequence that only becomes worse could reinforce the helplessness the project wants to challenge. The wind-energy scene was therefore kept as a visible alternative, and the presentation frames the ending as a consequence that can still be changed.

The team reports 42 generations on an RTX 4090 and estimates 1.8 kWh of electricity use, corresponding to 0.72 kg CO₂e under the electricity factor used by the team. These are project estimates, not independently measured values. Publishing the workflow, prompts, and settings can reduce unnecessary trial runs by future students.

## Repository contents

```text
.
├── README.md
├── DEMO_SCRIPT.md
├── through-the-glass.mp4
├── demo/
│   ├── workflow-1-text-to-image.mp3
│   ├── workflow-2-image-to-video.mp3
│   ├── workflow-demo.mp4
│   └── through-the-glass-workflow-demo-captioned-final.mp4
├── assets/
│   ├── storyboard/
│   └── workflows/
└── workflow/
    ├── text-to-image.json
    └── image-to-video.json
```

## Submission checklist

- [x] Final film, MP4, 1080p, 31 seconds
- [x] Six generated shots
- [x] Intended audience, exclusions, placement, and SDG link
- [x] Shot list with timing, descriptions, prompt summaries, and frames
- [x] Ethical reflection
- [x] Captioned workflow demonstration
- [x] Text-to-image and image-to-video ComfyUI workflow exports
- [ ] Upload the film to YouTube and add the public or unlisted URL above
- [ ] Confirm that the final upload visibly discloses that the imagery is AI generated

## Team

Pair submission for AI for Good, Hackathon 4, The Hague University of Applied Sciences.
