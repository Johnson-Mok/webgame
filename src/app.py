from questions import questions
from quiz import Quiz


def main() -> None:
    """
    Initializes a Quiz instance, loads questions from the predefined list,
    and starts the quiz.

    The function performs the following steps:
    1. Creates a new Quiz object.
    2. Loads questions into the Quiz object from a predefined list.
    3. Starts the quiz, prompting the user to answer each question and displaying
       the final score.
    """
    quiz = Quiz()
    quiz.load_questions_from_list(questions)
    quiz.start()


if __name__ == "__main__":
    main()
