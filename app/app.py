import streamlit as st

if "page_configured" not in st.session_state:
    st.set_page_config(page_title="FootyFacts - Football Trivia", layout="wide")
    st.session_state["page_configured"] = True

# Ensure `sys.path` includes project root
import sys
from pathlib import Path
base_path = Path(__file__).resolve().parent.parent
sys.path.append(str(base_path))

# Fix the incorrect function name in import
from ui.layout import setup_page_styles
from ui.homepage import show_homepage
from ui.trivia_game import show_trivia_game
# from services.game_logic import initialize_game_state, handle_answer_submission

# Apply custom styles
def main():
    """Main function to handle navigation between pages."""
    setup_page_styles()

    # ✅ Navigation Bar
    page = st.sidebar.radio("📍 Navigation", ["🏠 Home", "🎮 Play Trivia"])

    # ✅ Control Navigation
    if "navigate_to_game" not in st.session_state:
        st.session_state["navigate_to_game"] = False  # Default to homepage

    if page == "🎮 Play Trivia":
        st.session_state["navigate_to_game"] = True
    else:
        st.session_state["navigate_to_game"] = False

    # ✅ Show Appropriate Page
    if st.session_state["navigate_to_game"]:
        show_trivia_game()
    else:
        show_homepage()

if __name__ == "__main__":
    main()
