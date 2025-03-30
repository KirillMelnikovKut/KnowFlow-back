from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class CourseCreate(BaseModel):
    title: str
    description: str
    video: Optional[str] = None

class BlockCreate(BaseModel):
    title: str
    content: str
    order: int
    course_id: int

class QuestionCreate(BaseModel):
    text: str
    order: int
    block_id: int

class AnswerOptionCreate(BaseModel):
    text: str
    is_correct: bool
    question_id: int

class AnswerOptionResponse(BaseModel):
    id: int
    text: str
    is_correct: bool

class QuestionResponse(BaseModel):
    id: int
    text: str
    order: int
    answer_options: List[AnswerOptionResponse]

class BlockResponse(BaseModel):
    id: int
    title: str
    content: str
    order: int
    questions: List[QuestionResponse]

class CourseResponse(BaseModel):
    id: int
    title: str
    description: str
    video: Optional[str] = None
    blocks: List[BlockResponse]