def build_explain_prompt(language: str, code: str) -> str:
    return f"""
Explain the following {language} code.

Code:

{code}
"""