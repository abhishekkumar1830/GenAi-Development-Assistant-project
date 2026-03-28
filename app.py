import streamlit as st
import time

# ⚠️ MUST BE FIRST
st.set_page_config(page_title="GenAI Assistant", layout="wide")

# 🔐 AUTH
from services.auth_service import create_user_table, register_user, login_user

# 🚀 FEATURES
from services.code_service import explain_code, debug_code, optimize_code
from services.interview_service import generate_interview_answer, generate_interview_questions_from_code
from services.project_idea_service import analyze_project_with_gemini

# DB INIT
create_user_table()

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "menu" not in st.session_state:
    st.session_state.menu = "Explain Code"

if "show_menu" not in st.session_state:
    st.session_state.show_menu = False

if "username" not in st.session_state:
    st.session_state.username = ""

# ---------------- AUTH ----------------
if not st.session_state.logged_in:

    st.markdown("""
    <div style="text-align:center;">
        <h1 style="
            font-size:3rem;
            font-weight:900;
            background: linear-gradient(90deg, #64ffda, #00bcd4, #4facfe);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;">
            🚀 GenAI Developer Assistant
        </h1>
        <p style="color:#8892b0;">Login or create account</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2,2,2])

    with col2:
        option = st.radio("", ["Login", "Sign Up"], horizontal=True)

        username = st.text_input("👤 Username")
        password = st.text_input("🔑 Password", type="password")

        if option == "Sign Up":
            if st.button("✨ Create Account"):
                if register_user(username, password):
                    st.success("Account created")
                else:
                    st.error("Username exists")
        else:
            if st.button("🚀 Login"):
                user = login_user(username, password)
                if user:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.error("Invalid credentials")

    st.stop()

# ---------------- CSS ----------------
st.markdown("""
<style>
.block-container { padding-top: 0.5rem !important; }

.stApp {
    background: linear-gradient(-45deg, #0a192f, #112240, #020c1b, #0f3460);
    background-size: 400% 400%;
    animation: gradientBG 10s ease infinite;
    color: #ccd6f6;
}

.main-title {
    font-size: 3rem;
    font-weight: 900;
    background: linear-gradient(90deg, #64ffda, #00bcd4, #4facfe);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.tagline { color: #8892b0; }

.nav-card {
    background: rgba(255,255,255,0.05);
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 20px;
}

div.stButton > button {
    width: 100%;
    height: 38px;
    background: rgba(255,255,255,0.05);
    color: #ccd6f6;
    border-radius: 8px;
    border: 1px solid rgba(100,255,218,0.2);
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #64ffda, #00bcd4);
    color: #0a192f;
    transform: translateY(-3px);
}

textarea {
    background: rgba(255,255,255,0.05) !important;
    border-radius: 10px !important;
    border: 1px solid #233554 !important;
    color: #e6f1ff !important;
}

header, footer {visibility: hidden;}

@keyframes gradientBG {
    0% {background-position: 0%}
    50% {background-position: 100%}
    100% {background-position: 0%}
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
col1, col2 = st.columns([6,1])

with col1:
    st.markdown(f"""
    <div class="main-title">🚀 GenAI Developer Assistant</div>
    <div class="tagline">⚡ Welcome {st.session_state.username}</div>
    """, unsafe_allow_html=True)

with col2:
    c1, c2 = st.columns([1,1])

    with c1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=45)

    with c2:
        if st.button("☰"):
            st.session_state.show_menu = not st.session_state.show_menu

    if st.session_state.show_menu:
        st.write(f"👤 {st.session_state.username}")
        if st.button("🔓 Logout"):
            st.session_state.logged_in = False
            st.session_state.show_menu = False
            st.rerun()

# ---------------- NAVBAR ----------------
features = [
    "Explain Code","Debug Code","Optimize Code",
    "Interview Answer","Code Questions","Project Analyzer",
    "Resume Analyzer"
]

st.markdown('<div class="nav-card">', unsafe_allow_html=True)

rows = [features[:3], features[3:6], features[6:]]

for row in rows:
    cols = st.columns(3)
    for i,f in enumerate(row):
        with cols[i]:
            if st.button(f):
                st.session_state.menu = f

st.markdown('</div>', unsafe_allow_html=True)

menu = st.session_state.menu

# ---------------- COMMON ----------------
def action_buttons(label):
    c1,c2 = st.columns([2,1])
    return c1.button(label), c2.button("🧹 Clear")

def code_input(label):
    return st.text_area(label, height=250)

def feature_layout(title, image_url):
    left, right = st.columns([3,1])
    with left:
        st.markdown(f"""
        <h2 style="
            font-size:2.2rem;
            font-weight:800;
            background: linear-gradient(90deg, #64ffda, #00bcd4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;">
            {title}
        </h2>
        """, unsafe_allow_html=True)
    with right:
        st.image(image_url, width=140)

# ---------------- FEATURES ----------------

if menu == "Explain Code":
    feature_layout("🧠 Code Explainer","https://cdn-icons-png.flaticon.com/512/1006/1006363.png")
    code = code_input("Paste code")
    run,_ = action_buttons("Explain")
    if run and code:
        with st.spinner("⏳ Analyzing code..."):
            result = explain_code(code[:2000])
        st.write(result)

elif menu == "Debug Code":
    feature_layout("🐞 Code Debugger","https://cdn-icons-png.flaticon.com/512/1828/1828843.png")
    code = code_input("Paste code")
    run,_ = action_buttons("Debug")
    if run and code:
        with st.spinner("🐞 Debugging..."):
            result = debug_code(code[:2000])
        st.write(result)

elif menu == "Optimize Code":
    feature_layout("⚡ Code Optimizer","https://cdn-icons-png.flaticon.com/512/190/190411.png")
    code = code_input("Paste code")
    run,_ = action_buttons("Optimize")
    if run and code:
        with st.spinner("⚡ Optimizing..."):
            result = optimize_code(code[:2000])
        st.write(result)

elif menu == "Interview Answer":
    feature_layout("🎯 Interview Answer Generator","https://cdn-icons-png.flaticon.com/512/3135/3135715.png")
    q = st.text_input("Question")
    run,_ = action_buttons("Generate")
    if run and q:
        with st.spinner("💡 Generating answer..."):
            result = generate_interview_answer(q[:2000])
        st.write(result)

elif menu == "Code Questions":
    feature_layout("💡 Code Interview Questions","https://cdn-icons-png.flaticon.com/512/2721/2721297.png")
    code = code_input("Paste code")
    run,_ = action_buttons("Generate")
    if run and code:
        with st.spinner("🧠 Creating questions..."):
            result = generate_interview_questions_from_code(code[:3000])
        st.write(result)

elif menu == "Project Analyzer":
    feature_layout("🚀 Project Idea Analyzer","https://cdn-icons-png.flaticon.com/512/2942/2942789.png")
    idea = st.text_input("Idea")
    req = st.text_area("Requirements")
    run,_ = action_buttons("Analyze")
    if run:
        with st.spinner("🚀 Analyzing project..."):
            result = analyze_project_with_gemini(idea, req)
        st.write(result)

elif menu == "Resume Analyzer":
    feature_layout("📄 Resume Analyzer","https://cdn-icons-png.flaticon.com/512/3135/3135768.png")

    role = st.selectbox("Role", ["Data Scientist","Web Developer","AI Engineer"])
    file = st.file_uploader("Upload PDF", type=["pdf"])

    run,_ = action_buttons("Analyze Resume")

    if run and file:
        from services.resume_service import extract_text_from_pdf, analyze_resume

        with st.spinner("📄 Analyzing resume..."):
            text = extract_text_from_pdf(file)

            if text.strip():
                score, found, missing, suggestions = analyze_resume(text, role)

                if score <= 2:
                    color = "#ff5252"
                elif score == 3:
                    color = "#ffa726"
                else:
                    color = "#00e676"

                st.markdown(f"""
                <div style='text-align:center;
                            font-size:30px;
                            font-weight:bold;
                            background:{color};
                            padding:15px;
                            border-radius:10px;
                            box-shadow: 0 0 20px {color};
                            width:100%;'>
                🎯 Score: {score}/5
                </div>
                """, unsafe_allow_html=True)

                st.progress(score / 5)

                st.write("✅ Found:", found)
                st.write("❌ Missing:", missing)

                for s in suggestions:
                    st.write("•", s)

            else:
                st.error("Could not read PDF")

# ---------------- FOOTER ----------------
st.markdown("""
<hr style="margin-top:40px; border:0.5px solid #233554;">

<div style="text-align:center; color:#8892b0; font-size:14px;">
    🚀 Built with ❤️ using GenAI Assistant <br>
    © 2026 All Rights Reserved
</div>
""", unsafe_allow_html=True)