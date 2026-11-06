"""Hogweed Guard NL: a cautious three-class Roboflow screening MVP."""

from __future__ import annotations

import os
from dataclasses import dataclass

import streamlit as st
from dotenv import load_dotenv
from PIL import Image

from model_logic import extract_predictions, screening_decision

load_dotenv()


@dataclass(frozen=True)
class Species:
    name: str
    latin: str
    status: str
    next_step: str


SPECIES = {
    "giant_hogweed": Species(
        "Possible giant hogweed",
        "Heracleum mantegazzianum",
        "Invasive species: expert confirmation needed",
        "Keep your distance. Do not touch or remove the plant. Record the location and ask a site manager or species expert to confirm it.",
    ),
    "common_hogweed": Species(
        "Possible common hogweed",
        "Heracleum sphondylium",
        "Native look-alike",
        "Leave the plant in place. Ask an expert before taking management action.",
    ),
    "cow_parsley": Species(
        "Possible cow parsley",
        "Anthriscus sylvestris",
        "Common native look-alike",
        "This screening suggests no management action. Ask an expert if the result supports an official survey.",
    ),
}


@st.cache_resource(show_spinner=False)
def build_client(api_url: str, api_key: str):
    """Create the Roboflow inference client once per app session."""
    from inference_sdk import InferenceHTTPClient

    return InferenceHTTPClient(api_url=api_url, api_key=api_key)


def run_ai_model(image: Image.Image) -> list[tuple[str, float]]:
    """Send the image to the trained Roboflow DINOv3 classification workflow."""
    api_key = os.getenv("ROBOFLOW_API_KEY", "").strip()
    workspace = os.getenv("ROBOFLOW_WORKSPACE_NAME", "").strip()
    workflow_id = os.getenv("ROBOFLOW_WORKFLOW_ID", "").strip()
    api_url = os.getenv("ROBOFLOW_API_URL", "https://serverless.roboflow.com").strip()
    if not api_key or not workspace or not workflow_id or api_key.startswith("replace_"):
        raise RuntimeError(
            "Roboflow is not configured. Copy .env.example to .env and add the private connection values."
        )

    response = build_client(api_url, api_key).run_workflow(
        workspace_name=workspace,
        workflow_id=workflow_id,
        images={"image": image},
        use_cache=True,
    )
    return extract_predictions(response)


def main() -> None:
    st.set_page_config(page_title="Hogweed Guard NL", page_icon="🌿")
    st.title("Hogweed Guard NL")
    st.caption("Hackathon 7 individual resit · Roboflow DINOv3 Small · SDG 15, target 15.8")

    st.warning(
        "Never touch suspected giant hogweed. This three-species prototype only supports first screening and never confirms a species or recommends removal."
    )

    with st.expander("Why this counts as an AI MVP"):
        st.markdown(
            """
            The essential function is a trained **Roboflow DINOv3 Small image classifier**.
            The uploaded image is sent to a Roboflow Workflow, which returns confidence
            scores for giant hogweed, common hogweed and cow parsley. Without that model
            call, the app cannot produce a screening result.
            """
        )

    uploaded = st.file_uploader(
        "Upload one clear plant photo",
        type=["jpg", "jpeg", "png", "webp"],
        help="Avoid photos containing recognisable people, homes or licence plates.",
    )
    if uploaded is None:
        st.info("MVP scope: one user, one photo, three plant classes, one cautious result.")
        return

    try:
        image = Image.open(uploaded).convert("RGB")
    except Exception:
        st.error("The file could not be read as an image.")
        return

    st.image(image, caption="Uploaded photograph", use_container_width=True)
    if not st.button("Run AI screening", type="primary", use_container_width=True):
        return

    try:
        with st.spinner("Roboflow is comparing visible plant features..."):
            predictions = run_ai_model(image)
    except Exception as exc:
        st.error(str(exc))
        return

    threshold = float(os.getenv("CONFIDENCE_THRESHOLD", "0.65"))
    decision, confidence = screening_decision(predictions, threshold)
    if decision == "unrecognised":
        st.error("The model returned no recognised class.")
    elif decision == "uncertain":
        st.warning(
            f"Uncertain ({confidence:.0%}). The highest score is below the {threshold:.0%} safety threshold. Ask an expert."
        )
    else:
        species = SPECIES[decision]
        st.subheader(species.name)
        st.caption(f"{species.latin} · model confidence {confidence:.0%}")
        st.write(species.status)
        st.info(species.next_step)

    with st.expander("All model scores"):
        for label, score in predictions:
            if label in SPECIES:
                st.write(f"{SPECIES[label].name.replace('Possible ', '')}: {score:.1%}")
    st.caption("Confidence is a model score, not a guarantee that the identification is correct.")


if __name__ == "__main__":
    main()
