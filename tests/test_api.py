from fastapi.testclient import TestClient
from api.index import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_info():
    response = client.get("/info")
    assert response.status_code == 200

def test_storage():
    response = client.get("/storage?path=images/naveen.jpeg")
    assert response.status_code == 200
    