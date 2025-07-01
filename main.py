import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

if len(sys.argv) < 2:
    print("Error: No Prompt provided.")
    sys.exit(1)

verbose = "--verbose" in sys.argv

#build user prompt
prompt_parts = [arg for arg in sys.argv[1:] if arg != "--verbose"]
user_prompt = " ".join(prompt_parts)

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents=messages
)

print(response.text)

if verbose:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")