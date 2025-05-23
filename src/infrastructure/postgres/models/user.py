from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.infrastructure.postgres.client import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    user_blocks = relationship("UserBlocks", back_populates="user")
