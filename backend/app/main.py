from fastapi import FastAPI

from backend.app.api.router import api_router
from backend.app.core.config import get_settings


def create_app() -> FastAPI:
    settings = get_settings()

    application = FastAPI(
        title=f"{settings.app_name} API",
        description=settings.app_description,
        version=settings.app_version,
        debug=settings.debug,
    )

    application.include_router(api_router)

    return application


app = create_app()