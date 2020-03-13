"""Test Forex API"""


def test_forex_api_doc(client):
    response = client.get("/api/forex/doc")
    assert response.status_code == 200


def test_get_usd_rates(client):
    response = client.get("/api/forex/rates/usd", follow_redirects=True)
    assert response.status_code == 200
