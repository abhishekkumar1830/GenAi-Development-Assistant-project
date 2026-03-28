def explain_code_prompt(code):
    return f"""
    Explain the following code line by line in simple terms.
    Also mention time complexity if applicable.

    Code:
    {code}
    """

def debug_code_prompt(code):
    return f"""
    Find errors and bugs in the following code and suggest fixes.

    Code:
    {code}
    """

def optimize_code_prompt(code):
    return f"""
    Optimize the following code and explain the improvements.

    Code:
    {code}
    """
