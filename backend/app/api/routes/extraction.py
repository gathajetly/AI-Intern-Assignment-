# backend/app/api/routes/extraction.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/extract", tags=["Document Extraction"])
class ExtractionRequest(BaseModel):
    file_path: str
class ExtractionResponse(BaseModel):
    document_id: str
    raw_text: str
    structured_data: dict 
@router.post("/", response_model=ExtractionResponse)
async def process_document(request: ExtractionRequest):
    """
    Triggers OCR/text extraction over scanned or noisy files and produces structured data.
    """
    return ExtractionResponse(
        document_id="doc_12345",
        raw_text="CONFIDENTIAL RECORD... [messy OCR text goes here]",
        structured_data={"date": "2023-10-25", "case_type": "Notice"}
    )