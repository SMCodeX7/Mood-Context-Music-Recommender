from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "MoodTune AI"
    app_description: str = (
        "Backend API for the context-aware music recommendation system."
    )
    app_version: str = "0.1.0"
    app_env: Literal["development", "testing", "production"] = "development"
    debug: bool = True
    api_host: str = "127.0.0.1"
    api_port: int = 8000
    api_v1_prefix: str = "/api/v1"
    spotify_client_id: str = ""
    spotify_client_secret: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()