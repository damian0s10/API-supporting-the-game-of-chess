import requests


def test_valid_dest_field():
    url = "http://0.0.0.0:5000/api/v1/rook/c2/c5"
    resp = requests.get(url)
    r = resp.json()
    assert resp.status_code == 200
    assert r["currentField"] == "C2"
    assert r["error"] == None
    assert r["destField"] == "C5"
    assert r["move"] == "valid"
