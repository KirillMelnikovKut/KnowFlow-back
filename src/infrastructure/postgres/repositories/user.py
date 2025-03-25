from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from src.infrastructure.postgres.models.user import User
from src.application.schemas.user import UserLogin
from src.core.security import auth_service


class UserRepository:
    def create_user(self, user_data: UserLogin, db: Session):
        existing_user = db.query(User).filter_by(email=user_data.email).first()
        if existing_user:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")
        user_data.password = auth_service.hash_password(user_data.password)
        db_user = User(**user_data.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def authenticate_user(self, user_data: UserLogin, db: Session):
        user = db.query(User).filter_by(email=user_data.email).first()
        if not user or not auth_service.verify_password(user_data.password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return user


user_repository = UserRepository()
