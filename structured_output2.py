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

# Define the data model for the math reasoning steps
class Step(BaseModel):
    explanation: str
    output: str

# Define the data model for the overall math reasoning
class MathReasoning(BaseModel):
    steps: list[Step]
    final_answer: str


#single user message
messages =[
    {
        "role" : "system",
        "content": "You are a helpful math tutor. Guide the user through the solution step by step."       
    },
    {
        "role" : "user",
        "content": "how can I solve 8x + 7 = -23"
    }
]

 #call the chat completion endpoint
response = client.chat.completions.parse( 
    model=model,
    messages=messages,
    response_format=MathReasoning
    )

solution = response.choices[0].message.parsed
print("=== Basic Chat Completion ===")
for stepnumber, step in enumerate(solution.steps, start =1):
    print(f"Step {stepnumber}: {step.explanation}")
    print(f"Output: {step.output}\n")