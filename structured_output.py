from openai import OpenAI
from dotenv import load_dotenv
from langsmith.wrappers import wrap_openai
from pydantic import BaseModel, Field
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

class City(BaseModel):
    name: str = Field(description="The name of the city")
    country: str = Field(description="The country where the city is located")
    population: int = Field(description="The population of the city")

#single user message
messages =[
    {
        "role" : "user",
        "content": "Provide details about Paris."
    }
]

 #call the chat completion endpoint
response = client.chat.completions.parse( 
    model=model,
    messages=messages,
    response_format=City
    )

city = response.choices[0].message.parsed
print("=== Basic Chat Completion ===")
print(type(city))
print(city)