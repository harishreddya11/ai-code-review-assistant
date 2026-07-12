from pydantic import BaseModel


class AIResponse(BaseModel):
    task: str
    language: str
    result: str
    model: str