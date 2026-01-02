import pdfplumber
import requests
import io

def extract_text_from_arxiv_pdf(pdf_url: str) -> str:
    response = requests.get(pdf_url, timeout=20)
    pdf_bytes = io.BytesIO(response.content)

    text = ""
    with pdfplumber.open(pdf_bytes) as pdf:
        for page in pdf.pages[:5]:  # limit pages
            text += page.extract_text() or ""

    return text.strip()
