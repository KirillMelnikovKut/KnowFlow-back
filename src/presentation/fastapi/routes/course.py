from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session as DBSession
from src.infrastructure.postgres.client import get_db_session
from src.application.schemas.course import (
    CourseCreate, BlockCreate, QuestionCreate, AnswerOptionCreate,
    CourseResponse, BlockResponse, QuestionResponse, AnswerOptionResponse
)
from src.infrastructure.postgres.repositories.course import CourseRepository, BlockRepository, QuestionRepository, \
    AnswerOptionRepository

ROUTER = APIRouter(
    prefix="/courses",
    tags=["courses"]
)

course_repository = CourseRepository()
block_repository = BlockRepository()
question_repository = QuestionRepository()
answer_option_repository = AnswerOptionRepository()

# Ручка для создания нового курса
@ROUTER.post("/", response_model=CourseResponse)
def create_course(course_data: CourseCreate, db_session: DBSession = Depends(get_db_session)):
    course = course_repository.create_course(course_data, db_session)
    return course

# Ручка для добавления блока в курс
@ROUTER.post("/{course_id}/blocks", response_model=BlockResponse)
def create_block(course_id: int, block_data: BlockCreate, db_session: DBSession = Depends(get_db_session)):
    block_data.course_id = course_id
    block = block_repository.create_block(block_data, db_session)
    return block

# Ручка для добавления вопроса в блок
@ROUTER.post("/{course_id}/blocks/{block_id}/questions", response_model=QuestionResponse)
def create_question(block_id: int, question_data: QuestionCreate, db_session: DBSession = Depends(get_db_session)):
    question_data.block_id = block_id
    question = question_repository.create_question(question_data, db_session)
    return question

# Ручка для добавления варианта ответа к вопросу
@ROUTER.post("/{course_id}/blocks/{block_id}/questions/{question_id}/answers", response_model=AnswerOptionResponse)
def create_answer_option(question_id: int, answer_data: AnswerOptionCreate, db_session: DBSession = Depends(get_db_session)):
    answer_data.question_id = question_id
    answer = answer_option_repository.create_answer_option(answer_data, db_session)
    return answer

# Ручка для получения всех курсов
@ROUTER.get("/", response_model=List[CourseResponse])
def get_all_courses(db_session: DBSession = Depends(get_db_session)):
    courses = course_repository.get_all_courses(db_session)
    return courses

# Ручка для получения конкретного курса по ID
@ROUTER.get("/{course_id}", response_model=CourseResponse)
def get_course(course_id: int, db_session: DBSession = Depends(get_db_session)):
    course = course_repository.get_course_by_id(course_id, db_session)
    if not course:
        raise HTTPException(status_code=404, detail="Курс не найден")
    return course

# Ручка для получения всех блоков курса
@ROUTER.get("/{course_id}/blocks", response_model=List[BlockResponse])
def get_blocks_by_course_id(course_id: int, db_session: DBSession = Depends(get_db_session)):
    blocks = block_repository.get_blocks_by_course_id(course_id, db_session)
    return blocks

# Ручка для получения всех вопросов блока
@ROUTER.get("/{course_id}/blocks/{block_id}/questions", response_model=List[QuestionResponse])
def get_questions_by_block_id(block_id: int, db_session: DBSession = Depends(get_db_session)):
    questions = question_repository.get_questions_by_block_id(block_id, db_session)
    return questions

# Ручка для получения всех вариантов ответов для вопроса
@ROUTER.get("/{course_id}/blocks/{block_id}/questions/{question_id}/answers", response_model=List[AnswerOptionResponse])
def get_answer_options_by_question_id(question_id: int, db_session: DBSession = Depends(get_db_session)):
    answers = answer_option_repository.get_answer_options_by_question_id(question_id, db_session)
    return answers