from fastapi import FastAPI
from fastapi_pagination import add_pagination
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from app.config.settings import settings
from app.routers import router


def create_app() -> FastAPI:
    """
    Create a FastAPI application instance.
    Returns
    ----------
        FastAPI application instance
    """
    app: FastAPI = FastAPI(title=settings.SERVER_NAME)
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_headers=["*"],
        allow_methods=["*"],
        allow_origins=["*"],
    )
    app.include_router(router)

    @app.get("/")
    async def root():
        return RedirectResponse(url="/docs")

    add_pagination(app)
    return app
