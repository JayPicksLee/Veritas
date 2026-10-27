from io import BytesIO

import pytest
from PIL import Image

from app.analysis.image_checks import inspect_image


def make_image_bytes(
    image_format: str = "PNG",
    size: tuple[int, int] = (100, 80),
) -> bytes:
    image = Image.new("RGB", size, color="red")
    buffer = BytesIO()
    image.save(buffer, format=image_format)
    return buffer.getvalue()


def test_inspect_image_returns_metadata():
    contents = make_image_bytes()

    result = inspect_image(contents)

    assert result == {
        "format": "PNG",
        "width": 100,
        "height": 80,
        "mode": "RGB",
    }


def test_inspect_image_supports_jpeg():
    contents = make_image_bytes("JPEG")

    result = inspect_image(contents)

    assert result["format"] == "JPEG"
    assert result["width"] == 100
    assert result["height"] == 80


def test_inspect_image_rejects_invalid_bytes():
    with pytest.raises(
        ValueError,
        match="not a valid readable image",
    ):
        inspect_image(b"this is not an image")

def test_inspect_image_rejects_invalid_bytes():
    with pytest.raises(
        ValueError,
        match="not a valid readable image",
    ):
        # Fake image
        inspect_image(b"this is not an image")


@pytest.mark.parametrize("image_format", ["BMP", "TIFF", "GIF"])
def test_inspect_image_rejects_unsupported_format(image_format):
    contents = make_image_bytes(image_format)

    with pytest.raises(
        ValueError,
        match="Unsupported image format",
    ):
        inspect_image(contents)