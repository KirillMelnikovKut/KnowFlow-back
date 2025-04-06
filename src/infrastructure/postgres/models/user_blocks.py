from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from src.infrastructure.postgres.client import Base

class UserBlocks(Base):
    __tablename__ = "user_blocks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    block_id = Column(Integer, nullable=False) # Текстовый контент блока
    statistics = Column(Float, nullable=False)  # Связь с курсом

    # Связь с пользователем (многие к одному)
    user = relationship("User", back_populates="user_blocks")

    # Связь с блоком (многие к одному)
    block = relationship("Block", back_populates="user_blocks")
