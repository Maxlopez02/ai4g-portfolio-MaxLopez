# Term 1 - Week 7: Computer Vision

## Hackathon 7: Hogweed Guard NL

**Individual project**  
**Tool:** Roboflow image classification  
**SDG:** 15 - Life on Land

### The problem

Giant hogweed is invasive in the Netherlands and its sap can cause serious skin reactions. It can also be confused with common hogweed and cow parsley. I made this project for Dutch nature volunteers and local site managers who need a first check before asking an expert. It is not meant for people making removal, medical or legal decisions.

### What I built

The user uploads a plant photograph in a small Streamlit app. A Roboflow DINOv3 model compares three classes: giant hogweed, common hogweed and cow parsley. The app shows a cautious result when confidence is at least 65%. Below that threshold it shows **uncertain** and asks for expert review.

I collected 360 Dutch observations through GBIF. I used 324 labelled images in Roboflow and kept 36 images separate for a final test. The model correctly classified 30 of those 36 unseen images (83.3%).

The working prototype is in [`hackathon/app.py`](hackathon/app.py). A successful app result and the Roboflow model metrics are in [`hackathon/evidence/`](hackathon/evidence/). The presentation is [`presentation/Hogweed_Guard_NL_Hackathon_7.pptx`](presentation/Hogweed_Guard_NL_Hackathon_7.pptx).

### How to run it

1. Open a terminal in `hackathon/` and run `pip install -r requirements.txt`.
2. Copy `.env.example` to `.env` and add a private Roboflow API key.
3. Run `streamlit run app.py` and upload a JPG, PNG or WebP image.

### Ethical reflection

A false positive could make someone remove a native plant. A false negative could make someone approach dangerous giant hogweed. The GBIF labels may contain mistakes, and the photos do not represent every season, region or growth stage. I reduced these risks by keeping the scope to three species, testing on images that were not sent to Roboflow, withholding low-confidence answers, and showing a warning never to touch or remove a plant without expert confirmation. A real deployment would need more field data and review by botanists.

### My contribution and reflection

I chose the topic, collected and checked the dataset, trained the Roboflow model, tested it on the held-out set, and decided how the safety threshold and warnings should work. I used AI tools for coding and debugging support, then tested the final flow and checked the results myself.

The biggest lesson was that a strong result inside a training platform does not automatically make a model safe. The separate test exposed mistakes that mattered for the user. In a next version I would collect more difficult common-hogweed photographs from different seasons and distances.

### Sources

- [NVWA factsheet: reuzenberenklauw](https://www.nvwa.nl/documenten/plant/planten-in-de-natuur/exoten/risicobeoordelingen/factsheet-reuzenberenklauw)
- [GBIF occurrence API](https://techdocs.gbif.org/en/openapi/v1/occurrence)
