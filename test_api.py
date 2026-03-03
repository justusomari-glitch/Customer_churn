import joblib
import pandas as pd

MODEL_PATH = "churn_pipeline.pkl"

def make_sample():
    return pd.DataFrame([{
    "tenure_months":5,
    "payment_method":"Electronic check",
    "contract_type": "Month-to-month",
    "internet_service": "Fiber optic",
    "promo_discount_pct": 10,
    "monthly_charges": 70.5,
    "support_tickets_3m":2,
    "last_login_days": 5
    }])
    
def test_loads():
    model = joblib.load(MODEL_PATH)
    assert hasattr(model,"predict_proba")

def test_churn():
    model=joblib.load(MODEL_PATH)
    x = make_sample()
    proba= model.predict_proba(x)

    assert proba.shape == (1, 2)
    churn_prob=float(proba[0,1])
    assert 0.0 <= churn_prob <= 1.0



