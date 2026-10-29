from io import BytesIO

import pytest

from fastapi.testclient import TestClient
from PIL import Image
# Pillow is used to create test images for the tests

from app.main import app
from app.main import MAX_FILE_SIZE

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

@pytest.mark.parametrize(
    "image_format, content_type, extension",
    [
        ("PNG", "image/png", ".png"),
        ("JPEG", "image/jpeg", ".jpg"),
        ("WEBP", "image/webp", ".webp"),
    ],
)
def test_upload_valid_image(image_format, content_type, extension):
    # Create a test image with the specified format
    image = Image.new("RGB", (100, 80), color="blue")
    buffer = BytesIO()
    image.save(buffer, format=image_format)
    filename = f"test{extension}"

    response = client.post(
        "/api/v1/analyses",
        files={
            "file": (
                filename,
                buffer.getvalue(),
                content_type,
            )
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["filename"] == filename
    assert data["extension"] == extension
    assert data["media_type"] == "image"
    assert data["file_size_bytes"] > 0
    assert data["status"] == "validated"
    assert data["image"]["format"] == image_format


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

def test_upload_rejects_disguised_image_format():
    image = Image.new("RGB", (100, 80), color="green")
    buffer = BytesIO()
    image.save(buffer, format="GIF")  # Save as GIF

    response = client.post(
        "/api/v1/analyses",
        files={
            "file": (
                "disguised.png",
                buffer.getvalue(),
                "image/png",  # Disguised as PNG
            )
        },
    )

    assert response.status_code == 400
    assert "Unsupported image format" in response.json()["detail"]

def test_upload_rejects_large_file():
    # Create a large image that exceeds the MAX_FILE_SIZE
    contents = b"x" * (MAX_FILE_SIZE + 1)

    response = client.post(
        "/api/v1/analyses",
        files={
            "file": (
                "large.png",
                contents,
                "image/png",
            )
        },
    )

    assert response.status_code == 413
    assert response.json()["detail"] == (
        "File is too large. Maximum size is 10 MB."
    )