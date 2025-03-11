import openai
from openai import OpenAI
from config.settings import load_config

# Load configuration
config = load_config()

# Initialize OpenAI client (new API structure)
client = OpenAI(api_key=config["OPENAI_API_KEY"])

def get_trivia_answer(question: str) -> str:
    """Fetches a football trivia answer using OpenAI API (v1.0+ compatible)."""
    try:
        response = client.chat.completions.create(
            model=config["MODEL"],
            messages=[
                {"role": "system", "content": "You are a football trivia expert. Answer concisely."},
                {"role": "user", "content": question}
            ],
            max_tokens=config["MAX_TOKENS"],
            temperature=0.7
        )
        return response.choices[0].message.content
    except openai.OpenAIError as e:  # ✅ Corrected exception handling
        return f"⚠️ Error fetching response: {str(e)}"
