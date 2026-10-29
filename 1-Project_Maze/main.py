from config import get_key
from key_check import verify_key
from llm_client import ask,get_client
from agent import run_agent

def main():
   key = get_key()
   verify = verify_key(key)
   if verify is False:
      return 
   client = get_client(key)
   run_agent(client, "Have a look at https://maze.edwarddonner.com and do what it says.")

if __name__ == "__main__":
    main()
