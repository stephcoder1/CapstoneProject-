# 📦 Inventory Demand Forecasting & Restocking System

## 🧠 Project Overview

This project focuses on building a machine learning system that helps predict future product demand and recommends when and how much inventory to restock. The goal is to simulate a real-world business problem where companies need to balance having enough stock without over-ordering.

Instead of just creating a prediction model, this project goes a step further by turning predictions into actionable decisions.

---

## 🎯 Objective

The main objective of this project is to:

* Predict how many units of a product will be sold in the near future
* Account for uncertainty in predictions
* Provide restocking recommendations based on predicted demand and current inventory

---

## 📊 Dataset

A synthetic dataset was created to simulate real-world sales data. Each row represents a product's daily performance.

### Features include:

* Product and store identifiers
* Historical sales (lag features like previous day and previous week)
* Rolling averages to capture trends
* Pricing and discount information
* Promotion indicators
* Time-based features (day of week, month, weekend)
* Current stock levels

These features were chosen to reflect factors that typically influence demand in real business settings.

---

## 🤖 Model

A machine learning regression model (Random Forest) was used to predict daily product demand. The model learns patterns from historical data, including seasonality, pricing effects, and recent sales trends.

### Evaluation Metric:

* Mean Absolute Error (MAE) was used to measure how far predictions are from actual sales on average.

---

## 🔮 Uncertainty Estimation

To make predictions more realistic, a confidence range is added to each prediction. This helps account for variability in demand and allows for better decision-making.

Example:

* Predicted demand: 50 units
* Estimated range: 45–60 units

---

## 📦 Restock Recommendation System

A simple decision engine was built on top of the model to recommend restocking actions.

### Logic:

* Uses predicted demand and upper confidence bound
* Compares against current stock levels
* Outputs how many units to restock and priority level (Low, Medium, High)

This transforms the project from just a model into a basic decision-support system.

---

## 🚀 Key Takeaways

Through this project, I practiced:

* Working with structured, numerical data
* Feature engineering for time-based patterns
* Training and evaluating regression models
* Thinking beyond predictions to real-world application

---

## 💡 Summary

This project demonstrates how machine learning can be used not only to predict outcomes but also to support real business decisions like inventory management and restocking.
