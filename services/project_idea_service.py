from services.gemini_client import ask_gemini

def analyze_project_with_gemini(idea, requirements):
    prompt = f"""
You are a senior project architect.

Analyze the following project idea and requirements carefully.

IMPORTANT RULES:
- The project can be ANY domain (IT, Non-IT, Mechanical, Business, Medical, Agriculture, Social, etc.)
- Do NOT assume it is a software project unless required
- Decide whether software development is:
  - Not required
  - Optional
  - Mandatory
- If software is required:
  - Choose the BEST language and tech stack
  - Do NOT repeat generic answers
- If software is NOT required:
  - Provide domain-level execution roadmap
- The output MUST be specific to the idea

Project Idea:
{idea}

Requirements:
{requirements}

Return the analysis in the following format:

1. Project Nature (IT / Non-IT / Hybrid)
2. Usefulness & Real-world Impact
3. Whether Software is Required (Yes / No / Optional)
4. If Yes:
   - Recommended Language & Tech Stack
   - Folder / System Architecture
5. Step-by-step Execution Roadmap
6. Final Verdict (Is it worth building or not, and why)
"""
    return ask_gemini(prompt)
