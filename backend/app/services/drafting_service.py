import google.generativeai as genai
from app.core.config import settings
if settings.gemini_api_key:
    genai.configure(api_key=settings.gemini_api_key)

def generate_draft(draft_type: str, evidence: list[dict], learned_rules: list[str]) -> str:
    """
    Generates a grounded draft using retrieved evidence and past learned rules.
    """
    context = "\n\n".join([f"[ID: {e['chunk_id']}] {e['text']}" for e in evidence])
    rules_text = "\n".join([f"- {rule}" for rule in learned_rules]) if learned_rules else "None"
    
    prompt = f"""
    You are an AI Legal Drafter. Generate a '{draft_type}' based strictly on the provided evidence.
    
    Rules to follow based on past operator feedback:
    {rules_text}
    
    CRITICAL: 
    1. Ground all claims in the evidence.
    2. Do not invent confident-sounding assumptions.
    3. Cite the evidence using the chunk ID, like this: "Fact goes here. [ID: doc_1_chunk_2]".
    
    EVIDENCE:
    {context}
    """
    
    if not settings.gemini_api_key:
        return f"Mock Draft generated from evidence: {context[:100]}..."

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.2,
            )
        )
        return response.text
        
    except Exception as e:
        print(f"Drafting error: {e}")
        return "Failed to generate draft."