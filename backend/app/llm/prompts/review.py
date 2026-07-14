def build_review_prompt(language: str, code: str) -> str:
    return f"""
Review the following {language} code.

Return:
- improved code
- explanation
- complexity
- suggestions

Code:

{code}
"""