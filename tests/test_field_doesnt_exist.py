import requests


def test_field_doesnt_exist():
    url = "http://0.0.0.0:5000/api/v1/queen/d9"
    resp = requests.get(url)
    r = resp.json()
    assert resp.status_code == 409
    assert r["currentField"] == "D9"
    assert r["error"] == "Field does not exist."
    assert r["figure"] == "queen"
    assert r["availableMoves"] == []
