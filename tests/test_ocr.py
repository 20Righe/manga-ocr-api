from fastapi.testclient import TestClient
from app.main import app
import json
from pathlib import Path

TEST_DATA_ROOT = Path(__file__).parent / "data"

client = TestClient(app)


def test_ocr_endpoint():
    expected_results = json.loads(
        (TEST_DATA_ROOT / "expected_results.json").read_text(encoding="utf-8")
    )

    for item in expected_results:
        response = client.post(
            "/api/v1/ocr/",
            files=[("file", open(TEST_DATA_ROOT / "images" / item["filename"], "rb"))],
        )
        assert response.status_code == 200
        assert response.text == item["result"]


def test_invalid_file_type():
    files = {"file": ("test.txt", b"Some text data", "text/plain")}

    response = client.post("/api/v1/ocr/", files=files)

    assert response.status_code == 400
    assert (
        response.json()["detail"]
        == "Invalid file type. Only JPEG, PNG, BMP, TIFF, and WebP are supported."
    )


def test_internal_server_error_handling():
    files = {"file": ("test.png", b"not an image", "image/png")}

    response = client.post("/api/v1/ocr/", files=files)

    assert response.status_code == 500
    assert "detail" in response.json()
