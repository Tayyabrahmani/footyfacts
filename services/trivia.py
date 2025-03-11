import re
import streamlit as st
from services.model import generate_text

def extract_questions_and_answers(text, num_questions=10):
    """Extracts properly formatted questions & answers from model output."""
    questions = re.findall(r"\d+\.\s(.*?)\?", text)
    answers = re.findall(r"\d+\.\s.*?\?\s*(.*)", text)

    if len(questions) < num_questions or len(answers) < num_questions:
        questions = [f"Question {i+1}: Placeholder Question" for i in range(num_questions)]
        answers = ["Placeholder Answer"] * num_questions

    return [{"question": q.strip(), "answer": a.strip()} for q, a in zip(questions, answers)]

def generate_trivia_qa(num_questions=10):
    """Generates football trivia questions and answers."""
    input_text = f"Generate {num_questions} unique football trivia questions along with their correct answers."
    full_text = generate_text(input_text, max_tokens=400)
    return extract_questions_and_answers(full_text, num_questions)
