import chromadb
from chromadb.config import Settings
from app.core.config import settings
chroma_client = chromadb.PersistentClient(
    path=settings.chroma_db_dir,
    settings=Settings(anonymized_telemetry=False)
)

document_collection = chroma_client.get_or_create_collection(
    name="ambitio_legal_docs",
    metadata={"hnsw:space": "cosine"} 
)

def add_to_vector_store(chunks: list[str], metadatas: list[dict], ids: list[str]):
    """
    Adds text chunks and their metadata to the ChromaDB collection.
    """
    document_collection.add(
        documents=chunks,
        metadatas=metadatas,
        ids=ids
    )

def query_vector_store(query: str, document_id: str, top_k: int = 3) -> dict:
    """
    Queries the vector store for a specific document to ensure grounding.
    """
    results = document_collection.query(
        query_texts=[query],
        n_results=top_k,
        where={"document_id": document_id} 
    )
    return results