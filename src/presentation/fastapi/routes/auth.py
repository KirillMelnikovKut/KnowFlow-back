from fastapi import APIRouter, Depends
from src.application.schemas.user import UserLogin, UserCreate, UserResponse
from src.application.schemas.user import UserLogin, UserResponse, Token
from src.infrastructure.postgres.models.user import User
from src.infrastructure.postgres.repositories.user import user_repository
from sqlmodel import Session as DBSession
from src.infrastructure.postgres.client import get_db_session
from src.core.security import auth_service
from src.presentation.fastapi.midlewares import get_current_user

ROUTER = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@ROUTER.post("/register", response_model=Token)
def register(request: UserCreate, db_session: DBSession = Depends(get_db_session)):
    user = user_repository.create_user(request, db_session)
    token = auth_service.create_access_token(user.id)
    return Token(access_token=token, token_type="Bearer")


@ROUTER.post("/login", response_model=Token)
def login(request: UserLogin, db_session: DBSession = Depends(get_db_session)):
    user = user_repository.authenticate_user(request, db_session)
    token = auth_service.create_access_token(user.id)
    return Token(access_token=token, token_type="Bearer")


@ROUTER.post("/me", response_model=UserResponse)
def login(user: User = Depends(get_current_user), db_session: DBSession = Depends(get_db_session)):
    return UserResponse(**user.__dict__)