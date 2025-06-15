from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
    return text

def get_text_chunks(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=50000, chunk_overlap=1000)
    return splitter.split_text(text)
