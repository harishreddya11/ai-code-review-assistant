SYSTEM_PROMPT = """
You are DevPilot AI.

You are an expert software engineer.

Always return ONLY valid JSON.

Return this format:

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


def build_review_prompt(language: str, code: str) -> str:
    return f"""
Review this {language} code.

Return:
- improved code
- explanation
- complexity
- suggestions

Code:

{code}
"""


def build_explain_prompt(language: str, code: str) -> str:
    return f"""
Explain this {language} code.

Code:

{code}
"""


def build_fix_prompt(language: str, code: str) -> str:
    return f"""
Fix bugs in this {language} code.

Code:

{code}
"""