# Hackathon 7 resit: Hogweed Guard NL

**Author:** Max Lopez

**Submission type:** individual resit

**AI tool:** Roboflow DINOv3 Small image classifier

**SDG:** 15, Life on Land, target 15.8

**Repository:** https://github.com/Maxlopez02/ai4g-portfolio-MaxLopez/tree/main/Resit/Week%207/hackathon

Hogweed Guard NL is a small Streamlit MVP for Dutch nature volunteers. The user
uploads one photograph of a suspected hogweed. A trained Roboflow image model
compares giant hogweed with native common hogweed and cow parsley. The interface
shows a class result only at or above 65% confidence; otherwise it asks for
expert review. Every result tells the user not to touch or remove a plant on the
basis of the model.

## Knockout evidence

| Criterion | Direct evidence |
| --- | --- |
| **K1: AI tool** | [`AI_TOOL_EVIDENCE.md`](AI_TOOL_EVIDENCE.md), the live `run_workflow()` call in [`app.py`](app.py), and screenshots in [`evidence/`](evidence/) |
| **K2: SDG relevance** | [`SDG_AND_SCOPE.md`](SDG_AND_SCOPE.md) maps the user flow to SDG 15 target 15.8 and cites UN and NVWA sources |
| **K3: scope** | [`SDG_AND_SCOPE.md`](SDG_AND_SCOPE.md) defines one user, one input, three classes, one result and explicit exclusions |
| **Contribution** | [`CONTRIBUTIONS.md`](CONTRIBUTIONS.md) identifies Max as the individual resit author and clarifies Sofiia's status |
| **Repository** | This folder contains the runnable app, dependency file, safe environment template, tests, evidence and resit deck |

The submission deck is
[`presentation/Hogweed_Guard_NL_Hackathon_7_Resit_Submission.pptx`](presentation/Hogweed_Guard_NL_Hackathon_7_Resit_Submission.pptx).

## Reproduce the MVP

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Add the private Roboflow values to `.env`, then run:

```bash
streamlit run app.py
```

Run the offline logic tests without a Roboflow key:

```bash
python -m unittest discover -s tests -v
```

## Evidence and result

The earlier held-out evaluation used 36 images that were not sent to the model
during training. The model classified 30 correctly, giving 83.3% accuracy.
Errors included a giant-hogweed image predicted as common hogweed and a
common-hogweed image predicted as giant hogweed. These failures support the 65%
withholding threshold and mandatory expert confirmation rather than an automatic
management recommendation.

## Safety and limitations

The three classes do not cover every plant a volunteer may encounter. Dataset
labels can be wrong, photographs can hide diagnostic features, and confidence is
not the probability that a result is correct. A false negative could encourage
someone to approach a hazardous plant; a false positive could contribute to
removal of a native plant. The MVP therefore limits its claim to first screening,
withholds weak results and keeps a human expert in the decision.

Uploaded images go to Roboflow for inference. Users should avoid photographs
with recognisable people, homes or licence plates.

## Sources

- [UN Sustainable Development Goal 15, including target 15.8](https://sdgs.un.org/goals/goal15)
- [Dutch NVWA factsheet on giant hogweed](https://www.nvwa.nl/documenten/planten-in-de-natuur/exoten/risicobeoordelingen/factsheet-reuzenberenklauw)
- [GBIF Occurrence API documentation](https://techdocs.gbif.org/en/openapi/v1/occurrence)
