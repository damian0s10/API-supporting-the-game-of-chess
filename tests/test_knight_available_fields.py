import requests


def test_knight_available_fields():
    url = "http://0.0.0.0:5000/api/v1/knight/a5/"
    resp = requests.get(url)
    r = resp.json()
    assert resp.status_code == 200
    assert r["figure"] == "knight"
    assert r["error"] == None
    assert r["currentField"] == "A5"

    available_moves = [
        "B7",
        "B3",
        "C4",
        "C6"
    ]

    assert r["availableMoves"].sort() == available_moves.sort()