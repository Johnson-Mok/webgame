"""
Orchestrates the quiz by initializing the session, updating the score, and starting the quiz.
"""

import streamlit as st

from ui import (
    display_choices,
    display_final_score,
    display_question,
    display_score_percentage,
    initialize_session_state,
)


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
    initialize_session_state()
    quiz = st.session_state.quiz

    st.title("Quiz")
    st.divider()

    quiz.get_score_percentage()
    display_score_percentage()

    if not quiz.is_quiz_complete():
        current_question = quiz.questions[quiz.current_question]
        display_question(current_question.prompt)
        display_choices(quiz, current_question)
    else:
        display_final_score()


if __name__ == "__main__":
    main()
