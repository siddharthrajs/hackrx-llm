import os
from google import genai
from dotenv import load_dotenv
from server.file_processor import extract_text

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)



response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents="Who is Iron Man?"
)

print(response.text)