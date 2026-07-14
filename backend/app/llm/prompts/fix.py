def build_fix_prompt(language: str, code: str) -> str:
    return f"""
Fix bugs in this {language} code.

Code:

{code}
"""