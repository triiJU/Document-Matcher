from app.matcher import match_documents

def test_match_returns_results():
    query = "machine learning applications"
    results = match_documents(query)
    assert isinstance(results, list)
    assert len(results) > 0
