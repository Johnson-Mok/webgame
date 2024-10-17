import base64
import os
from typing import Dict, Optional


def get_image_base64(image_path: str, image_cache: Dict[str, str]) -> Optional[str]:
    """
    Returns the base64 encoded string of an image, with caching to improve performance.

    Args:
        image_path (str): The path to the image.
        image_cache (dict): A cache to store encoded images for reuse.

    Returns:
        Optional[str]: The base64 encoded string of the image, or None if the image is not found.
    """
    if image_path in image_cache:
        return image_cache[image_path]
    if os.path.exists(image_path):
        with open(image_path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode("utf-8")
            image_cache[image_path] = encoded
            return encoded
    return None
