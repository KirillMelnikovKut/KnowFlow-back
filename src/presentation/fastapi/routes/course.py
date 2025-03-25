from fastapi import APIRouter, Depends
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