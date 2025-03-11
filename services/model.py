import os
import torch
from dotenv import load_dotenv
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import streamlit as st

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), "..", "config", ".env")
load_dotenv(dotenv_path)

MODEL_NAME = "openchat/openchat-3.5-0106"
TOKEN = os.getenv("HUGGINGFACE_TOKEN")

if not TOKEN:
    raise ValueError("⚠️ HUGGINGFACE_TOKEN is missing! Set it in the .env file.")

device = "cuda" if torch.cuda.is_available() else "cpu"
print("✅ DEVICE LOADED:", device)

# ✅ Configure Quantization for Faster Inference
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

@st.cache_resource
def load_model():
    """Loads and caches the quantized model."""
    print("⏳ Loading Quantized Model (4-bit)...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=TOKEN)

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME, quantization_config=bnb_config, token=TOKEN
    ).to(device)
    print("✅ Model Loaded Successfully!")
    return tokenizer, model

tokenizer, model = load_model()

def generate_text(prompt, max_tokens=100):
    """Generates text from the model based on the given prompt."""
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=max_tokens)
    return tokenizer.decode(output[0], skip_special_tokens=True)
