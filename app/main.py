from fastapi import FastAPI
from pydantic import BaseModel
from app.matcher import match_documents

app = FastAPI(
    title="Document Matcher API",
    description="Semantic document similarity and retrieval engine using embeddings.",
    version="1.0.0"
)

class QueryRequest(BaseModel):
    query: str
    top_k: int = 5

@app.get("/")
def home():
    return {"message": "Welcome to Document Matcher API"}

@app.post("/match")
def get_matches(request: QueryRequest):
    results = match_documents(request.query, request.top_k)
    return {"query": request.query, "matches": results}
