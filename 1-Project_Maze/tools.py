import json
import requests
from bs4 import BeautifulSoup

MAZE_URL = "https://maze.edwarddonner.com"

def read_web_page(url):
    """Read a web page in the maze and return the text on the page, without the HTML"""
    print(f"Reading web page: {url}")
    if not url.startswith(MAZE_URL):
        return f"Sorry, this tool can only read pages in the maze. Please ask for a URL that starts with {MAZE_URL}"
    response = requests.get(url, timeout=20)
    page = BeautifulSoup(response.text, "html.parser")
    return page.body.get_text(separator="\n", strip=True)

read_web_page_json = {
    "type": "function",
    "function": {
        "name": "read_web_page",
        "description": "Read a web page and return the text on the page",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "The full URL of the web page to request"},
            },
            "required": ["url"],
        },
    },
}

tools = [read_web_page_json]

def handle_tool_call(tool_call):
    """Run the tool that the model asked for and package the result as a message"""
    try:
        arguments = json.loads(tool_call.function.arguments)
        result = read_web_page(**arguments)
    except Exception as error:
        result = f"The tool call failed: {error}"
    return {"role": "tool", "tool_call_id": tool_call.id, "content": result}