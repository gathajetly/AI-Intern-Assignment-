# backend/app/utils/chunking.py
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text_into_chunks(raw_text: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> list[str]:
    """
    Splits long, messy legal text into semantic chunks for vector storage.
    Uses recursive splitting to avoid breaking sentences/paragraphs halfway.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_text(raw_text)
    return chunks