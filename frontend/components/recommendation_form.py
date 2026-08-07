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

    if "recommendation_feedback" not in st.session_state:
        st.session_state.recommendation_feedback = None


def render_recommendation_form() -> None:
    initialize_recommendation_state()

    with st.form("recommendation_form"):
        mood_text = st.text_area(
            "How are you feeling?",
            placeholder="Example: I feel tired and want calm music",
            max_chars=500,
            key="mood_text",
        )

        language = st.selectbox(
            "Preferred language",
            LANGUAGES,
            key="language",
        )

        listening_context = st.selectbox(
            "Listening context",
            LISTENING_CONTEXTS,
            key="listening_context",
        )

        genre = st.selectbox(
            "Genre preference",
            GENRES,
            key="genre",
        )

        recommendation_count = st.slider(
            "Number of recommendations",
            min_value=5,
            max_value=25,
            value=10,
            step=5,
            key="recommendation_count",
        )

        submitted = st.form_submit_button(
            "Prepare Recommendation",
            type="primary",
            use_container_width=True,
        )

    if submitted:
        cleaned_mood_text = mood_text.strip()

        if not cleaned_mood_text:
            st.session_state.recommendation_feedback = {
                "type": "warning",
                "message": "Describe how you are feeling before continuing",
            }
        else:
            st.session_state.recommendation_input = {
                "mood_text": cleaned_mood_text,
                "language": language,
                "listening_context": listening_context,
                "genre": genre,
                "recommendation_count": recommendation_count,
            }

            st.session_state.recommendation_feedback = {
                "type": "success",
                "message": "Recommendation request prepared",
            }

    feedback = st.session_state.recommendation_feedback

    if feedback:
        if feedback["type"] == "warning":
            st.warning(feedback["message"])
        elif feedback["type"] == "success":
            st.success(feedback["message"])

    request_data = st.session_state.recommendation_input

    if request_data:
        st.subheader("Current Recommendation Request")
        st.json(request_data)
        st.info("Recommendation generation will be connected in a later phase")