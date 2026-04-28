import os
import sys
from fastapi import FastAPI

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from predict import load_model, make_prediction

app = FastAPI()

# Load model once when API starts
model = load_model()

@app.get("/")
def home():
    return {"message": "Inventory ML API is running"}

@app.post("/predict")
def predict(data: dict):
    try:
        result = make_prediction(model, data)
        return {"prediction": result}

    except Exception as e:
        return {"error": str(e)}