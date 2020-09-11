import requests


def test_figure_doesnt_exist():
    url = "http://0.0.0.0:5000/api/v1/knigh/d4/e5"
    resp = requests.get(url)
    r = resp.json()
    assert resp.status_code == 404
    assert r["currentField"] == "D4"
    assert r["error"] == "Figure does not exist."
    assert r["figure"] == "knigh"
    assert r["availableMoves"] == []
    
