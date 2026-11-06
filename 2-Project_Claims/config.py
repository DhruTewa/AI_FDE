from pathlib import Path
import os
from dotenv import load_dotenv


load_dotenv()

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

def get_key():
    key = os.getenv("key")
    if key is None:
        raise ValueError("OPENROUTER_API_KEY not found.")
    else:
        print("OPENROUTER_API_KEY verified")
    return key
