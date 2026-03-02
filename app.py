import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()
churn_model = joblib.load('churn_pipeline.pkl')    
threshold = joblib.load('final_threshold.pkl')
new_threshold= 0.5

print (churn_model.feature_names_in_)
print (threshold)


@app.get("/")
def home():
    return {"Message": "Welcome to The Customer Churn Prediction Api"}

class CustomerData(BaseModel):
    contract_type: str
    payment_method: str
    tenure_months: int
    internet_service: str
    monthly_charges: float
    support_tickets_3m: int
    last_login_days: int
    promo_discount_pct: float

@app.post("/predict")
def predict_churn(data: CustomerData):
    input_dict= data.model_dump()
    input_df= pd.DataFrame([input_dict])
    prediction_proba= churn_model.predict_proba(input_df)[0][1]
    prediction= int(prediction_proba >= threshold)
    prediction2= int(prediction_proba >= new_threshold)

    if prediction == 1:
        status= "The customer is likely to churn"
    else:
        status= "The customer is not likely to churn"




    return {
        "churn_probability": prediction_proba,
        "churn_prediction with tuned threshold": status,
        "Status with untuned threshold": "The customer is likely to churn" if prediction2 == 1 else "The customer is not likely to churn"
    }
