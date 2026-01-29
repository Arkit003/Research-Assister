from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.rag.vector_store import load_vectorstore
from app.rag.embedding import get_hf_embedding
from app.rag.vector_store import get_retriever
from app.models.cutsom_models import get_llm

@asynccontextmanager
async def lifespan(app: FastAPI):
    embeddings = get_hf_embedding(device="cuda")
    vectorstore = load_vectorstore(embeddings)
    retriever = get_retriever(vectorstore, k=5)
    llm = get_llm()

    app.state.embeddings = embeddings
    app.state.vectorstore = vectorstore
    app.state.retriever = retriever
    app.state.llm = llm

    yield  # app runs here

app = FastAPI(lifespan=lifespan)
