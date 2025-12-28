import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types



#LOAD API
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

if api_key is None:
    raise RuntimeError(
        "GEMINI_API_KEY environment variable not found. "
        "Please set it before running this program."
    )




#PARSE MESSAGE
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
user_prompt=args.user_prompt


messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]


#RESPONSE
response = client.models.generate_content(
    model='gemini-2.5-flash', contents=messages
)



#RESPONSE METADATA
usage = response.usage_metadata


#Get response
def get_response_text():
    if args.verbose:
        print(response.text)
        print(f'User prompt: {user_prompt}')
        print("Prompt tokens:", usage.prompt_token_count)
        print("Response tokens:", usage.candidates_token_count)
    
    else:
       print(response.text)



get_response_text()