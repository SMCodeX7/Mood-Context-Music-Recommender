from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


async def http_exception_handler(
    request: Request,
    exception: StarletteHTTPException,
) -> JSONResponse:
    return JSONResponse(
        status_code=exception.status_code,
        content={
            "error": {
                "status_code": exception.status_code,
                "detail": exception.detail,
                "path": request.url.path,
            }
        },
        headers=exception.headers,
    )


def register_exception_handlers(application: FastAPI) -> None:
    application.add_exception_handler(
        StarletteHTTPException,
        http_exception_handler,
    )