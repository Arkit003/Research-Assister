# Backend – Research-Assister

This directory contains the backend implementation that powers Research-Assister’s Retrieval-Augmented Generation (RAG) workflow.

The backend is responsible for:

- PDF ingestion and parsing  
- Text chunking and preprocessing  
- Embedding generation  
- Vector indexing and similarity search  
- RAG orchestration  
- API endpoints used by the frontend  

The design prioritizes modularity, model-agnostic integration, and clean separation of concerns.

---

## Architecture Overview

The backend follows a standard RAG pipeline:

1. **PDF Upload**
   - The API receives a PDF file from the frontend.
   - The document is passed to the parsing layer.

2. **Text Extraction & Chunking**
   - Text is extracted from the PDF.
   - The content is split into chunks suitable for embedding and LLM token limits.

3. **Embedding Generation**
   - Each chunk is converted into a dense vector representation.
   - These embeddings capture semantic meaning rather than keyword similarity.

4. **Vector Indexing**
   - Embeddings are stored in a vector index.
   - Enables fast nearest-neighbor semantic search.

5. **Query Handling**
   - A user question is embedded.
   - The system retrieves the most relevant document chunks.

6. **Generation**
   - Retrieved chunks + user query are combined into a prompt.
   - The LLM generates a grounded response.

---

## Design Principles

### 1. Modular Components

The backend separates responsibilities:

- PDF parsing
- Text preprocessing
- Embedding logic
- Retrieval logic
- Generation logic
- API layer

Each component can be swapped independently (e.g., replace embedding provider without touching retrieval).

---

### 2. Model-Agnostic Architecture

The system does not hard-code a specific LLM or embedding model.  
You can plug in:

- Hosted embedding APIs  
- Local embedding models  
- Different LLM providers  

Minimal changes are required if interfaces are respected.

---

### 3. Clean RAG Orchestration

The retrieval step ensures that:

- Only relevant chunks are passed to the model  
- Token usage remains controlled  
- Hallucination risk is reduced  

This keeps responses grounded in actual PDF content.

---

## Technologies & Tooling

### Python 3.12+

Modern Python features are leveraged for:

- Type hints
- Improved async handling
- Clean module structure

---

### Dependency Management

The backend uses:

- `pyproject.toml` for project configuration
- `uv.lock` for deterministic dependency resolution

This ensures reproducible builds and consistent environments.

---

### Vector Embeddings

The system relies on embedding models to convert text into numeric vectors for semantic similarity search.

This enables:

- Meaning-based retrieval  
- Better matching than keyword search  
- Efficient nearest-neighbor lookup  

---

### Vector Search

A vector index is used to:

- Store embeddings
- Perform similarity search
- Retrieve top-k relevant chunks for a query

The backend can be extended to use persistent vector databases if needed.

---

### API Layer

The backend exposes endpoints for:

- PDF upload
- Query submission
- Response generation

The API is designed to be consumed by the frontend in `../frontend`.

---

## Directory Structure
src/  
├── api/  
├── embeddings/  
├── generation/  
├── pdf_processing/  
├── retrieval/  
├── config.py  

---

### Directory Notes

- **api/**  
  HTTP route definitions and request handling.

- **pdf_processing/**  
  PDF parsing, text extraction, and chunking logic.

- **embeddings/**  
  Interfaces with embedding models and transforms text into vectors.

- **retrieval/**  
  Vector search and similarity lookup logic.

- **generation/**  
  RAG orchestration and prompt construction for the LLM.

- **config.py**  
  Configuration management (model settings, API keys, runtime parameters).

---

## Extensibility Notes

We could extend the backend to support:

- Multi-document indexing
- Persistent vector databases
- Streaming LLM responses
- Hybrid keyword + vector retrieval
- Local model inference
- Caching layers for embeddings

The modular structure makes these changes straightforward.

---

## Summary

The backend implements a clean, production-oriented RAG pipeline:

- Structured ingestion  
- Semantic indexing  
- Efficient retrieval  
- Grounded generation  

It is intentionally minimal and extensible, making it suitable for experimentation, scaling, or integration into larger systems.
