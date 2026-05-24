# backend/app/services/ocr_service.py
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import os

def extract_text(file_path: str) -> str:
    """
    Extracts text from PDFs or images. Handles messy/scanned inputs using OCR.
    """
    ext = os.path.splitext(file_path)[1].lower()
    extracted_text = ""
    try:
        if ext == ".pdf":
            doc = fitz.open(file_path)
            for page in doc:
                page_text = page.get_text()
                if page_text.strip():
                    extracted_text += page_text + "\n"
                else:
                    pix = page.get_pixmap()
                    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                    extracted_text += pytesseract.image_to_string(img) + "\n"
            doc.close()
        elif ext in [".jpg", ".jpeg", ".png", ".tiff"]:
            img = Image.open(file_path)
            extracted_text = pytesseract.image_to_string(img)
        return extracted_text.strip()
    except Exception as e:
        print(f"Error processing document: {e}")
        return "Extraction failed."