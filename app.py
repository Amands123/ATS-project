import streamlit as st
import fitz
import json
import logging
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import google.generativeai as genai

st.set_page_config(page_title="ATS Gemini Pro", layout="wide")

logging.basicConfig(level=logging.INFO)

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

def extract_text(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    return "\n".join(page.get_text() for page in doc)

def ask_gemini(prompt):
    return model.generate_content(prompt).text

def create_pdf(text):
    buf = BytesIO()
    doc = SimpleDocTemplate(buf)
    styles = getSampleStyleSheet()
    story = [Paragraph("ATS Report", styles["Title"]), Spacer(1,12),
             Paragraph(text.replace("\n","<br/>"), styles["BodyText"])]
    doc.build(story)
    return buf.getvalue()

st.title("🚀 ATS Gemini Pro")

jd = st.text_area("Job Description", height=200)
resume = st.file_uploader("Resume PDF", type=["pdf"])

if resume and jd:
    resume_text = extract_text(resume)

    if st.button("ATS Analysis"):
        prompt = f"Analyze resume against JD. Resume:{resume_text} JD:{jd} Return ATS score, missing keywords, strengths, weaknesses."
        result = ask_gemini(prompt)
        st.write(result)

        pdf_bytes = create_pdf(result)
        st.download_button("Download PDF Report", pdf_bytes, "ats_report.pdf")

    if st.button("Cover Letter"):
        st.write(ask_gemini(f"Create cover letter using resume:{resume_text} and JD:{jd}"))

    if st.button("Interview Questions"):
        st.write(ask_gemini(f"Generate interview questions from resume:{resume_text} and JD:{jd}"))
