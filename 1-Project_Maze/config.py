# This file will return the key 
import os
from dotenv import load_dotenv

load_dotenv()

def get_key():
    key = os.getenv("key")
    if key is None:
        raise ValueError("OPENROUTER_API_KEY not found.")
    else:
        print("OPENROUTER_API_KEY verified")
    return key
