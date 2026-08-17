import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

print("Lyra AI")
print("Type 'exit' to quit.\n")

while True:
    message = input("User: ")

    if message.lower() == "exit":
        print("Goodbye!")
        break

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=message
    )

    print("Lyra:", response.text)
    print()