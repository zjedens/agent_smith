import os
import argparse
import json

from dotenv import load_dotenv
from openai import OpenAI
from prompts import SYSTEM_PROMPT
from functions.call_function import available_functions


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key is None: raise Exception("Error! Unable to find API key")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    messages = [
        { "role": "system", "content": SYSTEM_PROMPT},
        { "role": "user", "content": args.user_prompt}
    ]
    response = client.chat.completions.create(
        model="openrouter/free", 
        messages=messages, 
        temperature=0,
        tools=available_functions
    )
    if response is None: raise Exception("Error! No usage reported by AI model.")

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    msg = response.choices[0].message
    if msg.tool_calls is not None:
        for tool_call in msg.tool_calls:
            func_args = json.loads(tool_call.function.arguments or "{}")
            print(f"Calling function: {tool_call.function.name}({func_args})")
    else:
        print(msg.content)


if __name__ == "__main__":
    main()
