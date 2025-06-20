import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


if len(sys.argv) < 2:
        print ("Usage: python3 main.py <prompt>")
        sys.exit(1)

user_prompt = sys.argv[1]

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)


messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
#sys.argv[1]
response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=messages,
)

if '--verbose' in sys.argv:
    print(f"{response.text}\nUser prompt: {user_prompt}\nPrompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")
else:
    print(response.text)