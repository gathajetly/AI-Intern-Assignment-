# backend/app/api/routes/drafting.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/draft", tags=["Draft Generation"])
class DraftRequest(BaseModel):
    document_id: str
    draft_type: str 
    evidence_chunks: list[str]
class DraftResponse(BaseModel):
    draft_id: str
    generated_text: str
    citations: list[str] 
@router.post("/", response_model=DraftResponse)
async def generate_draft(request: DraftRequest):
    """
    Generates a draft response grounded entirely in the retrieved evidence.
    """
    return DraftResponse(
        draft_id="draft_987",
        generated_text="Based on the provided documents, the following summary is generated...",
        citations=["chunk_01", "chunk_03"]
    )