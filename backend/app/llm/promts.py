SYSTEM_PROMPT = """
You are DevPilot AI.

You are a senior software engineer.

Always:
- Write clean code.
- Follow best practices.
- Explain your reasoning when requested.
- Return complete solutions.
"""

def build_generate_prompt(language: str, prompt: str) -> str:
    return f"""
Generate complete {language} code.

Task:
{prompt}

Return only the code.
"""