from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os

# =====================================================
# FastAPI app
# =====================================================
app = FastAPI(title="Customer Churn Prediction API")

# =====================================================
# Paths
# =====================================================
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "churn_logistic_model.pkl")
SCALER_PATH = os.path.join(PROJECT_ROOT, "models", "scaler.pkl")
FEATURE_PATH = os.path.join(PROJECT_ROOT, "models", "feature_columns.pkl")

# =====================================================
# Load artifacts
# =====================================================
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
feature_columns = joblib.load(FEATURE_PATH)

# =====================================================
# RAW INPUT SCHEMA (human-friendly)
# =====================================================
class CustomerData(BaseModel):
    SeniorCitizen: int
    tenure: float
    MonthlyCharges: float
    TotalCharges: float
    gender: str
    Partner: str
    Dependents: str
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str


# =====================================================
# Risk helper
# =====================================================
def get_risk_level(prob: float) -> str:
    if prob < 0.3:
        return "Low"
    elif prob < 0.7:
        return "Medium"
    else:
        return "High"


# =====================================================
# Health endpoint
# =====================================================
@app.get("/")
def home():
    return {"message": "Churn Prediction API is running"}


# =====================================================
# Prediction endpoint
# =====================================================
@app.post("/predict")
def predict(data: CustomerData):

    # Convert to dict
    input_dict = data.dict()

    # Start with empty feature frame
    input_df = pd.DataFrame(columns=feature_columns)
    input_df.loc[0] = 0

    # Fill numeric features
    input_df.at[0, "SeniorCitizen"] = input_dict["SeniorCitizen"]
    input_df.at[0, "tenure"] = input_dict["tenure"]
    input_df.at[0, "MonthlyCharges"] = input_dict["MonthlyCharges"]
    input_df.at[0, "TotalCharges"] = input_dict["TotalCharges"]

    # One-hot encoding logic (matches your training)

    if input_dict["gender"] == "Male":
        input_df.at[0, "gender_Male"] = 1

    if input_dict["Partner"] == "Yes":
        input_df.at[0, "Partner_Yes"] = 1

    if input_dict["Dependents"] == "Yes":
        input_df.at[0, "Dependents_Yes"] = 1

    if input_dict["PhoneService"] == "Yes":
        input_df.at[0, "PhoneService_Yes"] = 1

    if input_dict["MultipleLines"] == "No phone service":
        input_df.at[0, "MultipleLines_No phone service"] = 1
    elif input_dict["MultipleLines"] == "Yes":
        input_df.at[0, "MultipleLines_Yes"] = 1

    if input_dict["InternetService"] == "Fiber optic":
        input_df.at[0, "InternetService_Fiber optic"] = 1
    elif input_dict["InternetService"] == "No":
        input_df.at[0, "InternetService_No"] = 1

    if input_dict["OnlineSecurity"] == "No internet service":
        input_df.at[0, "OnlineSecurity_No internet service"] = 1
    elif input_dict["OnlineSecurity"] == "Yes":
        input_df.at[0, "OnlineSecurity_Yes"] = 1

    # Scale
    scaled_data = scaler.transform(input_df)

    # Predict
    probability = model.predict_proba(scaled_data)[0][1]
    THRESHOLD = 0.45
    prediction = int(probability >= THRESHOLD)

    return {
        "churn_probability": round(float(probability), 4),
        "risk_level": get_risk_level(probability),
        "prediction": prediction
    }