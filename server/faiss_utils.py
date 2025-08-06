import faiss
import numpy as np

def create_faiss_index(embeddings: list[list[float]]):
    """
    Creates a FAISS index from a list of embeddings (768-d float vectors).
    Returns the index.
    """
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)  # L2 = Euclidean distance

    # Convert to NumPy array of shape (n_chunks, 768)
    vectors_np = np.array(embeddings).astype("float32")
    index.add(vectors_np)

    return index

def search_similar_chunks(query_embedding: list[float], index, chunks, k=2):
    """
    Returns top-k most relevant chunks for a given query embedding.
    """
    query_np = np.array([query_embedding]).astype("float32")
    distances, indices = index.search(query_np, k)

    results = []
    for idx in indices[0]:
        results.append(chunks[idx])

    return results