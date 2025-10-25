import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# Load sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index and docs
faiss_index = faiss.read_index("model/vector_index.faiss")
with open("model/docs.pkl", "rb") as f:
    documents = pickle.load(f)

def match_documents(query: str, top_k: int = 5):
    """Return top-k most similar documents using FAISS for fast search."""
    query_emb = model.encode([query]).astype("float32")
    distances, indices = faiss_index.search(query_emb, top_k)
    results = [
        {"document": documents[i], "score": round(1 - float(distances[0][idx]), 4)}
        for idx, i in enumerate(indices[0])
    ]
    return results
