import streamlit as st
import sys
import os

# Fix import path
sys.path.append(os.path.abspath("../src"))

from code_generator import generate_eda_code
from resume_generator import generate_resume
from interview_generator import generate_interview_questions
from summarizer import summarize_meeting

st.set_page_config(page_title="AI Automation System", layout="wide")

st.title("🤖 AI Automation System")
st.subheader("Infosys Capstone Project – Generative AI Application")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Code Generator",
    "📄 Resume Generator",
    "🎯 Interview Questions",
    "📝 Meeting Summarizer"
])

# -------------------------------
# TAB 1: CODE GENERATOR
# -------------------------------
with tab1:
    st.header("📊 Data Analysis Code Generator")

    dataset_desc = st.text_area("Enter dataset description:")

    if st.button("Generate Code"):
        if dataset_desc:
            result = generate_eda_code(dataset_desc)
            st.code(result, language="python")
        else:
            st.warning("Please enter dataset description")

# -------------------------------
# TAB 2: RESUME GENERATOR
# -------------------------------
with tab2:
    st.header("📄 Resume Generator")

    resume_input = st.text_area("Enter your details:")

    if st.button("Generate Resume"):
        if resume_input:
            result = generate_resume(resume_input)
            st.write(result)
        else:
            st.warning("Please enter your details")

# -------------------------------
# TAB 3: INTERVIEW QUESTIONS
# -------------------------------
with tab3:
    st.header("🎯 Interview Question Generator")

    language = st.selectbox("Select Language", ["Python", "Java", "C++", "JavaScript"])
    level = st.selectbox("Difficulty Level", ["fresher", "intermediate"])

    if st.button("Generate Questions"):
        result = generate_interview_questions(language, level)
        st.write(result)

# -------------------------------
# TAB 4: SUMMARIZER
# -------------------------------
with tab4:
    st.header("📝 Meeting Notes Summarizer")

    notes = st.text_area("Enter meeting notes:")

    if st.button("Summarize"):
        if notes:
            result = summarize_meeting(notes)
            st.write(result)
        else:
            st.warning("Please enter notes")
