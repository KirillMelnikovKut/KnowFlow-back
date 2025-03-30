from src.presentation.fastapi.routes.auth import ROUTER as AUTH_ROUTER
from src.presentation.fastapi.routes.course import ROUTER as COURSE_ROUTER
from fastapi import FastAPI


def setup_routes(app: FastAPI):
    app.include_router(AUTH_ROUTER)
    app.include_router(COURSE_ROUTER)

