import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.storage import BookStorage
import app.routes as routes


@pytest.fixture(autouse=True)
def fresh_storage(monkeypatch):
    monkeypatch.setattr(routes, "storage", BookStorage())


client = TestClient(app)

BOOK = {"title": "Dune", "author": "Frank Herbert", "year": 1965}


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_create_and_get_book():
    created = client.post("/books", json=BOOK)
    assert created.status_code == 201
    book_id = created.json()["id"]

    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200
    assert response.json() == {"id": book_id, **BOOK}


def test_list_books():
    client.post("/books", json=BOOK)
    client.post("/books", json={"title": "Emma", "author": "Jane Austen"})
    assert len(client.get("/books").json()) == 2


def test_update_book():
    book_id = client.post("/books", json=BOOK).json()["id"]
    response = client.put(f"/books/{book_id}", json={**BOOK, "year": 1966})
    assert response.status_code == 200
    assert response.json()["year"] == 1966


def test_delete_book():
    book_id = client.post("/books", json=BOOK).json()["id"]
    assert client.delete(f"/books/{book_id}").status_code == 204
    assert client.get(f"/books/{book_id}").status_code == 404


def test_not_found():
    assert client.get("/books/999").status_code == 404
    assert client.put("/books/999", json=BOOK).status_code == 404
    assert client.delete("/books/999").status_code == 404


def test_validation_error():
    response = client.post("/books", json={"title": "", "author": "X"})
    assert response.status_code == 422
