from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class CustomerData(BaseModel):
    tenure_months: int
    support_tickets: int
    monthly_spend_inr: float
    last_login_days: int

@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API"}

@app.post("/predict")
def predict(data: CustomerData):
    probability = round(random.uniform(0, 1), 2)

    return {
        "churn_probability": probability,
        "prediction": "Churn" if probability > 0.5 else "Retain"
    }
