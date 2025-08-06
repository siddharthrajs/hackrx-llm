import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def embed_texts(texts: list[str]) -> list[list[float]]:
    """
    Embeds a list of text chunks using Gemini in batches of 100.
    Returns a list of 768-dim float vectors.
    """
    max_batch_size = 100
    all_embeddings = []

    for i in range(0, len(texts), max_batch_size):
        batch = texts[i:i + max_batch_size]
        
        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=batch,   #type:ignore
        )
        for emb in response.embeddings: #type: ignore
            all_embeddings.append(emb.values)

    return all_embeddings
