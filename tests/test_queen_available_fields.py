import requests


def test_knight_available_fields():
    url = "http://0.0.0.0:5000/api/v1/queen/h8/"
    resp = requests.get(url)
    r = resp.json()
    assert resp.status_code == 200
    assert r["figure"] == "queen"
    assert r["error"] is None
    assert r["currentField"] == "H8"

    available_moves = [
        "A8",
        "B8",
        "C8",
        "D8",
        "E8",
        "F8",
        "G8",
        "H1",
        "H2",
        "H3",
        "H4",
        "H5",
        "H6",
        "H7",
        "G7",
        "F6",
        "E5",
        "D4",
        "C3",
        "B2",
        "A1",
    ]

    assert r["availableMoves"].sort() == available_moves.sort()
