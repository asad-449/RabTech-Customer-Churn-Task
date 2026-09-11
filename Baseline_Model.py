# Simple Rule-Based Customer Churn Baseline

def predict_churn(last_login_days, support_tickets):
    if last_login_days > 30 and support_tickets > 3:
        return 1
    return 0

# Example
prediction = predict_churn(45, 5)
print("Predicted Churn:", prediction)
