from fastapi import FastAPI
from pathlib import Path
from app.rag.loader import processed_pdf
from app.rag.embedding import get_hf_embedding
from app.rag.vector_store import (
    build_vectorstore,
    load_vectorstore,
    add_documents,
)
from app.rag.reload import reload_vectorstore
import shutil

VECTOR_DIR = Path("vectorstore/bge_large")

def ingest_pdf(path: Path, app: FastAPI):
    shutil.rmtree(VECTOR_DIR, ignore_errors=True)
    chunks = processed_pdf(path)
    if not chunks:
        return

    embeddings = get_hf_embedding()

    try:
        vectorstore = load_vectorstore(embeddings)
        add_documents(vectorstore, chunks)
        print("Vector_store updated")
    except FileNotFoundError:
        build_vectorstore(chunks, embeddings)
        print("Vector_store created")

    reload_vectorstore(app)
    print("Vectorstore reloaded in memory")
