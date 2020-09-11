import requests


def test_valid_dest_field():
    url = "http://0.0.0.0:5000/api/v1/pawn/d4/e5"
    resp = requests.get(url)
    r = resp.json()
    assert resp.status_code == 200
    assert r["currentField"] == "D4"
    assert r["error"] == "Current move is not permitted."
    assert r["destField"] == "E5"
    assert r["move"] == "invalid"
    
