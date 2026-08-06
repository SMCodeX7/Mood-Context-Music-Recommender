from fastapi import FastAPI

app = FastAPI(
    title="MoodTune AI API",
    description="Backend API for the context-aware music recommendation system.",
    version="0.1.0",
)


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "MoodTune AI API is running",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
    }