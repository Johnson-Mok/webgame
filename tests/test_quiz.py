import pytest

from src.quiz import Quiz
from tests.mock_questions import QUESTIONS


@pytest.fixture
def sample_quiz() -> Quiz:
    """Fixture to create a Quiz instance and load questions."""
    quiz = Quiz()
    quiz.load_questions_from_list(QUESTIONS)
    return quiz


def test_load_questions(sample_quiz: Quiz) -> None:
    """Test that questions are loaded correctly into the quiz."""
    assert len(sample_quiz.questions) == len(QUESTIONS)

    loaded_prompts = [q.prompt for q in sample_quiz.questions]
    assert "What is the fastest land animal?" in loaded_prompts
    assert "Which animal has the longest lifespan?" in loaded_prompts


def test_check_answer_correct(sample_quiz: Quiz) -> None:
    """Test that check_answer returns True for the correct answer."""
    for question in sample_quiz.questions:
        # Match the question prompt to the correct answer and test
        if question.prompt == "What is the fastest land animal?":
            assert sample_quiz.check_answer("Cheetah", question.answer)
        elif question.prompt == "Which animal has the longest lifespan?":
            assert sample_quiz.check_answer("Bowhead Whale", question.answer)


def test_check_answer_incorrect(sample_quiz: Quiz) -> None:
    """Test that check_answer returns False for an incorrect answer."""
    for question in sample_quiz.questions:
        if question.prompt == "What is the fastest land animal?":
            assert not sample_quiz.check_answer("Lion", question.answer)


def test_increment_score(sample_quiz: Quiz) -> None:
    """Test that the score is incremented correctly."""
    assert sample_quiz.score == 0
    sample_quiz.increment_score()
    assert sample_quiz.score == 1


def test_next_question(sample_quiz: Quiz) -> None:
    """Test that next_question advances to the next question."""
    assert sample_quiz.current_question == 0
    sample_quiz.next_question()
    assert sample_quiz.current_question == 1


def test_is_quiz_complete(sample_quiz: Quiz) -> None:
    """Test that is_quiz_complete returns True when all questions are answered."""
    sample_quiz.current_question = len(sample_quiz.questions)
    assert sample_quiz.is_quiz_complete()


def test_is_quiz_not_complete(sample_quiz: Quiz) -> None:
    """Test that is_quiz_complete returns False when there are remaining questions."""
    assert not sample_quiz.is_quiz_complete()


def test_get_score_percentage(sample_quiz: Quiz) -> None:
    """Test that get_score_percentage correctly calculates the percentage."""
    # Simulate answering 2 questions correctly
    sample_quiz.increment_score()  # Correct answer for question 1
    sample_quiz.increment_score()  # Correct answer for question 2
    sample_quiz.current_question = 2  # Assuming 2 questions have been answered
    sample_quiz.get_score_percentage()

    assert sample_quiz.score_percentage == 100

    # Simulate 1 incorrect answer (2 out of 3 correct)
    sample_quiz.current_question = 3
    sample_quiz.get_score_percentage()

    assert sample_quiz.score_percentage == 67  # Round(2/3 * 100) = 67


def test_get_score_percentage_no_questions_answered(sample_quiz: Quiz) -> None:
    """Test that get_score_percentage returns 0 if no questions have been answered."""
    sample_quiz.get_score_percentage()
    assert sample_quiz.score_percentage == 0
