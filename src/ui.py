"""
Handles the user interface components like displaying the score percentage, final score, and initializing session state.
"""

from datetime import datetime

import pytz  # type: ignore
import streamlit as st

from questions import QUESTIONS
from quiz import Question, Quiz
from utils import get_image_base64


def initialize_session_state() -> None:
    if "quiz" not in st.session_state:
        st.session_state.quiz = Quiz()
        st.session_state.quiz.load_questions_from_list(QUESTIONS)
    if "image_cache" not in st.session_state:
        st.session_state.image_cache = {}


def display_question(question: str) -> None:
    """Displays the question in a styled rectangle."""
    st.markdown(
        f"""
        <div style="
            border: 2px solid black;
            padding: 20px;
            margin-bottom: 20px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            ">
            {question}
        </div>
        """,
        unsafe_allow_html=True,
    )


def display_score_percentage() -> None:
    if st.session_state.quiz.score_percentage >= 80:
        box_color = "#28a745"  # Green
    elif st.session_state.quiz.score_percentage >= 50:
        box_color = "#ffc107"  # Yellow
    else:
        box_color = "#dc3545"  # Red

    with st.sidebar:
        st.markdown(
            f"""
            <div style="background-color: {box_color}; padding: 20px; border-radius: 10px; text-align: center; color: white; font-size: 20px;">
                <strong>Score: {st.session_state.quiz.score_percentage}%</strong>
            </div>
            """,
            unsafe_allow_html=True,
        )


def display_version() -> None:
    amsterdam_tz = pytz.timezone("Europe/Amsterdam")
    amsterdam_time = datetime.now(amsterdam_tz)
    formatted_time = amsterdam_time.strftime("%Y-%m-%d %H:%M:%S %Z")

    # Display in the sidebar with enhanced aesthetics
    with st.sidebar:
        st.markdown(
            """
            <div style="background-color:#f0f0f5; padding: 10px; border-radius: 10px; text-align: center;">
                <h4 style="color:#4B8BBE; font-size:26px;">App Version</h4>
                <p style="font-size:20px; color:#333333;">{}</p>
            </div>
            """.format(
                formatted_time
            ),
            unsafe_allow_html=True,
        )


def display_final_score() -> None:
    st.markdown(
        f"""
        <div style="text-align: center; margin-top: 50px;">
            <h1 style="font-size: 60px; color: #4CAF50;">Final Score: {st.session_state.quiz.score_percentage}%</h1>
        </div>
    """,
        unsafe_allow_html=True,
    )


def render_image(image_base64: str, choice: str) -> None:
    """
    Renders an image for a quiz choice in the UI.

    Args:
        image_base64 (str): The base64 encoded image string.
        choice (str): The label for the quiz choice.
    """
    st.markdown(
        f"""
        <div style="text-align: center; margin-bottom: 20px;">
            <img src="data:image/jpeg;base64,{image_base64}" alt="{choice}" width="500" height="300" style="border: 1px solid #ddd; border-radius: 4px; padding: 5px;">
        </div>
        """,
        unsafe_allow_html=True,
    )


def display_choice_button(quiz: "Quiz", choice: str, correct_answer: str) -> None:
    """
    Displays the button for a quiz choice and checks if the selected choice is correct.

    Args:
        quiz (Quiz): The current quiz instance.
        choice (str): The current choice to display.
        correct_answer (str): The correct answer for the current question.
    """
    if st.button(choice):
        if quiz.check_answer(choice, correct_answer):
            st.success(f"Correct! The answer is {choice}.")
            quiz.increment_score()
        else:
            st.error(f"Incorrect. The correct answer is {correct_answer}.")
        quiz.next_question()
        st.rerun()


def display_choices(quiz: "Quiz", current_question: "Question") -> None:
    """
    Displays choices for the current question in a 2x2 grid layout.

    Args:
        quiz (Quiz): The current quiz instance.
        current_question (Question): The current question being asked.
    """
    cols = st.columns(2)
    for idx, (choice, image_path) in enumerate(current_question.options):
        with cols[idx % 2]:
            image_base64 = get_image_base64(image_path, st.session_state.image_cache)
            display_choice_button(quiz, choice, current_question.answer)
            render_image(image_base64, choice)
