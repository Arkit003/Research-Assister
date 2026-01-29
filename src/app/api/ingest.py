from fastapi import APIRouter, BackgroundTasks, UploadFile, File, HTTPException, Request
from app.rag.ingest import ingest_pdf
from pathlib import Path

router = APIRouter(prefix="/upload", tags=["ingest"])

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@router.post("/pdf")
async def upload_pdf(
    file: UploadFile = File(...),
    background_tasks: BackgroundTasks = None,
    request: Request = None,
):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files allowed")

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as f:
        while chunk := await file.read(1024 * 1024):
            f.write(chunk)

    background_tasks.add_task(ingest_pdf, file_path, request.app)

    return {
        "filename": file.filename,
        "status": "processing"
    }
