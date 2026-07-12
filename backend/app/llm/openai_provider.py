from app.llm.base import LLMProvider
from app.schemas.ai_request import AIRequest
from app.schemas.ai_response import AIResponse


class OpenAIProvider(LLMProvider):

    def execute(self, request: AIRequest) -> AIResponse:

        if request.task == "generate":
            result = f"Generated {request.language} code for: {request.prompt}"

        elif request.task == "review":
            result = "Reviewed the submitted code."

        elif request.task == "explain":
            result = "Explained the submitted code."

        elif request.task == "fix":
            result = "Fixed the submitted code."

        else:
            result = "Unsupported task."

        return AIResponse(
        task=request.task.value,
        language=request.language,
        result=result,
        model="dummy-model"
)