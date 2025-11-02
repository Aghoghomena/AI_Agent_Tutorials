import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

 # read in env variables
api_key = os.getenv("GEMINI_API_KEY")
api_base = os.getenv("GEMINI_API_BASE")
model = os.getenv("GEMINI_API_MODEL")

# Create client for Gemini API
client = OpenAI(api_key=api_key, base_url=api_base)

#single user message
messages =[
    {
        "role" : "user",
        "content": "Explain quantum computing in simple terms"
    }
]

# call the chat completion endpoint
response = client.chat.completions.create( 
    model=model,
    messages=messages,
    max_tokens=150, 
    temperature=0.5
    )

print("=== Basic Chat Completion ===")
print(f"Response: {response.choices[0].message.content}")