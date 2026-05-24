# backend/app/api/routes/upload.py
import os
import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter(prefix="/upload", tags=["Document Upload"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
@router.post("/")
async def upload_document(file: UploadFile = File(...)):
    """
    Accepts messy legal-style documents and saves them for processing.
    """
    if not file.filename:
        raise HTTPException(status_code=400, detail="No filename provided.")
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {str(e)}")
    finally:
        file.file.close()
    return {
        "status": "success",
        "message": f"File '{file.filename}' uploaded successfully.",
        "file_path": file_path
    }