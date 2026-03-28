import streamlit as st
from services.gemini_client import ask_gemini
from prompts.code_prompts import (
    explain_code_prompt,
    debug_code_prompt,
    optimize_code_prompt
)

def explain_code(code):
    return ask_gemini(explain_code_prompt(code))

def debug_code(code):
    return ask_gemini(debug_code_prompt(code))

def optimize_code(code):
    return ask_gemini(optimize_code_prompt(code))

@st.cache_data(show_spinner=False)
def optimize_code_cached(code):
    return ask_gemini(f"Optimize this code:\n{code}")