from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from rest_api.core.settings import settings
from .urls import server_routers


def get_application():
    _app = FastAPI(
        title=settings.PROJECT_NAME,
        docs_url="/docs" if settings.DEBUG_MODE else None,
        redoc_url="/redoc" if settings.DEBUG_MODE else None,
    )

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.include_router(server_routers)

    return _app


app = get_application()
