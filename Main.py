import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

st.set_page_config(
    page_title="Meeting Notes Assistant",
    layout="centered"
)

st.title("Meeting Notes Assistant")
st.write("A simple tool for turning  meeting notes into a structured follow-up report.")

if not API_KEY:
    st.error("No Gemini API key found. Please add it in the .env file.")
    st.stop()

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

transcript = st.text_area(
    "Meeting Transcript",
    height=300,
    placeholder="Paste your meeting transcript here..."
)

uploaded_file = st.file_uploader(
    "Upload meeting transcript",
    type=["txt"]
)

if uploaded_file is not None:
    transcript = uploaded_file.read().decode("utf-8")

if st.button("Analyze Meeting"):
    if not transcript.strip():
        st.warning("Please paste a meeting transcript first.")
    else:
        with st.spinner("Analyzing meeting..."):
            prompt = f"""
            Act as a junior project coordinator.

            Read the following meeting notes and turn them into a practical follow-up report.

            Write in a simple and clear way. Avoid overly formal or generic language.

            Include these sections:
            - Quick Summary
            - Main Points Discussed
            - Decisions Made
            - Tasks and Owners
            - Deadlines
            - Possible Risks
            - Suggested Next Steps

            If some information is missing, write "Not mentioned" instead of inventing details.

            Meeting Notes:
            {transcript}
            """
            response = model.generate_content(prompt)
            st.subheader("Generated Meeting Report")

            st.write(
                f"Report generated on {datetime.now().strftime('%d/%m/%Y %H:%M')}"
            )

            st.write(response.text)
