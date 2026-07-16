from app.core.config import get_settings
from app.llm.base import LLMProvider
from app.llm.client import get_client
from app.llm.parser import parse_response
from app.llm.prompts import SYSTEM_PROMPT
from app.schemas.ai_request import AIRequest
from app.schemas.ai_response import AIResponse

settings = get_settings()


class OpenAIProvider(LLMProvider):

    def execute(self, request: AIRequest) -> AIResponse:

        client = get_client()

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": request.prompt,
            },
        ]

        print("\n========== REQUEST ==========")
        print(messages)
        print("=============================\n")

        response = client.chat.completions.create(
            model=settings.openrouter_model,
            messages=messages,
        )

        response_text = response.choices[0].message.content or ""

        print("\n======= RAW MODEL RESPONSE =======")
        print(response_text)
        print("==================================\n")

        return parse_response(
            request,
            response_text,
            settings.openrouter_model,
        )

    def stream(self, request: AIRequest):

        client = get_client()

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": request.prompt,
            },
        ]

        stream = client.chat.completions.create(
            model=settings.openrouter_model,
            messages=messages,
            stream=True,
        )

        for chunk in stream:

            if not chunk.choices:
                continue

            delta = chunk.choices[0].delta.content

            if delta:
                yield delta