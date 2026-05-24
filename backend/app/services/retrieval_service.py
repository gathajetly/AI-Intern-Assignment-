from app.services.embedding_service import collection
def retrieve_evidence(document_id: str, query: str, top_k: int = 3) -> list[dict]:
    """
    Surfaces the most relevant passages for a given query and document.
    """
    results = collection.query(
        query_texts=[query],
        n_results=top_k,
        where={"document_id": document_id} # Only search within this specific document
    )
    evidence_list = []
    if results['documents']:
        for i in range(len(results['documents'][0])):
            evidence_list.append({
                "chunk_id": results['ids'][0][i],
                "text": results['documents'][0][i],
                "distance": results['distances'][0][i] if 'distances' in results else 0.0
            })
    return evidence_list