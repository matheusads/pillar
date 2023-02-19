from pillar.app import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_vowel_count_success():
    response = client.post("/vowel_count/", json={"words": ["coringa", "batman", "robin"]})

    assert response.status_code == 200
    assert response.json() == {"batman": 2, "robin": 2, "coringa": 3}


def test_method_error():
    response = client.get("/vowel_count/")

    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}


def test_invalid_payload_type():
    response = client.post("/vowel_count/", json={"words": [1, 2]})

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {"loc": ["body", "words", 0], "msg": "str type expected", "type": "type_error.str"},
            {"loc": ["body", "words", 1], "msg": "str type expected", "type": "type_error.str"},
        ],
    }


def test_invalid_payload_format():
    response = client.post("/vowel_count/", json={"no_words": [""]})

    assert response.status_code == 422
    assert response.json() == {
        "detail": [{"loc": ["body", "words"], "msg": "field required", "type": "value_error.missing"}]
    }


def test_payload_with_no_words():
    response = client.post("/vowel_count/", json={"words": []})

    assert response.status_code == 200
    assert response.json() == {}
