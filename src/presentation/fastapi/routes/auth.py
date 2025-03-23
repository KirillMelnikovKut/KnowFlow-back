from fastapi import APIRouter, Depends
from src.application.schemas.user import UserLogin
from src.application.schemas.user import UserLogin, UserResponse, Token
from src.infrastructure.postgres.repositories.user import user_repository
from sqlmodel import Session as DBSession
from src.infrastructure.postgres.client import get_db_session
from src.core.security import auth_service

ROUTER = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@ROUTER.post("/register", response_model=UserResponse)
def register(request: UserLogin, db_session: DBSession = Depends(get_db_session)):
    user = user_repository.create_user(request, db_session)
    token = auth_service.create_access_token(user.id)
    return {"access_token": token, "token_type": "Bearer"}


@ROUTER.post("/login", response_model=Token)
def login(request: UserLogin, db_session: DBSession = Depends(get_db_session)):
    user = user_repository.authenticate_user(request, db_session)
    token = auth_service.create_access_token(user.id)
    return {"access_token": token, "token_type": "Bearer"}
