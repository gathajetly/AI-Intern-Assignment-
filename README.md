# ⚖️ LegalRag Document Processing Assistant — Intelligent Legal Document Processing & Draft Generation System

LegalRag Document Processing Assistant is an end-to-end AI-powered legal document intelligence platform designed to process noisy legal files, retrieve grounded evidence, and generate structured legal drafts using Retrieval-Augmented Generation (RAG).

The system combines OCR, semantic retrieval, vector databases, and Large Language Models (LLMs) to assist with legal document analysis and drafting workflows.

---

# 🚀 Features

- 📄 Upload legal documents (`.pdf`, `.txt`)
- 🔍 OCR + text extraction for scanned/noisy documents
- 🧠 Semantic chunking and vector embeddings
- 📚 ChromaDB-based vector retrieval
- ⚡ FastAPI backend APIs
- 🎨 Streamlit interactive frontend
- 🤖 AI-powered grounded draft generation
- 📝 Multiple legal draft types
- 🐳 Dockerized deployment support

---

# 🏗️ Project Architecture

```text
                    ┌────────────────────┐
                    │   Streamlit UI     │
                    │  (Frontend Layer)  │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │     FastAPI API    │
                    │   (Backend Layer)  │
                    └─────────┬──────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
┌──────────────┐     ┌────────────────┐    ┌────────────────┐
│ OCR Pipeline │     │ Embedding Model│    │ Draft Generator│
│ PyMuPDF/OCR  │     │ SentenceTransf │    │ Gemini/OpenAI  │
└──────┬───────┘     └────────┬───────┘    └────────┬───────┘
       │                      │                     │
       ▼                      ▼                     ▼
               ┌────────────────────────────┐
               │      Chroma Vector DB      │
               │  Semantic Evidence Search  │
               └────────────────────────────┘
```

---

# 🧠 Tech Stack

## Backend
- FastAPI
- Python
- ChromaDB
- SQLAlchemy
- Sentence Transformers
- PyMuPDF
- Pydantic

## Frontend
- Streamlit

## AI / NLP
- Gemini API / OpenAI API
- Retrieval-Augmented Generation (RAG)
- Semantic Similarity Search

## Deployment
- Docker
- Docker Compose

---

# 📂 Project Structure

```text
ai-doc-processing/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── retrieval/
│   │   ├── generation/
│   │   ├── document_processing/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── frontend/
│   └── app.py
│
└── README.md
```

---

# ⚙️ Setup Instructions (Local Development)

## 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd ai-doc-processing
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
OPENAI_API_KEY=your_openai_key
```

---

# ▶️ Running the Project

## Start Backend

```bash
cd backend
uvicorn app.main:app --reload
```

Backend runs on:

```text
http://localhost:8000
```

Swagger Docs:

```text
http://localhost:8000/docs
```

---

## Start Frontend

Open another terminal:

```bash
cd frontend
streamlit run app.py
```

Frontend runs on:

```text
http://localhost:8501
```

---

# 🐳 Docker Setup

## Build Containers

```bash
docker compose build
```

---

## Run Containers

```bash
docker compose up
```

---

# 📌 API Workflow

## Step 1 — Upload Document

Endpoint:

```http
POST /api/v1/upload/
```

Uploads legal files for processing.

---

## Step 2 — OCR & Extraction

Endpoint:

```http
POST /api/v1/extract/
```

Extracts structured text from noisy/scanned files.

---

## Step 3 — Retrieval

Endpoint:

```http
POST /api/v1/retrieve/
```

Retrieves semantically relevant evidence chunks.

---

## Step 4 — Draft Generation

Endpoint:

```http
POST /api/v1/draft/
```

Generates grounded legal summaries/drafts using retrieved evidence.

---

# 📥 Sample Input

## Uploaded Legal Text

```text
The tenant failed to provide the required 30-day notice before vacating the premises. The lease agreement signed in 2022 explicitly required written notice prior to termination.
```

---

# 📤 Sample Retrieval Output

```json
[
  {
    "chunk_id": "chunk_01",
    "text_segment": "The tenant failed to provide the required 30-day notice before vacating.",
    "relevance_score": 0.89
  }
]
```

---

# 📤 Sample Draft Output

```text
Case Fact Summary:

The tenant vacated the premises without complying with the contractual requirement of providing a 30-day written notice. The lease agreement executed in 2022 explicitly mandated prior written notice before termination of tenancy obligations.
```

---

# 🧪 Evaluation Approach

The system was evaluated on:

- OCR extraction quality
- Semantic retrieval relevance
- Grounded draft generation
- End-to-end response latency

---

# 📊 Evaluation Metrics

| Component | Evaluation Method |
|---|---|
| OCR Accuracy | Manual inspection |
| Retrieval Quality | Semantic relevance score |
| Draft Grounding | Evidence consistency |
| API Latency | Response timing |

---

# 📈 Results

- Successfully processed noisy `.pdf` and `.txt` legal files
- Accurate semantic retrieval using vector similarity
- Grounded draft generation reduced hallucinations
- Modular pipeline enabled scalable document processing

---


# 🔄 Tradeoffs

| Decision | Tradeoff |
|---|---|
| Streamlit frontend | Faster prototyping but limited scalability |
| ChromaDB local storage | Easy setup but less production-grade |
| RAG pipeline | Better grounding but slightly higher latency |
| OCR fallback | Improved extraction but slower processing |

---
# 📊 Evaluation Approach and Results

The system was evaluated across multiple stages of the legal document processing pipeline to measure the effectiveness of:
- OCR extraction
- semantic retrieval
- grounded draft generation
- downstream usability of outputs

The evaluation focused not only on technical correctness, but also on whether the extracted information was practically usable for legal drafting workflows.

---

# 🧪 Evaluation Methodology

The evaluation process was divided into four major components:

| Component | Objective |
|---|---|
| Document Processing | Evaluate handling of noisy/scanned legal files |
| OCR & Extraction | Measure quality of extracted text |
| Retrieval Quality | Evaluate semantic relevance of retrieved evidence |
| Draft Generation | Assess factual grounding and usefulness of generated drafts |

---

# 1️⃣ Document Processing Evaluation

The system was tested on:
- scanned PDFs
- noisy text files
- partially structured legal documents
- lease agreements
- notices and contracts

## Evaluation Criteria

- Ability to process low-quality inputs
- OCR fallback reliability
- extraction completeness
- downstream usability of extracted text

## Result

✅ Successfully handled messy and semi-structured legal documents with minimal manual preprocessing.

---

# 2️⃣ OCR & Text Extraction Evaluation

OCR quality was evaluated through manual inspection of extracted outputs.

## Metrics Considered

- readability of extracted text
- preservation of legal clauses
- sentence completeness
- reduction of extraction noise

## Observations

- PyMuPDF performed well on digitally generated PDFs.
- OCR fallback improved extraction for scanned/image-based documents.
- Minor OCR inconsistencies were observed in heavily distorted scans.

## Result

✅ Generated sufficiently clean and usable text for downstream semantic retrieval and draft generation tasks.

---

# 3️⃣ Semantic Retrieval Evaluation

The retrieval system was evaluated based on how accurately it returned evidence relevant to the user query.

## Evaluation Method

- Queries were manually tested against uploaded legal documents.
- Retrieved chunks were inspected for semantic relevance.
- Relevance scores were compared qualitatively.

## Example Query

```text
Summarize notice violations in the lease agreement
```

## Example Retrieved Evidence

```json
[
  {
    "chunk_id": "chunk_01",
    "text_segment": "The tenant failed to provide the required 30-day notice before vacating.",
    "relevance_score": 0.89
  }
]
```

## Observations

- Semantic embeddings improved retrieval accuracy over keyword matching.
- ChromaDB efficiently returned contextually relevant evidence chunks.
- Retrieval grounding reduced hallucinated outputs during generation.

## Result

✅ High semantic relevance observed for most legal information retrieval tasks.

---

# 4️⃣ Draft Generation Evaluation

Draft quality was evaluated based on:
- factual grounding
- coherence
- legal phrasing quality
- consistency with retrieved evidence

## Evaluation Method

Generated drafts were manually compared against:
- source documents
- retrieved evidence chunks
- expected legal summaries

## Example Generated Draft

```text
The tenant vacated the premises without complying with the contractual requirement of providing a 30-day written notice. The lease agreement explicitly mandated prior written notice before termination.
```

## Observations

- Grounded retrieval significantly reduced unsupported legal statements.
- Drafts maintained coherence and contextual relevance.
- RAG-based prompting improved factual consistency.

## Result

✅ Generated drafts were contextually grounded and usable for legal summarization workflows.

---

# 📈 Overall Results Summary

| Evaluation Area | Result |
|---|---|
| Handling Messy Inputs | Successful |
| OCR Extraction Quality | Good |
| Semantic Retrieval Relevance | High |
| Draft Grounding | Strong |
| Downstream Usability | Effective |

---
