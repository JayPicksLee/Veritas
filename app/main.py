from fastapi import FastAPI, File, UploadFile

app = FastAPI(title="Veritas API")


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "veritas"}


@app.post("/analyse")
async def analyse_image(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "status": "received",
        "message": "Authenticity analysis will be added next.",
    }
