from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.post("/api/v1/ocr/")
    assert response.status_code == 200
    assert response.text == "こんにちは、ORC"
