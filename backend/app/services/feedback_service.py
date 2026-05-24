# backend/app/services/feedback_service.py
import google.generativeai as genai
from app.core.config import settings

if settings.gemini_api_key:
    genai.configure(api_key=settings.gemini_api_key)

def extract_learned_rule(original_draft: str, edited_draft: str) -> str:
    """
    Compares the original draft with the operator's edited version to extract a reusable formatting/stylistic rule.
    """
    if not settings.gemini_api_key:
        return "Always format dates as YYYY-MM-DD."

    prompt = f"""
    Compare the Original Draft and the Edited Draft. 
    Identify the core stylistic, structural, or phrasing change the operator made.
    Extract this as a short, reusable rule (1 sentence) that an AI can follow in the future.
    Do not mention specific names or case details, only the underlying pattern.
    
    Original Draft: {original_draft}
    
    Edited Draft: {edited_draft}
    """
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(temperature=0.1)
        )
        return response.text.strip()
        
    except Exception as e:
        print(f"Feedback learning error: {e}")
        return "Failed to extract rule."