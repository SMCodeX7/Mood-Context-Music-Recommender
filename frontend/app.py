import streamlit as st

from frontend.components.backend_status import render_backend_status
from frontend.components.recommendation_form import render_recommendation_form

st.set_page_config(
    page_title="MoodTune AI",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    st.title("MoodTune AI")
    st.caption("Context-aware music recommendations")
    st.divider()

    st.subheader("Current Phase")
    st.write("Frontend foundation")
    st.info("Recommendation generation will be added in later phases")

st.title("MoodTune AI")
st.subheader("Context-Aware Music Recommendation System")
st.write(
    "Discover music based on your mood, language, listening context, "
    "and personal preferences"
)

st.divider()

main_column, status_column = st.columns([2, 1], gap="large")

with main_column:
    st.subheader("Recommendation Workspace")
    render_recommendation_form()

with status_column:
    st.subheader("System Status")
    st.success("Frontend: Ready")
    render_backend_status()

st.divider()

st.caption("MoodTune AI — Frontend Foundation")