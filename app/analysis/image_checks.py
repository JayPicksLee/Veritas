from io import BytesIO

from PIL import Image, UnidentifiedImageError


def inspect_image(contents: bytes) -> dict:
    try:
        with Image.open(BytesIO(contents)) as image:
            image.verify()

        with Image.open(BytesIO(contents)) as image:
            return {
                "format": image.format,
                "width": image.width,
                "height": image.height,
                "mode": image.mode,
            }

    except (UnidentifiedImageError, OSError) as exc:
        raise ValueError("The file is not a valid readable image.") from exc
