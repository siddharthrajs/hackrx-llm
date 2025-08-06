from google import genai
from prompt_utils import build_prompt

client = genai.Client()

def get_structured_answer(query: str, relevant_chunks: list[str]) -> dict:
    prompt = build_prompt(query, relevant_chunks)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    text = response.text.strip()

    # Extract the JSON from response (safely)
    try:
        import json
        json_start = text.find("{")
        json_end = text.rfind("}") + 1
        return json.loads(text[json_start:json_end])
    except Exception as e:
        print("Error parsing JSON:", e)
        return {"error": "Failed to parse Gemini response", "raw": text}

