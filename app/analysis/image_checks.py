from io import BytesIO

from PIL import Image, UnidentifiedImageError

ALLOWED_FORMATS = {"PNG", "JPEG", "WEBP"}

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

    except (UnidentifiedImageError, OSError) as exc:
        raise ValueError("The file is not a valid readable image.") from exc

    if image_info["format"] not in ALLOWED_FORMATS:
        raise ValueError(f"Unsupported image format: {image_info['format']}.")
    
    return image_info
