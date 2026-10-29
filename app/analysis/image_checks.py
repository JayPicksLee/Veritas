from io import BytesIO

from PIL import Image, UnidentifiedImageError

ALLOWED_FORMATS = {"PNG", "JPEG", "WEBP"}
MAX_PIXELS = 50_000_000  # 50 million pixels, e.g., 10,000 x 5,000

def inspect_image(contents: bytes) -> dict:
    try:
        with Image.open(BytesIO(contents)) as image:
            image.verify()

        with Image.open(BytesIO(contents)) as image:
            image_info = {
                "format": image.format,
                "width": image.width,
                "height": image.height,
                "mode": image.mode,
            }
    except Image.DecompressionBombError as exc:
        raise ValueError("Image dimensions are too large to process.") from exc

    except (UnidentifiedImageError, OSError) as exc:
        raise ValueError("The file is not a valid readable image.") from exc

    if image_info["format"] not in ALLOWED_FORMATS:
        raise ValueError(f"Unsupported image format: {image_info['format']}.")

    width = image_info["width"]
    height = image_info["height"]

    if width * height > MAX_PIXELS:
        raise ValueError(
            f"Image dimensions are too large: {width}x{height} pixels."
        )
    
    return image_info
