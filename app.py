import streamlit as st

st.set_page_config(page_title="HealthGuard AI")

st.title("🩺 HealthGuard AI")

st.subheader("AI-powered preventive healthcare assistant")

uploaded_file = st.file_uploader(
    "Upload your medical report",
    type=["pdf"]
)

if uploaded_file:
    st.success("Medical report uploaded successfully!")