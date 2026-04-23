# Inventory Management ML Project Plan

## 📌 Project Goal

Build a machine learning system that predicts when inventory should be restocked based on stock levels, demand, and supplier lead time.

---

## 🧱 Phase 1: Project Setup

**Goal:** Create a clean and organized project structure

Tasks:

* Create folders: `data/`, `src/`, `models/`
* Create core files:

  * `data_generation.py`
  * `train_model.py`
  * `predict.py`
  * `main.py`
* Set up `requirements.txt`

---

## 📊 Phase 2: Data Generation

**Goal:** Create a realistic synthetic dataset

Tasks:

* Define dataset columns (stock, demand, lead time, etc.)
* Add logical relationships:

  * Low stock → higher chance of restock
  * High demand → faster stock depletion
* Generate 500–1000 rows of data
* Save dataset to `data/inventory_data.csv`

---

## 🧠 Phase 3: Model Development

**Goal:** Train a machine learning model

Tasks:

* Load dataset using pandas
* Split data into features (X) and target (y)
* Train a Random Forest classifier
* Evaluate performance (precision, recall, F1-score)
* Save model to `models/inventory_model.pkl`

---

## 🔍 Phase 4: Prediction System

**Goal:** Test the model

Tasks:

* Load saved model
* Create sample input data
* Generate prediction (restock or not)
* Print results

---

## 🔁 Phase 5: Pipeline Integration

**Goal:** Automate the workflow

Tasks:

* Connect all scripts in `main.py`
* Ensure correct execution order:

  1. Generate data
  2. Train model
  3. Run prediction

---

## 🐳 Phase 6: Dockerization (Optional but Recommended)

**Goal:** Make the project portable

Tasks:

* Create a `Dockerfile`
* Define environment and dependencies
* Build Docker image
* Run project inside container

---

## 🚀 Phase 7: Enhancements (Stretch Goals)

**Goal:** Improve project quality and impact

* Create an API using FastAPI

---

## ✅ Final Deliverables

* Working ML pipeline
* Synthetic dataset
* Trained model file
* Clean project structure
* README documentation

---

## 📌 Success Criteria

* Model runs without errors
* Predictions are generated successfully
* Code is organized and modular
* Project is easy to run using `main.py`

---

## 💡 Summary

This project simulates a real-world inventory system and applies machine learning to predict restocking needs, demonstrating both technical and practical problem-solving skills.
