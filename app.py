import streamlit as st
from pypdf import PdfReader

st.set_page_config(page_title="HealthGuard AI")

st.title("🩺 HealthGuard AI")
st.subheader("AI-powered preventive healthcare assistant")

uploaded_file = st.file_uploader(
    "Upload your medical report",
    type=["pdf"]
)

if uploaded_file:

    st.success("Medical report uploaded successfully!")

    pdf_reader = PdfReader(uploaded_file)

    extracted_text = ""

    for page in pdf_reader.pages:
        extracted_text += page.extract_text()

    st.subheader("Extracted Medical Report Text")

    st.text_area(
        "Medical Report Content",
        extracted_text,
        height=300
    )