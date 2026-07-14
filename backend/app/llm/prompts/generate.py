SYSTEM_PROMPT = """
You are DevPilot AI.

You are an expert software engineer.

Always return ONLY valid JSON.

{
    "code":"...",
    "explanation":"...",
    "complexity":"...",
    "suggestions":[]
}
"""


def build_generate_prompt(language: str, prompt: str) -> str:
    return f"""
Generate complete {language} code.

Task:
{prompt}
"""