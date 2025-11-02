import os
from dotenv import load_dotenv
from openai import OpenAI
from langsmith import traceable
from langsmith.wrappers import wrap_openai


load_dotenv()

 # read in env variables
api_key = os.getenv("GEMINI_API_KEY")
api_base = os.getenv("GEMINI_API_BASE")
model = os.getenv("GEMINI_API_MODEL")

# Create client for Gemini API
client = wrap_openai(OpenAI(api_key=api_key, base_url=api_base))

#add  multi language
@traceable(name ="multi_turn_conversation")
def multi_turn_conversation():
    "Demonstrate multi-turn conversation with context preservation"
    conversation_history = [
        {
            "role": "system",
            "content": "You are a helpful programming tutor. Provide clear explanations and build upon previous topics in the conversation."
        }
    ]

# now add the first user message to the history
    conversation_history.append(
    {
        "role": "user",
        "content": "What is a Python list?"
    })


# call the chat completion endpoint
    response = client.chat.completions.create( 
        model=model,
        messages=conversation_history,
        temperature=0.1
        )

    answer = response.choices[0].message.content
    conversation_history.append({
        "role": "assistant",
        "content":answer
    })

    conversation_history.append({
        "role": "user",
        "content":"How do i add an item to a list?"
    })

    response = client.chat.completions.create( 
        model=model,
        messages=conversation_history,
        temperature=0.1
        )

    # now add the assistant's response to the history
    assistant_response = response.choices[0].message.content
    conversation_history.append({
    "role": "assistant",
    "content": assistant_response
    })

# ask another follow up question
    conversation_history.append({
        "role": "user",
        "content": "What's the difference between append() and extend()?"
    })


    response = client.chat.completions.create( 
        model=model,
        messages=conversation_history,
        temperature=0.1
        )
    
    return conversation_history

    print("=== Basic Chat Completion ===")
    print(conversation_history)

response = multi_turn_conversation()