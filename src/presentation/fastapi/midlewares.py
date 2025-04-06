from fastapi import Depends, HTTPException, Security, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session

from src.application.schemas.user import UserResponse
from src.infrastructure.postgres.repositories.user import (
    user_repository
)
from src.core.security import auth_service
from src.infrastructure.postgres.client import get_db_session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token", auto_error=False)


async def get_current_user(
    token: str = Security(oauth2_scheme),
    db_session: Session = Depends(get_db_session),
) -> UserResponse:
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header missing or invalid",
        )

    try:
        user_id = auth_service.verify_token(token)

        user = user_repository.get_user(user_id, db_session)
        return user

    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal authentication error",
        )