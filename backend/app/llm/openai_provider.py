from app.core.config import get_settings
from app.llm.base import LLMProvider
from app.llm.parser import parse_response
from app.schemas.task import TaskType
from app.llm.client import get_client
from app.llm.prompts import (
    SYSTEM_PROMPT,
    build_generate_prompt,
    build_review_prompt,
    build_explain_prompt,
    build_fix_prompt,
)
from app.schemas.ai_request import AIRequest
from app.schemas.ai_response import AIResponse
from app.schemas.task import TaskType

settings = get_settings()


class OpenAIProvider(LLMProvider):

    def execute(self, request: AIRequest) -> AIResponse:

        client = get_client()

        if request.task == TaskType.GENERATE:
            prompt = build_generate_prompt(
                request.language,
                request.prompt or "",
           )

        elif request.task == TaskType.REVIEW:
            prompt = build_review_prompt(
                request.language,
                request.code or "",
            )

        elif request.task == TaskType.EXPLAIN:
            prompt = build_explain_prompt(
                request.language,
                request.code or "",
            )

        elif request.task == TaskType.FIX:
            prompt = build_fix_prompt(
                request.language,
                request.code or "",
            )

        else:
            raise ValueError("Unsupported task")
        
        
        response = client.chat.completions.create(
            model=settings.openrouter_model,
           messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": prompt,
                },

            ],
        )

        response_text = response.choices[0].message.content or ""

        return parse_response(
        request,
        response_text,
        settings.openrouter_model,
)