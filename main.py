import os
from dotenv import load_dotenv
from openai import OpenAI

def main():
    load_dotenv()
    
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key is None: raise Exception("Error! Unable to find API key")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    messages = [
        {
            "role": "user",
            "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
        }
    ]
    completion = client.chat.completions.create(model="openrouter/free", messages=messages)
    print(completion.choices[0].message.content)

if __name__ == "__main__":
    main()
