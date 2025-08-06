# file_processor.py
import os

from pdf_utils import extract_text_from_pdf
from docx_utils import extract_text_from_docx
from email_utils import extract_text_from_email

def extract_text(file_path):
    ext = os.path.splitext(file_path)[-1].lower()

    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    elif ext == ".msg":
        return extract_text_from_email(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")
