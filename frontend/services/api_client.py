from typing import Any

import httpx

from frontend.config import get_frontend_settings


class APIClientError(Exception):
    pass


class APIClient:
    def __init__(self) -> None:
        settings = get_frontend_settings()

        self.base_url = settings.backend_api_url.rstrip("/")
        self.timeout = settings.api_timeout

    def get_health(self) -> dict[str, Any]:
        try:
            response = httpx.get(
                f"{self.base_url}/health",
                timeout=self.timeout,
            )
            response.raise_for_status()
        except httpx.HTTPError as exc:
            raise APIClientError("Unable to communicate with backend API.") from exc

        return response.json()


api_client = APIClient()