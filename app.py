import streamlit as st
from helper import extract_text_from_pdf, summarize_text, answer_question

st.set_page_config(page_title="📄 Doc Summary & QA", layout="centered")

st.title("📄 Document Summarization & QA (Cohere-Powered)")

uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file:
    with st.spinner("🔍 Reading document..."):
        text = extract_text_from_pdf(uploaded_file)

    summary = None
    if st.button("📝 Summarize Document"):
        with st.spinner("✍️ Generating summary..."):
            summary = summarize_text(text)
        st.subheader("📌 Summary")
        st.write(summary)

        # Download summary as text file
        st.download_button(
            label="⬇️ Download Summary",
            data=summary,
            file_name="document_summary.txt",
            mime="text/plain"
        )

    st.subheader("❓ Ask a Question")
    question = st.text_input("Type your question about the document")
    if st.button("💬 Get Answer") and question:
        with st.spinner("🤖 Thinking..."):
            answer = answer_question(text, question)
        st.subheader("✅ Answer")
        st.write(answer)

        # Download answer as text file
        st.download_button(
            label="⬇️ Download Answer",
            data=answer,
            file_name="document_answer.txt",
            mime="text/plain"
        )
