from fastapi.testclient import TestClient

from backend.app.main import create_app

client = TestClient(create_app())


def test_read_root() -> None:
    response = client.get("/api/v1/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "MoodTune AI API is running",
        "version": "0.1.0",
    }


def test_health_check() -> None:
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
    }


def test_unversioned_health_endpoint_not_found() -> None:
    response = client.get("/health")

    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "status_code": 404,
            "detail": "Not Found",
            "path": "/health",
        }
    }


def test_unknown_versioned_endpoint_not_found() -> None:
    response = client.get("/api/v1/unknown")

    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "status_code": 404,
            "detail": "Not Found",
            "path": "/api/v1/unknown",
        }
    }