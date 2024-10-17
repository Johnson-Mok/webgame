import base64
from typing import Dict
from unittest.mock import mock_open, patch

import pytest

from src.utils import get_image_base64


def test_get_image_base64_with_cache() -> None:
    """Test if get_image_base64 returns a cached value if the image was already loaded."""
    image_cache = {"Cheetah.jpg": "fake_base64_encoded_string"}
    result = get_image_base64("Cheetah.jpg", image_cache)
    assert result == "fake_base64_encoded_string"


def test_get_image_base64_file_not_found(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test if get_image_base64 returns None if the image file is not found."""
    image_cache: Dict[str, str] = {}
    # Mock os.path.exists to simulate the file not existing
    with patch("os.path.exists", return_value=False):
        result = get_image_base64("non_existent.jpg", image_cache)
        assert result is None
        assert "non_existent.jpg" not in image_cache


def test_get_image_base64_file_found() -> None:
    """Test if get_image_base64 reads a file from the disk and adds it to the cache."""
    image_cache: Dict[str, str] = {}
    fake_file_data = b"fake_image_data"

    # Mock os.path.exists to simulate the file existing and mock open to simulate file read
    with patch("os.path.exists", return_value=True), patch(
        "builtins.open", mock_open(read_data=fake_file_data)
    ):
        result = get_image_base64("valid_image.jpg", image_cache)

    # Check if the result matches the base64-encoded fake file data
    assert result == base64.b64encode(fake_file_data).decode("utf-8")
    # Ensure that the image is cached
    assert "valid_image.jpg" in image_cache
    assert image_cache["valid_image.jpg"] == result


def test_get_image_base64_invalid_path() -> None:
    """Test if get_image_base64 handles invalid image paths gracefully."""
    image_cache: Dict[str, str] = {}
    result_empty = get_image_base64("", image_cache)

    assert result_empty is None
