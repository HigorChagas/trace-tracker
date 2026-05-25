from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_register():
    response = client.post(
        "/register/",
        json={
            "email": "gwyn@example.com",
            "password": "banana123",
            "name": "Bob Esponja",
        },
    )
    assert response.status_code == 201


def test_register_duplicate_email():
    response = client.post(
        "/register/",
        json={
            "email": "bobas@example.com",
            "password": "banana123",
            "name": "Bob Esponja",
        },
    )
    assert response.status_code == 400


def test_register_small_password():
    response = client.post(
        "/register/",
        json={
            "email": "bobas@example.com",
            "password": "ba",
            "name": "Bob Esponja",
        },
    )
    assert response.status_code == 422


def test_register_invalid_email():
    response = client.post(
        "/register/",
        json={
            "email": "bobas",
            "password": "banana123",
            "name": "Bob Esponja",
        },
    )
    assert response.status_code == 422

def test_login():
    response = client.post(
        "/login/",
        json={
            "email": "bob@example.com",
            "password": "banana123"
        }
    )

    assert response.status_code == 200