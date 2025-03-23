from src.presentation.fastapi.routes.auth import ROUTER as AUTH_ROUTER
from fastapi import FastAPI


def setup_routes(app: FastAPI):
    app.include_router(AUTH_ROUTER)

