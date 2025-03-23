from fastapi import FastAPI

from src.presentation.fastapi.setup_routes import setup_routes

app = FastAPI(
    title="User Auth API",
    description="REST API для регистрации и авторизации пользователей",
    version="1.0.0"
)

setup_routes(app)
