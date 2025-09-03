from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_read_all_luminosite():
    response = client.get("/luminosites")
    assert response.status_code == 200
    assert len(response.json()) > 1
    
def test_read_luminosite():
    response = client.get("/luminosites/1")
    assert response.status_code == 200
    assert response.json() == { "id": 1, "libelle": "Plein jour" }

def test_read_luminosite_not_found():
    response = client.get("/luminosites/0")
    assert response.status_code == 404
