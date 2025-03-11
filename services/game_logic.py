import streamlit as st
import time
from services.trivia import generate_trivia_qa
from utils.text_utils import is_answer_correct

def initialize_game_state():
    """Initializes the game state if not already set."""
    if "qa_pairs" not in st.session_state:
        st.session_state.qa_pairs = generate_trivia_qa(num_questions=10)
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.quiz_completed = False

def handle_answer_submission(user_answer, correct_answer):
    """Handles the answer submission logic."""
    if user_answer.strip():
        if is_answer_correct(user_answer, correct_answer):
            st.session_state.score += 1
            with st.spinner("Checking Answer..."):
                time.sleep(1)  # ✅ Small delay for suspense
            st.success("✅ Correct! 🎉")
        else:
            with st.spinner("Checking Answer..."):
                time.sleep(1)
            st.error(f"❌ Incorrect! The correct answer is: {correct_answer}")

        # ✅ Move to next question after animation
        st.session_state.question_index += 1
        st.rerun()
    else:
        st.warning("⚠️ Please enter an answer before submitting.")
