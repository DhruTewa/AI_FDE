import requests

def verify_key(key:str) -> bool:
    try:
        response =  requests.get("https://openrouter.ai/api/v1/key", headers={"Authorization": f"Bearer {key}"},timeout =30)
        result = response.json()
    except(requests.RequestException,ValueError) as error:
        print(f"Could not reach OpenRouter:{error}")
        return False
    
    if response.ok:
        key_info = result["data"]
        print(f"Success! OpenRouter accepted your key {key_info['label']}")
    else:
        print(f"OpenRouter did not accept this key: {result['error']['message']} (error {response.status_code})")
        
    return response.ok