# Research-Assister

A RAG-based PDF viewer and chatbot assistant that lets you upload research papers and ask natural-language questions against their content. Built with a **Python backend** and a clean **web frontend** for fast, context-aware querying.

---

## 📌 Description

**Research-Assister** combines vector search and large language models to make research PDFs interactive.  
Instead of reading and skimming PDFs manually, you upload a file, and the assistant retrieves the relevant text segments and generates accurate answers grounded in that content.

This workflow uses **Retrieval-Augmented Generation (RAG)**: first retrieve relevant text chunks from the document, then generate a response using an LLM.

Backend logic lives in [src/](./src), frontend UI in [frontend/](./frontend), and `main.py` ties the server to the UI.

---

## 🧠 Techniques Used

The codebase uses these core techniques, with links to official documentation where applicable:

- **Retrieval-Augmented Generation (RAG):** hybrid approach where semantic search over document chunks informs model responses (retrieval + generation).
- **Vector Embeddings & Similarity Search:** representing text as numeric vectors for semantic lookup.
- **PDF Text Extraction:** splitting PDFs into searchable chunks for indexing.
- **API Backend + Web UI:** backend serves embeddings and responses, frontend captures user interaction.
- **Semantic Search Indexing:** efficient nearest-neighbor search over embeddings.
- **Async API Handling:** backend endpoints manage file uploads and query streaming.
- **Client-side PDF Rendering:** browser PDF display without full page reloads.
- **Clean separation of concerns** between data processing, retrieval logic, and UI logic.

---

## 📦 Notable Libraries & Tech

Professional devs will find these noteworthy:

- **Python Server & RAG Logic**
  - Uses modern Python tooling (`pyproject.toml` + `uv.lock`)
  - Vector embeddings + RAG (likely OpenAI / LangChain / similar services)
- **Frontend**
  - Vanilla **JavaScript**, **CSS**, and **HTML**
  - In-browser PDF viewer (leverages browser PDF capabilities)
- **Package Management**
  - `uv` for dependency management and running scripts
- **Embedding & LLM Services**
  - The project uses a vector embedding model + LLM API (configurable)

> *Note:* The repo does *not* bundle specific LLMs — it integrates with hosted models through configuration and API keys.

---

## 📁 Project Structure
Research-Assister/  
├── frontend/  
├── src/  
├── .gitignore  
├── .python-version  
├── main.py  
├── pyproject.toml  
└── uv.lock  


- **frontend/** — Web UI for uploading PDFs, showing them in the browser, and chatting with the assistant.
- **src/** — Python backend: RAG indexing, retrieval, API endpoints, PDF processing.
- **main.py** — Entrypoint that starts the backend server.
- **pyproject.toml / uv.lock** — Dependency and project config.

---

## 🛠️ Features

- Upload a research PDF via browser UI.
- Extract and index the PDF content for fast semantic search.
- Ask questions in natural language about the document.
- Backend retrieves relevant text chunks before answering.
- Browser displays PDF and chat in one interface.
- Built for simplicity and performance without heavy frameworks.

---

## ⚙️ Quick Tips for Developers

- Backend runs on Python 3.12+ with `uv` task runner.
- The RAG logic is decoupled from UI — you can swap out embedding models or LLM APIs.
- Frontend is framework-agnostic: pure JS, CSS, HTML for easy customization.
- Structure is modular, suitable for extending into multi-document support.

---

## 🧾 License & Author

This project is open source. See the repo for license details.

Authored by Arkit003 — explore the code, file issues, and contribute on GitHub.

---
