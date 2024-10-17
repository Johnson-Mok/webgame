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


def display_score_percentage() -> None:
    score_percentage = (
        round((st.session_state.score / st.session_state.current_question) * 100)
        if st.session_state.current_question > 0
        else 0
    )

    # Determine the color of the score box based on the score percentage
    if score_percentage >= 80:
        box_color = "#28a745"  # Green
    elif score_percentage >= 50:
        box_color = "#ffc107"  # Yellow
    else:
        box_color = "#dc3545"  # Red

    st.sidebar.markdown(
        f"""
        <div style="background-color: {box_color}; padding: 20px; border-radius: 10px; text-align: center; color: white; font-size: 20px;">
            <strong>Score: {score_percentage}%</strong>
        </div>
        """,
        unsafe_allow_html=True,
    )
