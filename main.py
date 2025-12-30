import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from call_function import available_functions, call_function
from prompts import system_prompt



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




#Get response
def get_response_text():
    for _ in range(20):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt
            )
        )

        usage = response.usage_metadata

        if args.verbose:
            print(f"User prompt: {user_prompt}")
            print("Prompt tokens:", usage.prompt_token_count)
            print("Response tokens:", usage.candidates_token_count)

        if response.candidates:
            for c in response.candidates:
                messages.append(c.content)
        else:
            raise SystemExit(1)

        if not response.function_calls:
            print("Response:")
            print(response.text)
            return

        function_responses = []

        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")

            function_call_result = call_function(function_call)

            if not function_call_result.parts:
                raise Exception("call_function returned Content with empty .parts")

            if function_call_result.parts[0].function_response is None:
                raise Exception("Missing .function_response on parts[0]")

            if function_call_result.parts[0].function_response.response is None:
                raise Exception("Missing .response on parts[0].function_response")

            function_responses.append(function_call_result.parts[0])

            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")

        messages.append(types.Content(role="user", parts=function_responses))

    print("Error: Reached max iterations (20) without a final response.")
    raise SystemExit(1)


if __name__ == "__main__":
    get_response_text()