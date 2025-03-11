import streamlit as st
from services.trivia import generate_trivia_qa

def setup_page_styles():
    """Configures Streamlit page settings & custom styling."""
    st.markdown("""
        <style>
            .main-title {
                text-align: center;
                font-size: 40px;
                font-weight: bold;
                background: linear-gradient(to right, #007bff, #00c6ff);
                color: white;
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 10px;
            }
            .question-box {
                background-color: #ffffff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
            }
            .sidebar-header {
                text-align: center;
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 5px;
            }
            .footer {
                text-align: center;
                font-size: 14px;
                color: #555;
                margin-top: 20px;
            }
        </style>
    """, unsafe_allow_html=True)

def show_question(question, correct_answer, handle_submission):
    """Displays a question and input field for answering."""
    st.markdown(f'<div class="question-box"><h3>📢 {question}</h3></div>', unsafe_allow_html=True)

    # ✅ Use a unique session state key per question to prevent modification issues
    question_key = f"user_answer_{st.session_state.question_index}"

    # ✅ Ensure session state is initialized BEFORE UI rendering
    if question_key not in st.session_state:
        st.session_state[question_key] = ""

    # ✅ Capture user input using a unique key per question
    user_answer = st.text_input("Your Answer:", key=question_key)

    if st.button("🚀 Submit Answer"):
        handle_submission(user_answer, correct_answer)

        # ✅ Clear input field by resetting key for next question
        del st.session_state[question_key]
        st.rerun()  # ✅ Fix: Use `st.rerun()` instead of `st.experimental_rerun()`

    # ✅ Expander hides correct answer unless clicked
    with st.expander("🔍 Show Correct Answer"):
        st.write(f"✅ **Correct Answer:** {correct_answer}")

    # ✅ Improved Progress Bar with Question Counter in Sidebar
    current_question = st.session_state.question_index + 1
    total_questions = 10
    progress = current_question / total_questions

    with st.sidebar:
        st.markdown(f'<p class="sidebar-header">📊 Question {current_question}/{total_questions}</p>', unsafe_allow_html=True)
        st.progress(progress)

def show_final_screen():
    """Displays the final score & play again button."""
    st.markdown(f'<h3 class="main-title">🎯 Quiz Finished! Final Score: {st.session_state.score}/10</h3>', unsafe_allow_html=True)

    if st.button("🔄 Play Again"):
        st.session_state.qa_pairs = generate_trivia_qa(num_questions=10)
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.quiz_completed = False
        st.rerun()  # ✅ Fix: Use `st.rerun()`

    # ✅ Footer with Social Media Links
    st.markdown("""
        <div class="footer">
            Made with ❤️ by FootyFacts | 
            <a href="https://twitter.com/FootyFacts" target="_blank">🐦 Twitter</a> |
            <a href="https://github.com/FootyFacts" target="_blank">💻 GitHub</a>
        </div>
    """, unsafe_allow_html=True)
