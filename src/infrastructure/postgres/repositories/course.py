from typing import List
from sqlalchemy.orm import Session
from src.application.schemas.course import CourseCreate, BlockCreate, QuestionCreate, AnswerOptionCreate
from src.infrastructure.postgres.models.course import Course, AnswerOption, Question, Block


class CourseRepository:
    def create_course(self, course_data: CourseCreate, db_session: Session) -> Course:
        course = Course(**course_data.dict())
        db_session.add(course)
        db_session.commit()
        db_session.refresh(course)
        return course

    def get_course_by_id(self, course_id: int, db_session: Session) -> Course:
        return db_session.query(Course).filter(Course.id == course_id).first()

    def get_all_courses(self, db_session: Session) -> List[Course]:
        return db_session.query(Course).all()


class BlockRepository:
    def create_block(self, block_data: BlockCreate, db_session: Session) -> Block:
        block = Block(**block_data.dict())
        db_session.add(block)
        db_session.commit()
        db_session.refresh(block)
        return block

    def get_blocks_by_course_id(self, course_id: int, db_session: Session) -> List[Block]:
        return db_session.query(Block).filter(Block.course_id == course_id).all()


class QuestionRepository:
    def create_question(self, question_data: QuestionCreate, db_session: Session) -> Question:
        question = Question(**question_data.dict())
        db_session.add(question)
        db_session.commit()
        db_session.refresh(question)
        return question

    def get_questions_by_block_id(self, block_id: int, db_session: Session) -> List[Question]:
        return db_session.query(Question).filter(Question.block_id == block_id).all()


class AnswerOptionRepository:
    def create_answer_option(self, answer_data: AnswerOptionCreate, db_session: Session) -> AnswerOption:
        answer = AnswerOption(**answer_data.dict())
        db_session.add(answer)
        db_session.commit()
        db_session.refresh(answer)
        return answer

    def get_answer_options_by_question_id(self, question_id: int, db_session: Session) -> List[AnswerOption]:
        return db_session.query(AnswerOption).filter(AnswerOption.question_id == question_id).all()