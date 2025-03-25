from typing import List
from pydantic import BaseModel
from datetime import datetime

class CourseCreate(BaseModel):
    title: str
    description: str

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

class CourseResponse(BaseModel):
    id: int
    title: str
    description: str
    created_at: datetime

class BlockResponse(BaseModel):
    id: int
    title: str
    content: str
    order: int
    course_id: int

class QuestionResponse(BaseModel):
    id: int
    text: str
    order: int
    block_id: int

class AnswerOptionResponse(BaseModel):
    id: int
    text: str
    is_correct: bool
    question_id: int