import pickle
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

with open("model/vector_index.pkl", "rb") as f:
    vector_data = pickle.load(f)

documents = vector_data["docs"]
embeddings = vector_data["embeddings"]

def match_documents(query, top_k=5):
    query_emb = model.encode(query, convert_to_tensor=True)
    scores = util.cos_sim(query_emb, embeddings)[0]
    top_results = scores.topk(k=top_k)
    results = [{"document": documents[idx], "score": float(scores[idx])} for idx in top_results[1]]
    return results
