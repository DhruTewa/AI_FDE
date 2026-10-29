from llm_client import MODEL
from tools import tools,handle_tool_call

SYSTEM_PROMPT = """
You are an agent that completes tasks by using your tools, one step at a time.
Your replies are displayed as Markdown, so format them in Markdown with headings, bold text and lists.
Put any map or diagram in a code block so that it lines up. Do not use emojis.
"""

def run_agent(client,task, max_steps=25):
    """Call the model in a loop, running the tool whenever it asks, until it gives a final answer"""
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": task},
    ]
    for step in range(1, max_steps + 1):
        response = client.chat.completions.create(model=MODEL, messages=messages, tools=tools)
        message = response.choices[0].message
        print(f"Step {step} answered by {response.model}")

        text = (message.content or "").strip()
        if text:
            print(text)

        if message.tool_calls:
            messages.append(message)
            for tool_call in message.tool_calls:
                messages.append(handle_tool_call(tool_call))
        elif text:
            return
        else:
            print("The reply was empty, so we ask again")

    print("The agent ran out of steps")