from io import BytesIO

from fastapi.testclient import TestClient
from PIL import Image
# Pillow is used to create test images for the tests

from app.main import app


client = TestClient(app)


def make_png_bytes() -> bytes:
    image = Image.new("RGB", (100, 80), color="blue")
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return buffer.getvalue()


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "veritas",
        "version": "0.1.0",
    }


def test_upload_valid_image():
    response = client.post(
        "/api/v1/analyses",
        files={
            "file": (
                "test.png",
                make_png_bytes(),
                "image/png",
            )
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["filename"] == "test.png"
    assert data["extension"] == ".png"
    assert data["media_type"] == "image"
    assert data["file_size_bytes"] > 0
    assert data["status"] == "validated"
    assert data["image"]["format"] == "PNG"


def test_upload_rejects_unsupported_media_type():
    response = client.post(
        "/api/v1/analyses",
        files={
            "file": (
                "notes.txt",
                b"not an image",
                "text/plain",
            )
        },
    )

    assert response.status_code == 415


def test_upload_rejects_empty_file():
    response = client.post(
        "/api/v1/analyses",
        files={
            "file": (
                "empty.png",
                b"",
                "image/png",
            )
        },
    )

    assert response.status_code == 400


def test_upload_rejects_invalid_image_contents():
    response = client.post(
        "/api/v1/analyses",
        files={
            "file": (
                "fake.png",
                b"not really a PNG",
                "image/png",
            )
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "The file is not a valid readable image."
    )
