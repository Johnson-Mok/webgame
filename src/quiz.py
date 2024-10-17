"""
Contains the core logic for managing questions, displaying them, and calculating the score.
"""

# import base64
# import os
from typing import Any, List


class Question:
    """
    Represents a single quiz question with multiple-choice answers.
    """

    def __init__(self, prompt: str, options: List[str], answer: int) -> None:
        """
        Initializes a Question instance.

        Args:
            prompt (str): The text of the question.
            options (List[str]): A list of possible answers.
            answer (int): The index (1-based) of the correct answer in the options list.
        """
        self.prompt = prompt
        self.options = options
        self.answer = answer


class Quiz:
    def __init__(self) -> None:
        self.questions: List[Question] = []
        self.score: int = 0
        self.score_percentage: int = 0
        self.current_question: int = 0

    def load_questions_from_list(self, questions_list: Any) -> None:
        """
        Loads questions from a list of dictionaries and adds them to the quiz.
        """
        for question_data in questions_list:
            question = Question(
                question_data["prompt"],
                [(opt[1], opt[0]) for opt in question_data["options"]],  # type: ignore
                question_data["answer"],
            )
            self.questions.append(question)

    def check_answer(self, selected_choice: str, correct_answer: str) -> bool:
        """Checks if the selected choice is the correct answer."""
        return selected_choice == correct_answer

    def increment_score(self) -> None:
        """Increments the quiz score."""
        self.score += 1

    def next_question(self) -> None:
        """Moves to the next question."""
        self.current_question += 1

    def is_quiz_complete(self) -> bool:
        """Checks if all questions have been answered."""
        return self.current_question >= len(self.questions)

    def get_score_percentage(self) -> None:
        """Calculates the score percentage."""
        if self.current_question == 0:
            self.score_percentage = 0
        else:
            self.score_percentage = round((self.score / self.current_question) * 100)
