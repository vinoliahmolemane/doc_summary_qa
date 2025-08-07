import cohere
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def summarize_text(text):
    response = co.summarize(
        text=text,
        length='medium',
        format='paragraph',
        model='command-r-plus'
    )
    return response.summary

def answer_question(text, question):
    prompt = f"""You are a helpful assistant. Use the following document to answer the question.

Document:
{text}

Question:
{question}

Answer:"""

    response = co.generate(
        model="command-r-plus",
        prompt=prompt,
        max_tokens=300,
        temperature=0.3
    )
    return response.generations[0].text.strip()
