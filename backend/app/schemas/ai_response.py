from pydantic import BaseModel


class AIResponse(BaseModel):
    response: str
    model: str