from openai import OpenAI
from dotenv import load_dotenv
from langsmith.wrappers import wrap_openai
import os


load_dotenv()

 # read in env variables
api_key = os.getenv("GEMINI_API_KEY")
api_base = os.getenv("GEMINI_API_BASE")
model = os.getenv("GEMINI_API_MODEL")

# Create client for Gemini API
client = wrap_openai(OpenAI(
    api_key=api_key, base_url=api_base
    ))



# define the tools
tools =[
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the weather in a given location",
            "parameters": {
                "type": "object",
                "properties":{
                    "location": {
                        "type" : "string",
                        "description": "The city and state, e.g. Chicago, IL"
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["location"],
            }
        }
    }
]

#single user message
messages =[
    {
        "role" : "user",
        "content": "What's the weather like in Chicago today?"
    }
]

 #call the chat completion endpoint
response = client.chat.completions.create( 
    model=model,
    messages=messages,
    tools= tools
    )

print("=== Basic Chat Completion ===")
print(response)