from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.presentation.fastapi.setup_routes import setup_routes

app = FastAPI(
    title="User Auth API",
    description="REST API для регистрации и авторизации пользователей",
    version="1.0.0"
)

origins = [
    "http://localhost:5173",
    "http://158.255.0.90:8081"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

setup_routes(app)