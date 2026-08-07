from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class FrontendSettings(BaseSettings):
    backend_api_url: str = "http://127.0.0.1:8000/api/v1"
    api_timeout: float = 5.0

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_frontend_settings() -> FrontendSettings:
    return FrontendSettings()