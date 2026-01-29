from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.api.app import app
from app.api.ingest import router as ingest_router
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(chat_router)
app.include_router(ingest_router)

