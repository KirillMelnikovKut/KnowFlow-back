from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from src.infrastructure.postgres.client import Base

class UserBlocks(Base):
    __tablename__ = "user_blocks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Связь с пользователем
    block_id = Column(Integer, ForeignKey("blocks.id"), nullable=False)  # Связь с блоком
    statistics = Column(Float, nullable=False)  # Статистика для конкретного пользователя и блока

    # Связь с пользователем (многие к одному)
    user = relationship("User", back_populates="user_blocks")

    # Связь с блоком (многие к одному)
    block = relationship("Block", back_populates="user_blocks")