import os
from dotenv import load_dotenv

# Construct the full path to the .env file
dotenv_path = os.path.join(os.path.dirname(__file__), 'config', '.env')

# Load the .env file
load_dotenv(dotenv_path)

def load_config():
    """Load application settings from environment variables."""
    config = {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        "HUGGINGFACE_TOKEN": os.getenv("HUGGINGFACE_TOKEN"),
        "MODEL": os.getenv("GPT_MODEL", "gpt-4"),
        "MAX_TOKENS": int(os.getenv("MAX_TOKENS", 500)),
    }

    if not config["HUGGINGFACE_TOKEN"]:
        raise ValueError("⚠️ HUGGING FACE API TOKEN IS MISSING! Please set HUGGINGFACE_TOKEN in the .env file.")

    return config
