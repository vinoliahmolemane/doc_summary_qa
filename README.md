# Document Summarization & QA System

A simple web app to **summarize PDF documents** and **answer questions** about their content using **Cohere's AI models**.

---

## Features

- Upload PDF documents and extract text automatically.
- Generate concise summaries of the document content.
- Ask specific questions related to the document.
- Download summaries and answers as text files.
- Built with Python, Streamlit, and Cohere API.

---

## Demo

Run locally and open your browser at `http://localhost:8501` to use the app.

---

## Tech Stack

- Python 3.8+
- Streamlit (Web UI)
- Cohere API (AI Summarization and Q&A)
- PyPDF2 (PDF text extraction)
- python-dotenv (Environment variables)

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/vinoliahmolemane/doc-summary-qa.git
cd doc-summary-qa

Install dependencies
pip install -r requirements.txt

Create .env file with your Cohere API key
COHERE_API_KEY=your-cohere-api-key-here

Run the Streamlit app
streamlit run app.py





