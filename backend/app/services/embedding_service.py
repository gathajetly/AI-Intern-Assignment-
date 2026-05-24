# backend/app/services/embedding_service.py
import chromadb
from app.core.config import settings
chroma_client = chromadb.PersistentClient(path=settings.chroma_db_dir)
collection = chroma_client.get_or_create_collection(name="legal_documents")

def chunk_and_store(document_id: str, raw_text: str, chunk_size: int = 500):
    """
    Splits text into chunks and stores them in the vector database.
    """
    words = raw_text.split()
    chunks = [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    ids = [f"{document_id}_chunk_{i}" for i in range(len(chunks))]
    metadatas = [{"document_id": document_id, "chunk_index": i} for i in range(len(chunks))]
    collection.add(
        documents=chunks,
        metadatas=metadatas,
        ids=ids
    )
    return len(chunks)