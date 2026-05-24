# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import core configurations and database
from app.core.config import settings
from app.core.database import engine, Base

# Import all API routes
from app.api.routes import upload, extraction, retrieval, drafting, feedback

# Create database tables automatically on startup
# This is great for an intern assessment as it requires zero manual DB setup
Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI(
    title=settings.app_name,
    description="Backend API for processing messy legal documents, generating grounded drafts, and learning from operator edits.",
    version="1.0.0"
)

# Set up CORS (Allowing frontend to communicate with backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all the routers
app.include_router(upload.router, prefix="/api/v1")
app.include_router(extraction.router, prefix="/api/v1")
app.include_router(retrieval.router, prefix="/api/v1")
app.include_router(drafting.router, prefix="/api/v1")
app.include_router(feedback.router, prefix="/api/v1")

@app.get("/", tags=["Health Check"])
async def root():
    """
    Simple health check endpoint to verify the API is running.
    """
    return {
        "status": "online",
        "message": f"Welcome to the {settings.app_name} API.",
        "environment": settings.environment
    }