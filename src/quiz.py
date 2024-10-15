import base64
import os
from typing import Any, Dict, List

import streamlit as st


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
        """
        Initializes a Quiz instance with an empty list of questions and a score of 0.
        """
        self.questions: List[Question] = []
        self.score: int = 0
        self.image_cache: Dict[str, str] = {}

    def load_questions_from_list(self, questions_list: Any) -> None:
        """
        Loads questions from a list of dictionaries and adds them to the quiz.

        Args:
            questions_list (List[Dict[str, any]]): A list of dictionaries, each containing
            question data with keys "prompt", "options", and "answer".
        """
        for question_data in questions_list:
            question = Question(
                question_data["prompt"],
                [(opt[1], opt[0]) for opt in question_data["options"]],  # type: ignore
                question_data["answer"],
            )
            self.questions.append(question)

    def display_question(self, question: str) -> None:
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

    def get_image_base64(self, image_path: str) -> str:
        """
        Returns the base64 encoded string of an image, with caching to improve performance.

        Args:
            image_path (str): The path to the image.

        Returns:
            str: The base64 encoded string of the image.
        """
        if image_path in self.image_cache:
            return self.image_cache[image_path]
        if os.path.exists(image_path):
            with open(image_path, "rb") as image_file:
                encoded = base64.b64encode(image_file.read()).decode()
                self.image_cache[image_path] = encoded
                return encoded
        return ""

    def display_choice(
        self, image_path: str, choice: str, answer: str, choice_index: int
    ) -> None:
        image_base64 = self.get_image_base64(image_path)
        if image_base64:
            if st.button(choice):
                if choice == answer:
                    st.success(f"Correct! The answer is {choice}.")
                    st.session_state.score += 1
                else:
                    st.error(f"Incorrect. The correct answer is {answer}.")
                st.session_state.current_question += 1

            st.markdown(
                f"""
                <div style="text-align: center; margin-bottom: 20px;">
                    <img src="data:image/jpeg;base64,{image_base64}" alt="{choice}" width="500" height="300" style="border: 1px solid #ddd; border-radius: 4px; padding: 5px;">
                </div>
                """,
                unsafe_allow_html=True,
            )

    def start(self) -> None:
        """
        Starts the quiz, prompts the user to answer each question, and displays the final score.
        """
        if st.session_state.current_question < len(self.questions):
            current_q = self.questions[st.session_state.current_question]
            self.display_question(current_q.prompt)

            # Display choices in a 2x2 grid
            cols = st.columns(2)
            for idx, (choice, image_path) in enumerate(current_q.options):
                with cols[idx % 2]:
                    self.display_choice(image_path, choice, current_q.answer, idx)

            # Add the "Next Question" button at the bottom right
            col1, col2 = st.columns([8, 2])
            with col2:
                if st.button("Next Question", key="next_question"):
                    st.rerun()
        else:
            st.write(
                f"Quiz completed! Your score is {st.session_state.score} out of {len(self.questions)}"
            )
            if st.button("Restart"):
                st.session_state.current_question = 0
                st.session_state.score = 0
                st.rerun()
