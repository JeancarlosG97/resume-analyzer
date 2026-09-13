from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Resume Analyzer API"
    }

def test_analyze_demo():
    response = client.post("/analyze-demo")

    assert response.status_code == 200

    body = response.json()

    assert "score" in body
    assert "matched_skills" in body
    assert "missing_skills" in body

    assert isinstance(body["score"], (int, float))
    assert isinstance(body["matched_skills"], list)
    assert isinstance(body["missing_skills"], list)