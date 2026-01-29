from fastapi import APIRouter, Request, HTTPException
from app.api.schema import ChatRequest, ChatResponse
from app.rag.chain import run_rag_chain

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/query", response_model=ChatResponse)
async def chat_query(payload: ChatRequest, request: Request):
    if not request.app.state.ready:
        raise HTTPException(
            status_code=503,
            detail="not ready. Upload PDFs first."
        )

    retriever = request.app.state.retriever
    llm = request.app.state.llm

    answer, _ = run_rag_chain(
        llm=llm,
        retriever=retriever,
        question=payload.query,
    )

    return ChatResponse(answer=answer)
