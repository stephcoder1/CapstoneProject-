# 📦 Inventory Demand Forecasting & Restocking System

# Inventory Management ML System

## 📌 Overview

This project is a machine learning-based inventory management system that predicts when a product should be restocked. The goal is to simulate real-world inventory behavior and help businesses avoid running out of stock.

Since real data was not available, a synthetic dataset was generated to mimic realistic inventory patterns such as demand, stock levels, and supplier delays.

---

## 🎯 Objectives

* Generate realistic inventory data
* Train a machine learning model to predict restocking needs
* Automate the workflow using a structured pipeline
* Build a project that reflects real-world business logic

---

## 🧠 How It Works

The project follows a simple ML pipeline:

1. **Data Generation**

   * Creates synthetic inventory data with realistic relationships
   * Includes features like stock level, demand, and lead time

2. **Model Training**

   * Uses a Random Forest classifier
   * Learns patterns such as when stock is too low and needs restocking

3. **Prediction**

   * Tests the trained model on sample data
   * Outputs whether restocking is needed

---

## 📁 Project Structure

```
CapstoneProject/
│
├── data/
│   └── inventory_data.csv
│
├── src/
│   ├── data_generation.py
│   ├── train_model.py
│   └── predict.py
│
├── models/
│   └── inventory_model.pkl
│
├── main.py
├── requirements.txt
└── README.md
```

## 🧪 Example Output

```
--- Generating Dataset ---
--- Training Model ---
--- Running Sample Prediction ---
Restock Needed
```

---

## 🤖 Model Details

* Model: Random Forest Classifier
* Task: Binary Classification (Restock vs No Restock)
* Key Features:

  * Stock Level
  * Daily Demand
  * Supplier Lead Time
  * Units Sold

---

## 💡 Key Insights

* Lower stock levels increase restocking probability
* Higher demand leads to faster inventory depletion
* Lead time impacts when restocking should occur
