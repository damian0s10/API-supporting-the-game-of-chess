import requests


def test_rook_available_fields():
    url = "http://0.0.0.0:5000/api/v1/rook/c4/"
    resp = requests.get(url)
    r = resp.json()
    assert resp.status_code == 200
    assert r["figure"] == "rook"
    assert r["error"] is None
    assert r["currentField"] == "C4"

    available_moves = [
        "A4",
        "A4",
        "D4",
        "E4",
        "F4",
        "G4",
        "H4",
        "C1",
        "C2",
        "C3",
        "C5",
        "C6",
        "C7",
        "C8",
    ]

    assert r["availableMoves"].sort() == available_moves.sort()
