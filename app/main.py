from pathlib import Path
from uuid import uuid4

from fastapi import FastAPI, File, HTTPException, UploadFile

from app.analysis.service import analyse_image

app = FastAPI(
    title="Veritas API",
    version="0.1.0",
)

ALLOWED_IMAGE_TYPES = {
    "image/jpeg",
    "image/png",
    "image/webp",
}

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


@app.get("/health")
def health_check() -> dict:
    """Confirm that the API is running."""
    return {
        "status": "ok",
        "service": "veritas",
        "version": "0.1.0",
    }


@app.post("/api/v1/analyses")
async def analyse_uploaded_image(file: UploadFile = File(...)) -> dict:
    """Validate and analyse an uploaded image."""

    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(
            status_code=415,
            detail=(
                "Unsupported file type. "
                "Upload a JPEG, PNG, or WebP image."
            ),
        )

    contents = await file.read()

    if not contents:
        raise HTTPException(
            status_code=400,
            detail="The uploaded file is empty.",
        )

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="File is too large. Maximum size is 10 MB.",
        )

    try:
        analysis = analyse_image(contents)
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc

    return {
        "analysis_id": str(uuid4()),
        "filename": file.filename,
        "extension": Path(file.filename or "").suffix.lower(),
        "media_type": "image",
        "file_size_bytes": len(contents),
        **analysis,
    }
