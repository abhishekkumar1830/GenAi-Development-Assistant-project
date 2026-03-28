def interview_prompt(question):
    return f"""
    Answer the following interview question in a professional manner.
    Keep it concise and structured.

    Question:
    {question}
    """

def interview_questions_from_code_prompt(code):
    return f"""
    You are a technical interviewer.

    Analyze the following code and generate:
    1. 5 technical interview questions
    2. 2 debugging questions
    3. 2 optimization-related questions

    Code:
    {code}
    """

