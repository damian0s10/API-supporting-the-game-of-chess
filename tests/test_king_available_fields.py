import requests


def test_knight_available_fields():
    url = "http://0.0.0.0:5000/api/v1/king/a5/"
    resp = requests.get(url)
    r = resp.json()
    assert resp.status_code == 200
    assert r["figure"] == "king"
    assert r["error"] is None
    assert r["currentField"] == "A5"

    available_moves = ["A4", "A6", "B4", "B5", "B6"]

    assert r["availableMoves"].sort() == available_moves.sort()
