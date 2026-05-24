# backend/app/services/extraction_service.py
import google.generativeai as genai
from app.core.config import settings
import json
import re

if settings.gemini_api_key:
    genai.configure(api_key=settings.gemini_api_key)

def extract_structured_data(raw_text: str) -> dict:
    """
    Uses Gemini to parse messy legal text into structured fields.
    """
    if not settings.gemini_api_key:
        return {"dates": ["2023-10-01"], "parties": ["Client A", "Company B"]}

    prompt = f"""
    Extract the key entities from the following legal text. 
    Return ONLY a valid JSON object with keys: "dates", "parties", "case_numbers", and "document_type".
    Do not include any markdown formatting or explanation. Just the raw JSON.
    
    Text:
    {raw_text[:8000]} # Gemini handles much larger context windows!
    """
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(temperature=0)
        )
        clean_json = re.sub(r'```json\n|\n```', '', response.text).strip()
        return json.loads(clean_json)
        
    except Exception as e:
        print(f"Extraction error: {e}")
        return {}