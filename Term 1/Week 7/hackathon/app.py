"""Hogweed Guard NL — cautious screening of three Dutch plant species."""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

import streamlit as st
from dotenv import load_dotenv
from PIL import Image

load_dotenv()


@dataclass(frozen=True)
class SpeciesCard:
    display_name: str
    latin_name: str
    status: str
    action: str
    detail: str
    tone: str


SPECIES: dict[str, SpeciesCard] = {
    "giant_hogweed": SpeciesCard(
        display_name="Possible giant hogweed",
        latin_name="Heracleum mantegazzianum",
        status="Invasive — expert confirmation needed",
        action="Keep your distance. Do not touch or remove the plant. Record the location and ask the site manager or a species expert to confirm it.",
        detail="Typical field clues include very large, sharply divided leaves and a hollow, hairy stem with purple-red blotches. A photograph alone cannot confirm every growth stage.",
        tone="danger",
    ),
    "common_hogweed": SpeciesCard(
        display_name="Possible common hogweed",
        latin_name="Heracleum sphondylium",
        status="Native look-alike",
        action="Leave the plant in place. If identification matters for management, ask an expert to confirm it before taking action.",
        detail="Common hogweed is native and generally smaller. Its flower heads, leaves, and stems can still resemble giant hogweed in photographs.",
        tone="native",
    ),
    "cow_parsley": SpeciesCard(
        display_name="Possible cow parsley",
        latin_name="Anthriscus sylvestris",
        status="Common native look-alike",
        action="No management action is suggested by this screening. Seek expert confirmation if the photograph was taken for an official survey.",
        detail="Cow parsley has finer, fern-like leaves and delicate white flower clusters, but framing and plant age can hide those clues.",
        tone="neutral",
    ),
}

CLASS_ALIASES = {
    "giant hogweed": "giant_hogweed",
    "giant-hogweed": "giant_hogweed",
    "heracleum mantegazzianum": "giant_hogweed",
    "common hogweed": "common_hogweed",
    "common-hogweed": "common_hogweed",
    "heracleum sphondylium": "common_hogweed",
    "cow parsley": "cow_parsley",
    "cow-parsley": "cow_parsley",
    "anthriscus sylvestris": "cow_parsley",
}


def normalise_label(label: str) -> str:
    """Map Roboflow label variants to the app's stable class identifiers."""
    cleaned = label.strip().lower().replace("__", "_")
    cleaned = CLASS_ALIASES.get(cleaned, cleaned.replace(" ", "-") if " " in cleaned else cleaned)
    if cleaned in CLASS_ALIASES:
        cleaned = CLASS_ALIASES[cleaned]
    return cleaned.replace("-", "_")


def extract_predictions(payload: Any) -> list[tuple[str, float]]:
    """Parse direct-model and Workflow classification response shapes."""
    if isinstance(payload, list):
        if len(payload) == 1 and isinstance(payload[0], dict):
            return extract_predictions(payload[0])
        candidates = payload
    elif isinstance(payload, dict):
        candidates = payload.get("predictions", [])
        if isinstance(candidates, dict):
            if all(isinstance(value, (int, float)) for value in candidates.values()):
                candidates = [
                    {"class": label, "confidence": confidence}
                    for label, confidence in candidates.items()
                ]
            else:
                nested = extract_predictions(candidates)
                if nested:
                    return nested
        if not candidates and payload.get("top"):
            confidence = payload.get("confidence", payload.get("top_confidence", 0))
            candidates = [{"class": payload["top"], "confidence": confidence}]
        if not candidates:
            for value in payload.values():
                nested = extract_predictions(value)
                if nested:
                    return nested
    else:
        candidates = []

    parsed: list[tuple[str, float]] = []
    for item in candidates:
        if not isinstance(item, dict):
            continue
        label = item.get("class") or item.get("label") or item.get("class_name")
        confidence = item.get("confidence", item.get("score", 0))
        if label is None:
            continue
        try:
            parsed.append((normalise_label(str(label)), float(confidence)))
        except (TypeError, ValueError):
            continue
    return sorted(parsed, key=lambda row: row[1], reverse=True)


@st.cache_resource(show_spinner=False)
def build_client(api_url: str, api_key: str):
    from inference_sdk import InferenceHTTPClient

    return InferenceHTTPClient(api_url=api_url, api_key=api_key)


def run_inference(image: Image.Image) -> list[tuple[str, float]]:
    api_key = os.getenv("ROBOFLOW_API_KEY", "").strip()
    workspace_name = os.getenv("ROBOFLOW_WORKSPACE_NAME", "").strip()
    workflow_id = os.getenv("ROBOFLOW_WORKFLOW_ID", "").strip()
    api_url = os.getenv("ROBOFLOW_API_URL", "https://serverless.roboflow.com").strip()
    if (
        not api_key
        or not workspace_name
        or not workflow_id
        or api_key.startswith("replace_")
    ):
        raise RuntimeError(
            "The Roboflow connection is not configured yet. Add the private API key, "
            "workspace name, and workflow ID to the local .env file."
        )
    client = build_client(api_url, api_key)
    result = client.run_workflow(
        workspace_name=workspace_name,
        workflow_id=workflow_id,
        images={"image": image},
        use_cache=True,
    )
    return extract_predictions(result)


def render_header() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Fraunces:opsz,wght@9..144,650&display=swap');
        :root {
          --peat: #18251e;
          --fern: #315c45;
          --paper: #fbfcf7;
          --lichen: #dce7d8;
          --stem: #6f3f63;
          --warning: #e7ae3f;
        }
        .stApp { background: #eff3ec; }
        .block-container { max-width: 1040px; padding-top: 2.1rem; padding-bottom: 4rem; }
        h1, h2, h3 { font-family: 'Fraunces', Georgia, serif !important; color: var(--peat); }
        p, label, button, input, .stMarkdown { font-family: 'DM Sans', system-ui, sans-serif; }
        .field-head { display: grid; grid-template-columns: 1fr auto; gap: 2rem; align-items: end; margin-bottom: 1.5rem; }
        .eyebrow { font: 700 .73rem/1.2 'DM Sans', sans-serif; letter-spacing: .16em; text-transform: uppercase; color: var(--fern); }
        .field-title { font: 650 clamp(2.7rem, 7vw, 5.4rem)/.92 'Fraunces', Georgia, serif; letter-spacing: -.045em; color: var(--peat); margin: .65rem 0 .8rem; max-width: 780px; }
        .field-deck { max-width: 650px; color: #496054; font-size: 1.03rem; line-height: 1.55; }
        .specimen-mark { width: 58px; height: 146px; border: 1px solid #9aae9d; border-radius: 999px 999px 8px 8px; position: relative; background: linear-gradient(90deg,#dbe8d6 0 46%,#c9d9c5 46% 54%,#dbe8d6 54%); }
        .specimen-mark:before, .specimen-mark:after { content:''; position:absolute; background:var(--stem); border-radius:50%; opacity:.88; }
        .specimen-mark:before { width:13px; height:23px; left:10px; top:46px; transform:rotate(19deg); box-shadow:22px 38px 0 -2px var(--stem), 2px 76px 0 -3px var(--stem); }
        .specimen-mark:after { width:8px; height:13px; right:9px; top:20px; transform:rotate(-18deg); box-shadow:-23px 80px 0 -1px var(--stem); }
        .field-note { background: var(--paper); border: 1px solid #cad6c8; border-left: 5px solid var(--stem); border-radius: 3px; padding: 1rem 1.15rem; margin: 1.1rem 0 1.3rem; color: #34483d; }
        [data-testid="stFileUploader"] { background: var(--paper); border: 1px solid #c4d2c2; border-radius: 3px; padding: .65rem; }
        [data-testid="stFileUploaderDropzone"] { background: #f6f8f2; border: 1.5px dashed #8ba18f; border-radius: 2px; }
        .result-card { background: var(--paper); border: 1px solid #c4d2c2; border-top: 7px solid var(--fern); border-radius: 3px; padding: 1.35rem 1.45rem; margin-top: .4rem; box-shadow: 0 14px 34px rgba(31,55,41,.08); }
        .result-card.danger { border-top-color: var(--stem); }
        .result-card.native { border-top-color: #467a58; }
        .result-card.neutral { border-top-color: #879878; }
        .result-label { color: #66796c; font-size: .76rem; text-transform: uppercase; letter-spacing: .13em; font-weight: 700; }
        .result-name { font: 650 2rem/1.08 'Fraunces', Georgia, serif; color: var(--peat); margin: .35rem 0 .15rem; }
        .latin { font-style: italic; color: #627267; margin-bottom: .9rem; }
        .confidence-track { height: 9px; background: #dce5d9; overflow: hidden; margin: .75rem 0 .45rem; }
        .confidence-fill { height: 100%; background: repeating-linear-gradient(90deg, var(--stem) 0 20px, #9c6b8e 20px 25px); }
        .action { margin-top: 1rem; padding: .85rem 1rem; background: #f0ead9; border-left: 4px solid var(--warning); color: #403b2d; }
        .smallprint { color: #65766a; font-size: .82rem; line-height: 1.5; }
        .stButton > button { border-radius: 2px; background: var(--peat); color: white; border: 1px solid var(--peat); min-height: 44px; font-weight: 700; }
        .stButton > button:hover { background: var(--fern); border-color: var(--fern); color: white; }
        .stButton > button:focus-visible, a:focus-visible { outline: 3px solid var(--warning); outline-offset: 3px; }
        @media (max-width: 640px) { .field-head { grid-template-columns: 1fr; } .specimen-mark { display:none; } }
        </style>
        <div class="field-head">
          <div>
            <div class="eyebrow">SDG 15 · Field screening prototype</div>
            <div class="field-title">Hogweed Guard NL</div>
            <div class="field-deck">Screen a photograph of a suspected hogweed before an expert inspection. The model compares giant hogweed, common hogweed and cow parsley.</div>
          </div>
          <div class="specimen-mark" aria-hidden="true"></div>
        </div>
        <div class="field-note"><strong>Safety first:</strong> never touch a suspected giant hogweed. This prototype supports screening only; it does not confirm a species or recommend removal.</div>
        """,
        unsafe_allow_html=True,
    )


def render_result(predictions: list[tuple[str, float]], threshold: float) -> None:
    known = [(label, score) for label, score in predictions if label in SPECIES]
    if not known:
        st.error("The model returned no recognised plant classes. Check the Roboflow class names.")
        return
    label, confidence = known[0]
    if confidence < threshold:
        st.markdown(
            f"""
            <div class="result-card">
              <div class="result-label">Screening result</div>
              <div class="result-name">Uncertain — expert review needed</div>
              <div class="latin">Highest model score: {confidence:.0%}</div>
              <div class="confidence-track"><div class="confidence-fill" style="width:{confidence * 100:.1f}%"></div></div>
              <p>The photograph is below the {threshold:.0%} confidence threshold. Try a clear photograph of the full plant, leaf and stem—without touching it.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    card = SPECIES[label]
    st.markdown(
        f"""
        <div class="result-card {card.tone}">
          <div class="result-label">Screening result · {card.status}</div>
          <div class="result-name">{card.display_name}</div>
          <div class="latin">{card.latin_name}</div>
          <div class="confidence-track"><div class="confidence-fill" style="width:{confidence * 100:.1f}%"></div></div>
          <div class="smallprint">Model confidence: {confidence:.0%}. Confidence is not the probability that the identification is correct.</div>
          <p>{card.detail}</p>
          <div class="action"><strong>Next step:</strong> {card.action}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if len(known) > 1:
        with st.expander("See all model scores"):
            for other_label, score in known:
                st.write(f"{SPECIES[other_label].display_name.replace('Possible ', '')}: {score:.1%}")


def main() -> None:
    st.set_page_config(page_title="Hogweed Guard NL", page_icon="🌿", layout="centered")
    render_header()

    left, right = st.columns([1.08, 0.92], gap="large")
    with left:
        st.subheader("Photograph the clues")
        st.write("Use one clear JPG or PNG showing the full plant where possible. A second close-up of the stem or leaves can help an expert later.")
        uploaded = st.file_uploader(
            "Choose a plant photograph",
            type=["jpg", "jpeg", "png", "webp"],
            help="Maximum file size: 12 MB.",
        )
    with right:
        st.subheader("What this model knows")
        st.markdown(
            """
            - Giant hogweed *(invasive)*
            - Common hogweed *(native)*
            - Cow parsley *(native)*

            It does **not** recognise every Dutch plant. Only use it for plants that resemble these three species.
            """
        )

    if uploaded is None:
        st.markdown("---")
        st.caption("Built for nature volunteers and local site managers. Model predictions must be checked before management decisions.")
        return

    try:
        image = Image.open(uploaded).convert("RGB")
    except Exception:
        st.error("This file could not be read as an image. Choose a different JPG, PNG or WebP file.")
        return

    st.image(image, caption="Uploaded photograph", use_container_width=True)
    if st.button("Screen this photograph", type="primary", use_container_width=True):
        try:
            with st.spinner("Comparing visible plant features…"):
                predictions = run_inference(image)
            threshold = float(os.getenv("CONFIDENCE_THRESHOLD", "0.65"))
            render_result(predictions, threshold)
        except Exception as exc:
            st.error(str(exc))
            st.info("The interface is ready. Add the rotated private API key to the local .env file, then retry.")

    st.markdown("---")
    st.caption("Privacy note: uploaded images are sent to Roboflow for inference. Avoid photographs containing recognisable people, homes or licence plates.")


if __name__ == "__main__":
    main()
