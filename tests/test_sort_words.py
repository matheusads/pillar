from fastapi.testclient import TestClient

from pillar.app import app

client = TestClient(app)


def test_sort_success():
    response = client.post("/sort", json={"words": ["batman", "robin", "coringa"], "order": "asc"})

    assert response.status_code == 200
    assert response.json() == ["batman", "coringa", "robin"]


def test_sort_without_order_key_should_sort_asc():
    response = client.post(
        "/sort",
        json={
            "words": ["batman", "robin", "coringa"],
        },
    )

    assert response.status_code == 200
    assert response.json() == ["batman", "coringa", "robin"]


def test_sort_reverse():
    response = client.post("/sort", json={"words": ["batman", "coringa", "robin"], "order": "desc"})

    assert response.status_code == 200
    assert response.json() == ["robin", "coringa", "batman"]


def test_method_error():
    response = client.get("/sort/")

    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}


def test_invalid_payload_type():
    response = client.post("/sort/", json={"words": [1, 2]})

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {"loc": ["body", "words", 0], "msg": "str type expected", "type": "type_error.str"},
            {"loc": ["body", "words", 1], "msg": "str type expected", "type": "type_error.str"},
        ],
    }


def test_payload_with_no_words():
    response = client.post("/sort/", json={"words": []})

    assert response.status_code == 200
    assert response.json() == []
