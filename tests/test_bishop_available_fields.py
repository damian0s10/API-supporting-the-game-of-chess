import requests


def test_knight_available_fields():
    url = "http://0.0.0.0:5000/api/v1/bishop/h8/"
    resp = requests.get(url)
    r = resp.json()
    assert resp.status_code == 200
    assert r["figure"] == "bishop"
    assert r["error"] == None
    assert r["currentField"] == "H8"

    available_moves = [
        "G7",
        "F6",
        "E5",
        "D4",
        "C3",
        "B2",
        "A1"
    ]

    assert r["availableMoves"].sort() == available_moves.sort()