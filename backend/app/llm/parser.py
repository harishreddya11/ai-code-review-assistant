from app.schemas.ai_request import AIRequest
from app.schemas.ai_response import AIResponse


def parse_response(
    request: AIRequest,
    response_text: str,
    model: str,
) -> AIResponse:

    return AIResponse(
        response=response_text,
        model=model,
    )