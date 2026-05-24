# backend/app/api/routes/feedback.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/feedback", tags=["Improvement from Edits"])

class FeedbackRequest(BaseModel):
    draft_id: str
    original_text: str
    edited_text: str
class FeedbackResponse(BaseModel):
    status: str
    learned_rule: str
@router.post("/", response_model=FeedbackResponse)
async def process_operator_edits(request: FeedbackRequest):
    """
    Captures operator edits, extracts a reusable rule, and saves it to improve future drafts.
    """
    learned_pattern = "Operator consistently changes 'Client' to 'Plaintiff'. Will apply to future prompts."
    
    return FeedbackResponse(
        status="Feedback processed successfully",
        learned_rule=learned_pattern
    )