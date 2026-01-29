from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    query: str = Field(..., min_length=3, max_length=500)
    session_id: str | None = None


class ChatResponse(BaseModel):
    answer: str
