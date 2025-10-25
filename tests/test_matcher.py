from app.matcher import match_documents

def test_match_returns_results():
    results = match_documents("AI in finance", top_k=3)
    assert isinstance(results, list)
    assert len(results) > 0
    assert "document" in results[0]
