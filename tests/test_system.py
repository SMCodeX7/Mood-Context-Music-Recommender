from fastapi.testclient import TestClient

from backend.app.main import create_app

client = TestClient(create_app())


def test_read_root() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "MoodTune AI API is running",
        "version": "0.1.0",
    }


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
    }