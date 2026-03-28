import google.generativeai as genai
from utils.cleaner import clean_text
from dotenv import load_dotenv
import os
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-3-flash-preview")

def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return clean_text(response.text)
