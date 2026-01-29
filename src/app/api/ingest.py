from fastapi import FastAPI, BackgroundTasks, UploadFile, File, HTTPException
from app.rag.loader import processed_pdf,extract_docs
from pathlib import Path
import uvicorn
from app.logging import logger

app = FastAPI()

@app.get("/")
def hello():
    return "hi"

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.post("/upload/pdf")
async def upload_pdf(
    file: UploadFile = File(...),
    background_tasks: BackgroundTasks = None
):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files allowed")

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as f:
        while chunk := await file.read(1024 * 1024):
            f.write(chunk)

    background_tasks.add_task(processed_pdf, file_path)
    docs = extract_docs(file_path)

    return {
        "filename": file.filename,
        "status": "processing",
        # "docs_content": docs[1].page_content,
        # "docs_metadata": docs[1].metadata,
        # "no_of_pages": len(docs)
    }



if __name__=="__main__":
    uvicorn.run(app="app.api.ingest:app",reload=True)