from openai import OpenAI
from config import OPENROUTER_BASE_URL

def get_client(key: str) -> OpenAI:
    return OpenAI(api_key=key, base_url=OPENROUTER_BASE_URL, timeout=120, max_retries=5)
