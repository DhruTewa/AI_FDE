from openai import OpenAI

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "openrouter/free"

def get_client(key: str) -> OpenAI:
    return OpenAI(api_key=key, base_url=OPENROUTER_BASE_URL, timeout=120, max_retries=5)

def ask(key:str,prompt:str) ->str:

    openrouter = get_client(key)
    messages = [{"role": "user", "content": prompt}]
    try:
        response = openrouter.chat.completions.create(model=MODEL, messages=messages)
        print(f"Answered by {response.model}")
    except Exception as error:
        print(f"Chat request failed:{error}")
        return ""
    return response.choices[0].message.content

    