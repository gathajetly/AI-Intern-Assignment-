# backend/app/api/routes/retrieval.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/retrieve", tags=["Grounded Retrieval"])
class RetrievalRequest(BaseModel):
    document_id: str
    query: str
    top_k: int = 3

class Evidence(BaseModel):
    chunk_id: str
    text_segment: str
    relevance_score: float

class RetrievalResponse(BaseModel):
    query: str
    retrieved_evidence: list[Evidence]

@router.post("/", response_model=RetrievalResponse)
async def retrieve_evidence(request: RetrievalRequest):
    """
    Surfaces relevant passages for a given drafting task so generation is anchored to source material.
    """
    mock_evidence = Evidence(
        chunk_id="chunk_01",
        text_segment="The tenant failed to provide the required 30-day notice...",
        relevance_score=0.89
    )
    return RetrievalResponse(
        query=request.query,
        retrieved_evidence=[mock_evidence]
    )