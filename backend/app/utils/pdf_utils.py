# backend/app/utils/pdf_utils.py
from PIL import Image, ImageEnhance
import os
def preprocess_image_for_ocr(image: Image.Image) -> Image.Image:
    """
    Enhances a messy or low-resolution image to improve OCR extraction quality.
    """
    img = image.convert('L')
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(1.5)
    return img

def is_valid_document(filename: str) -> bool:
    """
    Checks if the uploaded file has a supported extension.
    """
    valid_extensions = {".pdf", ".png", ".jpg", ".jpeg", ".tiff"}
    ext = os.path.splitext(filename)[1].lower()
    return ext in valid_extensions