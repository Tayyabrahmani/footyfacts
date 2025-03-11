import streamlit as st
from services.trivia import generate_trivia_qa
from ui.layout import show_question, show_final_screen

def show_trivia_game():
    """Handles trivia game display and logic."""
    if "navigate_to_game" in st.session_state:
        del st.session_state["navigate_to_game"]

    # ✅ Show the image **only** on the game page
    st.image("assets/FootyFacts.png", width=250)
    st.markdown('<h1 class="title">🎮 Football Trivia Game</h1>', unsafe_allow_html=True)

    # ✅ Retrieve User Preferences
    difficulty = st.session_state.get("difficulty", "Medium")
    num_questions = st.session_state.get("num_questions", 10)

    # ✅ Load New Questions If Not Loaded
    if "qa_pairs" not in st.session_state:
        st.session_state.qa_pairs = generate_trivia_qa(num_questions=num_questions)
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.quiz_completed = False

    if not st.session_state.quiz_completed:
        show_question(
            st.session_state.qa_pairs[st.session_state.question_index]["question"],
            st.session_state.qa_pairs[st.session_state.question_index]["answer"]
        )
    else:
        show_final_screen()

    # ✅ Add "Back to Homepage" Button
    if st.button("🏠 Back to Homepage"):
        st.session_state["navigate_to_game"] = False  # ✅ Go back to homepage
        st.rerun()
