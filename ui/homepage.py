import streamlit as st

def show_homepage():
    """Displays the homepage where users can select quiz settings."""
    st.markdown('<h1 class="title">⚽ Welcome to FootyFacts!</h1>', unsafe_allow_html=True)
    st.image("assets/FootyFacts.png", width=300)

    # ✅ Remove the duplicate image
    st.subheader("⚙️ Customize Your Trivia Experience")

    # ✅ Difficulty Selection
    difficulty = st.radio("🎚 Select Difficulty:", ["Easy", "Medium", "Hard"], horizontal=True)

    # ✅ Number of Questions Selection
    num_questions = st.slider("🔢 Select Number of Questions:", min_value=5, max_value=20, value=10)

    # ✅ Start Quiz Button
    if st.button("🎮 Start Trivia"):
        st.session_state["difficulty"] = difficulty
        st.session_state["num_questions"] = num_questions
        st.session_state["navigate_to_game"] = True
        st.rerun()
