import uuid

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def get_random_email():
    return f"user_{uuid.uuid4().hex[:8]}@example.com"


def test_register():
    response = client.post(
        "/register/",
        json={
            "email": get_random_email(),
            "password": "banana123",
            "name": "Bob Esponja",
        },
    )
    assert response.status_code == 201


# def test_register_duplicate_email():
#     response = client.post(
#         "/register/",
#         json={
#             "email": "teste@example.com",
#             "password": "banana123",
#             "name": "Bob Esponja",
#         },
#     )
#     assert response.status_code == 400


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
        "/login/", json={"email": "bob@example.com", "password": "banana123"}
    )

    assert response.status_code == 200


login_response = client.post(
    "/login/", json={"email": "bob@example.com", "password": "banana123"}
)

token = login_response.json()["access_token"]


def test_send_log():
    log = "Traceback (most recent call last):\n  File main.py, line 12\nZeroDivisionError: division by zero"
    response = client.post(
        "/send-log/",
        headers={"Authorization": f"Bearer {token}"},
        json={"message": log},
    )

    print(response.json())
    assert response.status_code == 404
