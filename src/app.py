import streamlit as st

from ui import display_score_percentage, initialize_session_state


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
    display_score_percentage()

    st.session_state.quiz.start()


if __name__ == "__main__":
    main()
