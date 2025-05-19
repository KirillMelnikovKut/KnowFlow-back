from typing import List

from fastapi import APIRouter, Depends
from src.application.schemas.statistics import StatisticsResponse, StatisticsRequest
from src.application.schemas.user import UserLogin, UserResponse, Token
from src.infrastructure.postgres.models.user import User
from src.infrastructure.postgres.models.user_blocks import UserBlocks
from src.infrastructure.postgres.repositories.user_blocks import user_blocks_repository
from sqlmodel import Session as DBSession
from src.infrastructure.postgres.client import get_db_session
from src.core.security import auth_service
from src.presentation.fastapi.midlewares import get_current_user

ROUTER = APIRouter(
    prefix="/statistics",
    tags=["statistics"]
)


@ROUTER.post("", response_model=StatisticsResponse)
def add_user_block(request: StatisticsRequest, user: User = Depends(get_current_user), db_session: DBSession = Depends(get_db_session)):
    return user_blocks_repository.create_user_block(user.id, request.block_id, request.statistics, db_session)


@ROUTER.get("", response_model=List[StatisticsResponse])
def get_user_blocks(user: User = Depends(get_current_user), db_session: DBSession = Depends(get_db_session)):
    return user_blocks_repository.get_user_blocks(user.id, db_session)
