from fastapi import FastAPI
from app.rag.vector_store import load_vectorstore, get_retriever

def reload_vectorstore(app: FastAPI):
    embeddings = app.state.embeddings

    vectorstore = load_vectorstore(embeddings)
    retriever = get_retriever(vectorstore)

    app.state.vectorstore = vectorstore
    app.state.retriever = retriever
    app.state.ready = True
