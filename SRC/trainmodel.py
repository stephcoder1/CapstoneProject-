import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os

def train_model():
    # Load data
    df = pd.read_csv("data/inventory_data.csv")

    # Features & target
    X = df.drop(columns=["restocked", "product_name", "category"])
    y = df["restocked"]

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    print("\nModel Evaluation:\n")
    print(classification_report(y_test, y_pred))

    # Save model
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/inventory_model.pkl")

    print("\nModel saved!")

if __name__ == "__main__":
    train_model()