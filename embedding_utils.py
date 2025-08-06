import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client()

def embed_texts(texts: list[str]) -> list[list[float]]:
    """
    Embeds a list of text chunks using Gemini's embedding model.
    Returns a list of 768-dimensional float vectors.
    """
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=texts,
    )

    return [embedding.values for embedding in response.embeddings]
