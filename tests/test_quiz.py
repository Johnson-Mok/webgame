import base64
from io import BytesIO
from typing import Any

import pytest

from src.quiz import Quiz
from tests.mock_questions import QUESTIONS


def test_load_questions_from_list() -> None:
    """Test if the quiz loads questions from the list correctly."""
    quiz = Quiz()

    # Load the sample questions list
    quiz.load_questions_from_list(QUESTIONS)

    # Check if the questions were loaded
    assert len(quiz.questions) == len(QUESTIONS)
    assert quiz.questions[0].prompt == "What is the fastest land animal?"
    assert quiz.questions[0].options == [
        ("Cheetah", "Cheetah.jpg"),
        ("Lion", "Lion.jpg"),
        ("Horse", "Horse.jpg"),
        ("Greyhound", "Greyhound.jpg"),
    ]
    assert quiz.questions[0].answer == "Cheetah"

    assert quiz.questions[1].prompt == "Which animal has the longest lifespan?"
    assert quiz.questions[1].options == [
        ("Elephant", "Elephant.jpg"),
        ("Bowhead Whale", "BowheadWhale.jpg"),
        ("Dog", "Dog.jpg"),
        ("Gorilla", "Gorilla.jpg"),
    ]
    assert quiz.questions[1].answer == "Bowhead Whale"


def test_get_image_base64_with_cache() -> None:
    """Test if get_image_base64 returns a cached value if the image was already loaded."""
    quiz = Quiz()
    quiz.image_cache["Cheetah.jpg"] = "fake_base64_encoded_string"

    result = quiz.get_image_base64("Cheetah.jpg")

    assert result == "fake_base64_encoded_string"


def test_get_image_base64_without_cache(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test if get_image_base64 loads an image, encodes it to base64, and caches it."""
    quiz = Quiz()

    # Mock os.path.exists to simulate that the file exists
    monkeypatch.setattr("os.path.exists", lambda path: True)

    # Mock the open method to simulate file reading
    def mock_open(*args: Any, **kwargs: Any) -> BytesIO:
        return BytesIO(b"fake_image_data")

    monkeypatch.setattr("builtins.open", mock_open)

    result = quiz.get_image_base64("Cheetah.jpg")

    expected_encoded_image = base64.b64encode(b"fake_image_data").decode()
    assert result == expected_encoded_image
    assert quiz.image_cache["Cheetah.jpg"] == expected_encoded_image


def test_get_image_base64_file_not_found(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test if get_image_base64 returns an empty string if the image file is not found."""
    quiz = Quiz()

    # Mock os.path.exists to simulate the file not existing
    monkeypatch.setattr("os.path.exists", lambda path: False)

    result = quiz.get_image_base64("non_existent.jpg")

    assert result == ""
    assert "non_existent.jpg" not in quiz.image_cache
