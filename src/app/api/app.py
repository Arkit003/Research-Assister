from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.rag.vector_store import load_vectorstore, get_retriever
from app.rag.embedding import get_hf_embedding
from app.models.cutsom_models import get_llm

@asynccontextmanager
async def lifespan(app: FastAPI):
    embeddings = get_hf_embedding()
    llm = get_llm()

    app.state.embeddings = embeddings
    app.state.llm = llm

    try:
        vectorstore = load_vectorstore(embeddings)
        retriever = get_retriever(vectorstore, k=5)

        app.state.vectorstore = vectorstore
        app.state.retriever = retriever
        app.state.ready = True

    except FileNotFoundError:
        app.state.vectorstore = None
        app.state.retriever = None
        app.state.ready = False

    yield

app = FastAPI(lifespan=lifespan)