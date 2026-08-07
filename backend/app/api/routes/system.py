from fastapi import APIRouter

router = APIRouter(tags=["System"])


@router.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "MoodTune AI API is running",
        "version": "0.1.0",
    }


@router.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
    }