from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_predict():
    payload = {
        "tenure_months": 12,
        "support_tickets": 2,
        "monthly_spend_inr": 500,
        "last_login_days": 10
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
