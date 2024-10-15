import streamlit as st

from questions import QUESTIONS
from quiz import Quiz


def initialize_session_state() -> None:
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "quiz" not in st.session_state:
        st.session_state.quiz = Quiz()
    if "questions" not in st.session_state:
        st.session_state.questions = st.session_state.quiz.load_questions_from_list(
            QUESTIONS
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
    st.title("Quiz")
    st.divider()

    st.session_state.quiz.start()


if __name__ == "__main__":
    main()
