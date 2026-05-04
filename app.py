from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib
from datetime import datetime

model = joblib.load("inventory_model.pkl")
encoder = joblib.load("encoder.pkl")
scaler = joblib.load("scaler.pkl")

app = FastAPI(title="Hair Braiding Inventory Stockout Predictor")

# Columns used during training
categorical_cols = ["item_name", "style_type", "item_style"]

numeric_cols = [
    "price",
    "stock_level",
    "promotion",
    "is_weekend",
    "is_holiday",
    "appointments_per_day",
    "day_of_week",
    "month",
    "lag_sales",
    "rolling_avg_3",
    "units_per_appt",
    "stock_pressure"
]

class InventoryInput(BaseModel):
    date: str
    item_name: str
    style_type: str
    price: float
    stock_level: float
    promotion: int
    is_holiday: int
    appointments_per_day: int
    lag_sales: float
    rolling_avg_3: float


@app.get("/")
def home():
    return {"message": "Stockout prediction API is running"}


@app.post("/predict")
def predict_stockout(data: InventoryInput):
    
    input_data = data.dict()

    
    date_obj = pd.to_datetime(input_data["date"])

    
    input_data["day_of_week"] = date_obj.dayofweek
    input_data["month"] = date_obj.month
    input_data["is_weekend"] = 1 if date_obj.dayofweek >= 5 else 0

    input_data["item_style"] = (
        input_data["item_name"] + "_" + input_data["style_type"]
    )

    input_data["units_per_appt"] = (
        input_data["rolling_avg_3"] / (input_data["appointments_per_day"] + 1)
    )

    input_data["stock_pressure"] = (
        input_data["stock_level"] / (input_data["appointments_per_day"] + 1)
    )

    
    df = pd.DataFrame([input_data])

    
    X_cat = encoder.transform(df[categorical_cols])
    X_num = scaler.transform(df[numeric_cols])

    X_final = np.hstack((X_cat, X_num))

    prediction = model.predict(X_final)[0]
    probability = model.predict_proba(X_final)[0][1]

    return {
        "stockout_prediction": int(prediction),
        "stockout_probability": round(float(probability), 3),
        "message": "Stockout likely" if prediction == 1 else "Stockout not likely"
    }