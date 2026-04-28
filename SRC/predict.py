import joblib
import pandas as pd

# Load model
def load_model():
    model = joblib.load("models/inventory_model.pkl")
    return model

# Make prediction
def make_prediction(model, data: dict):
    # Convert input into DataFrame
    df = pd.DataFrame([data])

    # Ensure correct column order (VERY IMPORTANT)
    expected_columns = [
        "price",
        "stock_level",
        "daily_demand",
        "supplier_lead_time",
        "reorder_point",
        "is_weekend",
        "units_sold"
    ]

    df = df[expected_columns]

    prediction = model.predict(df)[0]

    return "Restock Needed" if prediction == 1 else "No Restock Needed"