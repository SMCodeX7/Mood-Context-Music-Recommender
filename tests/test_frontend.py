from pathlib import Path

from streamlit.testing.v1 import AppTest

from frontend.services.api_client import api_client

PROJECT_ROOT = Path(__file__).resolve().parents[1]
APP_PATH = PROJECT_ROOT / "frontend" / "app.py"


def mock_healthy_backend(monkeypatch) -> None:
    monkeypatch.setattr(
        api_client,
        "get_health",
        lambda: {"status": "healthy"},
    )


def test_frontend_loads(monkeypatch) -> None:
    mock_healthy_backend(monkeypatch)

    app = AppTest.from_file(APP_PATH)
    app.run()

    assert not app.exception
    assert any(title.value == "MoodTune AI" for title in app.title)
    assert any(status.value == "Frontend: Ready" for status in app.success)
    assert any(status.value == "Backend: Healthy" for status in app.success)


def test_empty_mood_text_shows_warning(monkeypatch) -> None:
    mock_healthy_backend(monkeypatch)

    app = AppTest.from_file(APP_PATH)
    app.run()

    app.button[0].click().run()

    assert app.session_state["recommendation_input"] is None
    assert app.session_state["recommendation_feedback"] == {
        "type": "warning",
        "message": "Describe how you are feeling before continuing",
    }


def test_valid_recommendation_request(monkeypatch) -> None:
    mock_healthy_backend(monkeypatch)

    app = AppTest.from_file(APP_PATH)
    app.run()

    app.text_area(key="mood_text").input(
        "I feel tired after studying and want calm music"
    )
    app.selectbox(key="language").select("Tamil")
    app.selectbox(key="listening_context").select("Study")
    app.selectbox(key="genre").select("Lo-fi")
    app.slider(key="recommendation_count").set_value(15)

    app.button[0].click().run()

    assert app.session_state["recommendation_input"] == {
        "mood_text": "I feel tired after studying and want calm music",
        "language": "Tamil",
        "listening_context": "Study",
        "genre": "Lo-fi",
        "recommendation_count": 15,
    }

    assert app.session_state["recommendation_feedback"] == {
        "type": "success",
        "message": "Recommendation request prepared",
    }