import requests


def test_pawn_available_fields():
    url = "http://0.0.0.0:5000/api/v1/pawn/b2/"
    resp = requests.get(url)
    r = resp.json()
    assert resp.status_code == 200
    assert r["figure"] == "pawn"
    assert r["error"] is None
    assert r["currentField"] == "B2"

    available_moves = ["B3", "B4"]

    assert r["availableMoves"].sort() == available_moves.sort()
