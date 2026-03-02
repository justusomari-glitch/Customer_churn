import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()
churn_model = joblib.load('churn_pipeline.pkl')    
threshold = joblib.load('threshold.pkl')

print (churn_model.feature_names_in_)
print (threshold)
