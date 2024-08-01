from typing import Any, Dict, List


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

    def check_answer(self, user_answer: int) -> bool:
        """
        Checks if the provided answer is correct.

        Args:
            user_answer (int): The index (1-based) of the user's answer.

        Returns:
            bool: True if the user's answer is correct, False otherwise.
        """
        return user_answer == self.answer


class Quiz:
    def __init__(self) -> None:
        """
        Initializes a Quiz instance with an empty list of questions and a score of 0.

        Attributes:
            questions (List[Question]): A list of Question objects in the quiz.
            score (int): The current score of the quiz.
        """
        self.questions: List[Question] = []
        self.score: int = 0

    def load_questions_from_list(self, questions_list: List[Dict[str, Any]]) -> None:
        """
        Loads questions from a list of dictionaries and adds them to the quiz.

        Args:
            questions_list (List[Dict[str, any]]): A list of dictionaries, each containing
            question data with keys "prompt", "options", and "answer".
        """
        for question_data in questions_list:
            question = Question(
                question_data["prompt"],
                question_data["options"],
                question_data["answer"],
            )
            self.questions.append(question)

    def start(self) -> None:
        """
        Starts the quiz, prompts the user to answer each question, and displays the final score.
        """
        for question in self.questions:
            print(question.prompt)
            for idx, option in enumerate(question.options):
                print(f"{idx + 1}. {option}")
            user_answer = int(input("Enter the number of your answer: "))
            if question.check_answer(user_answer):
                self.score += 1
                print("Correct!\n")
            else:
                print("Wrong!\n")
        print(f"Your final score is: {self.score}/{len(self.questions)}")
