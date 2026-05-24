# backend/app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    app_name: str = "Ambitio Legal AI System"
    environment: str = "development"
    
    openai_api_key: str = ""
    anthropic_api_key: str = ""
    
    upload_dir: str = os.path.join(os.getcwd(), "uploads")
    chroma_db_dir: str = os.path.join(os.getcwd(), "vector_db")
    
    database_url: str = "sqlite:///./ambitio_ai.db"

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()