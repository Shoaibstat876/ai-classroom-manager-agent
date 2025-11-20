from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AI_PROVIDER = (os.getenv("AI_PROVIDER") or "openrouter").lower()

# Decide which provider to use
if AI_PROVIDER == "openrouter":
    if not OPENROUTER_API_KEY:
        raise ValueError(
            "AI_PROVIDER is set to 'openrouter' but OPENROUTER_API_KEY is missing."
        )

    # OpenRouter OpenAI-compatible endpoint
    client = OpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
    )

    # ✅ FREE GOOGLE MODEL ON OPENROUTER
    DEFAULT_MODEL = "google/gemma-3n-e2b-it:free"
    
    # Other free alternatives (non-Google):
    # DEFAULT_MODEL = "deepseek/deepseek-r1:free"
    # DEFAULT_MODEL = "meta-llama/llama-3.1-8b-instruct:free"

elif AI_PROVIDER == "openai":
    if not OPENAI_API_KEY:
        raise ValueError(
            "AI_PROVIDER is set to 'openai' but OPENAI_API_KEY is missing."
        )

    # Official OpenAI endpoint
    client = OpenAI(
        api_key=OPENAI_API_KEY,
        base_url="https://api.openai.com/v1",
    )

    # Default OpenAI model
    DEFAULT_MODEL = "gpt-4o-mini"

else:
    raise ValueError("AI_PROVIDER must be 'openrouter' or 'openai'.")