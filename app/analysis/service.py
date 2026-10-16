from app.analysis.image_checks import inspect_image

def analyse_image(contents: bytes) -> dict:
    image_info = inspect_image(contents)

    return {
        "status": "validated",
        "classification": "uncertain",
        "synthetic_probability": None,
        "confidence": None,
        "signals": [],
        "image": image_info,
        "message": "Image validated. Model analysis will be added next.",
    }
