"""Streamlit entry point for MigrationHelp."""

from __future__ import annotations

import os

import streamlit as st
from dotenv import load_dotenv

from migrationhelp.assistant import SUPPORTED_LANGUAGES, answer_question, friendly_api_error
from migrationhelp.knowledge_base import SOURCE_BY_ID, select_sources
from migrationhelp.safety import check_question, is_emergency


load_dotenv()

st.set_page_config(
    page_title="MigrationHelp — your next Dutch admin step",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    :root {
      --ink: #102A43;
      --blue: #1363DF;
      --sky: #EAF3FF;
      --orange: #E86A33;
      --paper: #F7F9FC;
      --line: #CAD5E2;
    }
    .stApp { background: var(--paper); color: var(--ink); }
    [data-testid="stSidebar"] { background: #102A43; }
    [data-testid="stSidebar"] * { color: #F7F9FC; }
    [data-testid="stSidebar"] input, [data-testid="stSidebar"] [data-baseweb="select"] * { color: #102A43; }
    .block-container { max-width: 1120px; padding-top: 4.2rem; }
    h1, h2, h3 { letter-spacing: -0.035em; color: var(--ink); }
    h1 { font-size: clamp(2.5rem, 6vw, 5.2rem) !important; line-height: .92 !important; max-width: 12ch; }
    .eyebrow { font: 700 .78rem/1.2 ui-monospace, SFMono-Regular, Menlo, monospace; letter-spacing: .12em; color: var(--orange); text-transform: uppercase; }
    .lede { max-width: 640px; font-size: 1.15rem; line-height: 1.55; color: #334E68; }
    .route-ribbon { display: grid; grid-template-columns: repeat(3, 1fr); margin: 2rem 0; border: 1px solid var(--line); background: white; }
    .route-stop { padding: 1rem 1.1rem; border-right: 1px solid var(--line); }
    .route-stop:last-child { border-right: 0; }
    .route-stop b { display: block; color: var(--blue); font-size: .78rem; text-transform: uppercase; letter-spacing: .08em; margin-bottom: .25rem; }
    .answer-card { background: white; border: 1px solid var(--line); border-left: 6px solid var(--blue); padding: 1.3rem 1.5rem; margin: 1rem 0; box-shadow: 0 12px 32px rgba(16,42,67,.06); }
    .source-card { background: #fff; border: 1px solid var(--line); padding: .9rem 1rem; margin: .55rem 0; }
    .micro { color: #627D98; font-size: .84rem; }
    .privacy-note { padding: .8rem 1rem; background: #FFF5ED; border-left: 4px solid var(--orange); }
    [data-testid="stFormSubmitButton"] button { background: var(--blue); color: white; border: 0; border-radius: 4px; min-height: 3rem; font-weight: 700; }
    [data-testid="stFormSubmitButton"] button:hover { background: #0B4FB8; color: white; }
    [data-testid="stFormSubmitButton"] button:focus { outline: 3px solid #F6BD60; outline-offset: 2px; }
    @media (max-width: 700px) {
      .route-ribbon { grid-template-columns: 1fr; }
      .route-stop { border-right: 0; border-bottom: 1px solid var(--line); }
    }
    @media (prefers-reduced-motion: reduce) { * { scroll-behavior: auto !important; transition: none !important; } }
    </style>
    """,
    unsafe_allow_html=True,
)


def show_sources(source_ids: list[str]) -> None:
    st.subheader("Check the official sources")
    for source_id in source_ids:
        source = SOURCE_BY_ID[source_id]
        st.markdown(
            f"<div class='source-card'><strong>{source.organisation}</strong><br>"
            f"<a href='{source.url}' target='_blank'>{source.title}</a><br>"
            f"<span class='micro'>Reviewed for this prototype: {source.last_checked}</span></div>",
            unsafe_allow_html=True,
        )


with st.sidebar:
    st.markdown("### Your situation")
    language = st.selectbox("Answer language", SUPPORTED_LANGUAGES)
    stay_length = st.selectbox(
        "How long will you stay?",
        ("I am not sure", "4 months or less", "More than 4 months"),
    )
    municipality = st.text_input("Municipality or city (optional)", max_chars=80, placeholder="e.g. The Hague")
    st.markdown("---")
    if os.getenv("GEMINI_API_KEY"):
        st.success("Live AI is connected")
    else:
        st.warning("API key not connected")
        st.caption("Add GEMINI_API_KEY to a local .env file, then restart the app.")
    st.caption("No account. No chat history. Do not enter identity numbers.")


st.markdown("<div class='eyebrow'>Netherlands · first administrative steps</div>", unsafe_allow_html=True)
st.title("A clearer route through Dutch paperwork.")
st.markdown(
    "<p class='lede'>Ask one practical question about registration, a BSN, DigiD, health insurance or a residence-permit next step. MigrationHelp turns official information into a short route in your language.</p>",
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="route-ribbon" aria-label="How MigrationHelp works">
      <div class="route-stop"><b>1 · You ask</b>No document numbers needed</div>
      <div class="route-stop"><b>2 · AI explains</b>Only from the source pack</div>
      <div class="route-stop"><b>3 · You verify</b>Official links stay visible</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='privacy-note'><strong>Protect your privacy.</strong> Do not enter a BSN, passport number, residence-card number, exact address or medical details.</div>",
    unsafe_allow_html=True,
)

with st.form("migration_question"):
    question = st.text_area(
        "What do you need to arrange?",
        height=135,
        max_chars=1_200,
        placeholder="Example: I arrived for a one-year job. How do I get a BSN and what should I do next?",
    )
    submitted = st.form_submit_button("Show my next steps", use_container_width=True)

if submitted:
    safety = check_question(question)
    if not safety.allowed:
        st.error(safety.message)
    elif is_emergency(question):
        st.error("This sounds urgent. In immediate danger in the Netherlands, call 112. This chatbot cannot provide emergency help.")
    elif not os.getenv("GEMINI_API_KEY"):
        st.error("Live AI is not connected. Add the API key to the local .env file and restart the app.")
        show_sources([source.id for source in select_sources(question)])
    else:
        with st.spinner("Checking the official route…"):
            try:
                answer = answer_question(question, language, stay_length, municipality)
            except Exception as error:  # Safe boundary: never expose SDK or credential details in the UI.
                st.error(friendly_api_error(error))
                show_sources([source.id for source in select_sources(question)])
            else:
                risk_label = {"low": "Routine information", "medium": "Check details", "high": "Human help recommended"}[answer.risk_level]
                st.caption(risk_label)
                # Model output is rendered as text/Markdown, never injected as trusted HTML.
                with st.container(border=True):
                    st.write(answer.direct_answer)

                if answer.steps:
                    st.subheader("Your route")
                    for index, step in enumerate(answer.steps, start=1):
                        st.markdown(f"**{index}.** {step}")

                if answer.what_to_prepare:
                    st.subheader("What to prepare")
                    for item in answer.what_to_prepare:
                        st.markdown(f"- {item}")

                st.info(answer.limits)
                show_sources(answer.source_ids)

st.markdown("---")
st.caption(
    "MigrationHelp gives general public information, not legal or medical advice. Rules and personal circumstances can change the answer. Verify critical details with the linked authority."
)
