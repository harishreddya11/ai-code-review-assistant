from pydantic import BaseModel

from app.schemas.task import TaskType


class AIRequest(BaseModel):
    task: TaskType

    language: str

    prompt: str | None = None

    code: str | None = None