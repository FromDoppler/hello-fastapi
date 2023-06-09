from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_openapi_json():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert response.headers.get("content-type") == "application/json"


def test_get_docs():
    response = client.get("/docs")
    assert response.status_code == 200
    assert response.headers.get("content-type") == "text/html; charset=utf-8"


def test_get_redoc():
    response = client.get("/redoc")
    assert response.status_code == 200
    assert response.headers.get("content-type") == "text/html; charset=utf-8"
