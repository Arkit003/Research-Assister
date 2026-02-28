# 📄 Research Assister

A **RAG-based PDF viewer and chatbot assistant** that lets you upload research papers and ask any question about their content — powered by Retrieval-Augmented Generation (RAG).

---

## ✨ Features

- 📂 Upload and view PDF research papers directly in the browser
- 🤖 Chat with an AI assistant that answers questions based on the document's content
- 🔍 RAG pipeline for accurate, context-aware responses grounded in the PDF
- ⚡ Fast and lightweight — built with a Python backend and a clean web frontend

---

## 🛠️ Tech Stack

| Layer    | Technology              |
|----------|-------------------------|
| Backend  | Python, Langchain      |
| Frontend | JavaScript, CSS, HTML   |
| RAG      | Vector embeddings + LLM |
| Package Manager | [uv](https://github.com/astral-sh/uv) |

---

## 📁 Project Structure

```
Research-Assister/
├── src/              # Backend source code (RAG pipeline, PDF processing, API)
├── frontend/         # Frontend UI (PDF viewer + chat interface)
├── pyproject.toml    # Project metadata and dependencies
└── uv.lock           # Locked dependency versions
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Arkit003/Research-Assister.git
   cd Research-Assister
   ```

2. **Install dependencies**

   ```bash
   uv sync
   ```

3. **Run the application**

   ```bash
   uv run main.py
   ```

4. Open your browser and navigate to `http://localhost:8000` (or the port shown in the terminal).

---

## 💬 Usage

1. Upload a research paper (PDF) using the file picker.
2. The PDF will be processed and indexed using RAG.
3. Type your question in the chat box.
4. The assistant will retrieve relevant sections from the PDF and generate an accurate answer.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📜 License

This project is open source. See the repository for license details.

---

## 👤 Author

**Arkit003** — [GitHub Profile](https://github.com/Arkit003)