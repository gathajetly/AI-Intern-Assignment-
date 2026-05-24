import streamlit as st
import requests


BASE_URL = "http://127.0.0.1:8000/api/v1"


st.set_page_config(page_title="LegalRag Document Processing Assistant", layout="wide")

st.title("LegalRag Document Processing Assistant")
st.write("Upload a document, process it, retrieve evidence, and generate grounded legal drafts.")


if "file_path" not in st.session_state:
    st.session_state.file_path = None

if "document_id" not in st.session_state:
    st.session_state.document_id = None

if "retrieved_evidence" not in st.session_state:
    st.session_state.retrieved_evidence = None

if "query" not in st.session_state:
    st.session_state.query = ""

# STEP 1 — UPLOADING THE DOCUMENT(.txt OR .pdf file)

st.header("Step 1: Upload Document")

uploaded_file = st.file_uploader(
    "Choose a legal file",
    type=["txt", "pdf"]
)

if uploaded_file is not None:
    if st.button("Upload File"):
        with st.spinner("Uploading file..."):
            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }
            response = requests.post(
                f"{BASE_URL}/upload/",
                files=files
            )
            if response.status_code == 200:
                data = response.json()
                st.session_state.file_path = data.get("file_path")
                if data.get("document_id"):
                    st.session_state.document_id = data.get("document_id")
                st.success("File uploaded successfully!")
                st.write("Uploaded File Path:")
                st.code(st.session_state.file_path)
            else:
                st.error(f"Upload failed:\n{response.text}")

# STEP 2 — EXTRACTION THE INFORMATION FROM THE DOCUMENT

st.divider()
st.header("Step 2: Extract Text & Structure")
if st.session_state.file_path:
    if st.button("Process Document"):
        with st.spinner("Running OCR and extraction..."):
            payload = {
                "file_path": st.session_state.file_path
            }
            response = requests.post(
                f"{BASE_URL}/extract/",
                json=payload
            )
            if response.status_code == 200:
                data = response.json()
                st.session_state.document_id = data.get(
                    "document_id",
                    "temp_doc_123"
                )
                st.success("Document processed successfully!")
                st.write("Document ID:")
                st.code(st.session_state.document_id)
                with st.expander("Extraction Details"):
                    st.json(data)
            else:
                st.error(f"Extraction failed:\n{response.text}")
else:
    st.info("Upload a document first.")

# STEP 3 — RETRIEVAL OF EVIDENCE

st.divider()
st.header("Step 3: Retrieve Evidence")
if st.session_state.document_id:
    query = st.text_input(
        "Enter your legal query",
        value="Summarize the key facts of the case."
    )
    st.session_state.query = query
    top_k = st.slider(
        "Number of evidence chunks",
        min_value=1,
        max_value=10,
        value=3
    )
    if st.button("Retrieve Evidence"):
        with st.spinner("Searching document..."):
            payload = {
                "document_id": st.session_state.document_id,
                "query": query,
                "top_k": top_k
            }
            response = requests.post(
                f"{BASE_URL}/retrieve/",
                json=payload
            )
            if response.status_code == 200:
                data = response.json()
                st.session_state.retrieved_evidence = data.get(
                    "retrieved_evidence",
                    []
                )
                st.success("Evidence retrieved successfully!")
                with st.expander("Retrieved Evidence"):
                    st.json(st.session_state.retrieved_evidence)
            else:
                st.error(f"Retrieval failed:\n{response.text}")
else:
    st.info("Process a document first.")

# STEP 4 — GENERATING DRAFT AFTER PROCESSING

st.divider()
st.header("Step 4: Generate Draft")
if st.session_state.retrieved_evidence:
    draft_type = st.selectbox(
        "Select Draft Type",
        [
            "Title Review Summary",
            "Case Fact Summary",
            "Notice-Related Summary",
            "Document Checklist",
            "Internal Memo"
        ]
    )
    if st.button("Generate Final Draft"):
        with st.spinner("Generating legal draft..."):
            payload = {
                "document_id": st.session_state.document_id,
                "draft_type": draft_type,
                "query": st.session_state.query,
                "evidence_chunks": [
    chunk["text_segment"]
    for chunk in st.session_state.retrieved_evidence
]
            }
            st.write("Generation Payload:")
            st.json(payload)
            response = requests.post(
                f"{BASE_URL}/draft/",
                json=payload
            )
            if response.status_code == 200:
                data = response.json()
                draft_text = data.get(
                    "draft",
                    str(data)
                )
                st.success("Draft generated successfully!")
                st.subheader("Generated Draft")
                st.text_area(
                    "",
                    value=draft_text,
                    height=400
                )
            else:
                st.error(f"Generation failed:\n{response.text}")
else:
    st.info("Retrieve evidence first before generating a draft.")