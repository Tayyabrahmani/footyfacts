import re
from fuzzywuzzy import fuzz

def clean_text(text):
    """Removes punctuation, extra spaces, and newlines for better matching."""
    text = text.lower().strip()
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces/newlines with a single space
    text = re.sub(r'[^\w\s]', '', text)  # Remove all special characters
    return text

def is_answer_correct(user_answer, correct_answer):
    """Checks if the user answer is correct with fuzzy matching."""
    if not correct_answer:
        print("⚠️ Correct Answer is empty! Skipping validation.")
        return False

    user_answer = clean_text(user_answer)
    correct_answer = clean_text(correct_answer)

    # ✅ Use fuzzy matching for partial similarity
    return user_answer == correct_answer or fuzz.partial_ratio(user_answer, correct_answer) > 75
