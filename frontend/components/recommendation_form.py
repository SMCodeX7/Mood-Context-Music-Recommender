import streamlit as st

LANGUAGES = (
    "Any",
    "English",
    "Tamil",
    "Sinhala",
    "Hindi",
    "Instrumental",
)

LISTENING_CONTEXTS = (
    "Relax",
    "Study",
    "Work",
    "Workout",
    "Travel",
    "Party",
    "Sleep",
)

GENRES = (
    "Any",
    "Pop",
    "Rock",
    "Hip-Hop",
    "R&B",
    "Electronic",
    "Classical",
    "Jazz",
    "Indie",
    "Lo-fi",
)


def initialize_recommendation_state() -> None:
    if "recommendation_input" not in st.session_state:
        st.session_state.recommendation_input = None


def render_recommendation_form() -> None:
    initialize_recommendation_state()

    with st.form("recommendation_form"):
        mood_text = st.text_area(
            "How are you feeling?",
            placeholder="Example: I feel tired and want calm music",
            max_chars=500,
        )

        language = st.selectbox(
            "Preferred language",
            LANGUAGES,
        )

        listening_context = st.selectbox(
            "Listening context",
            LISTENING_CONTEXTS,
        )

        genre = st.selectbox(
            "Genre preference",
            GENRES,
        )

        recommendation_count = st.slider(
            "Number of recommendations",
            min_value=5,
            max_value=25,
            value=10,
            step=5,
        )

        submitted = st.form_submit_button(
            "Prepare Recommendation",
            type="primary",
            use_container_width=True,
        )

    if submitted:
        cleaned_mood_text = mood_text.strip()

        if not cleaned_mood_text:
            st.warning("Describe how you are feeling before continuing")
            return

        st.session_state.recommendation_input = {
            "mood_text": cleaned_mood_text,
            "language": language,
            "listening_context": listening_context,
            "genre": genre,
            "recommendation_count": recommendation_count,
        }

        st.success("Recommendation request prepared")

    request_data = st.session_state.recommendation_input

    if request_data:
        st.subheader("Current Recommendation Request")
        st.json(request_data)
        st.info("Recommendation generation will be connected in a later phase")