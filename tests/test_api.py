from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_api_match():
    response = client.post("/match", json={"query": "AI in fintech", "top_k": 2})
    assert response.status_code == 200
    data = response.json()
    assert "matches" in data
    assert isinstance(data["matches"], list)
