from fastapi import FastAPI

from backend.app.api.router import api_router
from backend.app.core.config import get_settings
from backend.app.core.exception_handlers import register_exception_handlers


def create_app() -> FastAPI:
    settings = get_settings()

    application = FastAPI(
        title=f"{settings.app_name} API",
        description=settings.app_description,
        version=settings.app_version,
        debug=settings.debug,
    )

    register_exception_handlers(application)

    application.include_router(
        api_router,
        prefix=settings.api_v1_prefix,
    )

    return application


app = create_app()