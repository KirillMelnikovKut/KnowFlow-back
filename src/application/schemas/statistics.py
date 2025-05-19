from pydantic import BaseModel


class StatisticsResponse(BaseModel):
    user_id: int
    block_id: int
    statistics: float

class StatisticsRequest(BaseModel):
    block_id: int
    statistics: float