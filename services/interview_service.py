from services.gemini_client import ask_gemini
from prompts.interview_prompts import (
    interview_prompt,
    interview_questions_from_code_prompt
)

def generate_interview_answer(question):
    return ask_gemini(interview_prompt(question))

def generate_interview_questions_from_code(code):
    return ask_gemini(interview_questions_from_code_prompt(code))
