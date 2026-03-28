from PyPDF2 import PdfReader

# 📄 Extract text from PDF
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

    return text


# 🎯 Role-based keywords
def get_keywords_by_role(role):
    if role == "Data Scientist":
        return ["python", "machine learning", "data science", "pandas", "numpy"]
    
    elif role == "Web Developer":
        return ["html", "css", "javascript", "react", "node"]
    
    elif role == "AI Engineer":
        return ["python", "deep learning", "tensorflow", "nlp", "ai"]

    return []


# 🧠 Analyze resume
def analyze_resume(resume_text, role):
    keywords = get_keywords_by_role(role)

    score = 0
    resume_lower = resume_text.lower()

    found = []
    missing = []

    for kw in keywords:
        if kw in resume_lower:
            found.append(kw)
            score += 1
        else:
            missing.append(kw)

    suggestions = [f"Add {kw}" for kw in missing]

    return score, found, missing, suggestions