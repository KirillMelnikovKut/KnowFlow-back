from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from src.infrastructure.postgres.client import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)  # Название курса
    description = Column(Text, nullable=True)  # Описание курса
    video = Column(String, nullable=True)  # Ссылка на видео (новое поле)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)  # Дата создания курса
    # Связь с блоками курса (один ко многим)
    blocks = relationship("Block", back_populates="course", cascade="all, delete-orphan")

class Block(Base):
    __tablename__ = "blocks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)  # Название блока
    content = Column(Text, nullable=False)  # Текстовый контент блока
    order = Column(Integer, nullable=False)  # Порядок блока в курсе
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)  # Связь с курсом

    # Связь с курсом (многие к одному)
    course = relationship("Course", back_populates="blocks")

    # Связь с вопросами (один ко многим)
    questions = relationship("Question", back_populates="block", cascade="all, delete-orphan")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)  # Текст вопроса
    order = Column(Integer, nullable=False)  # Порядок вопроса в блоке
    block_id = Column(Integer, ForeignKey("blocks.id"), nullable=False)  # Связь с блоком

    # Связь с блоком (многие к одному)
    block = relationship("Block", back_populates="questions")

    # Связь с вариантами ответов (один ко многим)
    answer_options = relationship("AnswerOption", back_populates="question", cascade="all, delete-orphan")


class AnswerOption(Base):
    __tablename__ = "answer_options"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)  # Текст варианта ответа
    is_correct = Column(Boolean, default=False, nullable=False)  # Правильный ли ответ
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)  # Связь с вопросом

    # Связь с вопросом (многие к одному)
    question = relationship("Question", back_populates="answer_options")