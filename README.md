#  Inventory Stockout Prediction System

##  Project Overview

This project focuses on predicting inventory stockouts for a hair braiding business using machine learning. The goal is to identify when specific products are likely to run out so that the business can restock proactively and avoid losing customers.

The system simulates real-world salon operations by modeling customer demand, product usage, and inventory behavior.

---

## Problem Statement

Small businesses such as hair braiding salons often face challenges with inventory management. Running out of essential products can result in:

- Lost revenue  
- Poor customer experience  
- Inefficient operations  

This project aims to address this issue by predicting stockouts before they occur.

---

## Solution

A machine learning classification model was developed to predict whether a stockout will occur based on:

- Inventory levels  
- Customer demand  
- Product type  
- Time-based patterns  

The model was deployed using FastAPI to enable real-time predictions through an API.

---

##  Dataset Description

The dataset contains approximately **2,500+ rows**, where:

> Each row represents one product on one specific day.

### Key Features

- item_name → product type (e.g., mousse, braiding hair)  
- style_type → hairstyle being performed  
- stock_level → available inventory  
- quantity_sold → units used  
- appointments_per_day → number of customers  
- promotion, is_holiday → demand drivers  

---

##  Feature Engineering

Feature engineering was applied to improve model performance by capturing meaningful patterns.

Examples include:

- Extracting day of week and month from the date  
- Creating stock_pressure to represent inventory risk  
- Building item_style to capture interactions between product and hairstyle  
- Generating lag and rolling average features to reflect demand trends  

---

## Model Selection

The model used is a:

### Random Forest Classifier

### Justification

- Handles non-linear relationships effectively  
- Works well with both numerical and categorical data  
- Captures interactions between features  
- Reduces risk of overfitting through ensemble learning  

---

### Key Insight

Recall was prioritized because missing a stockout can lead to lost sales and negative customer impact.

---

## Evaluation Metrics

- Precision → How often predicted stockouts are correct  
- Recall → How many actual stockouts are detected  
- F1-score → Balance between precision and recall  
- Confusion Matrix → Breakdown of predictions  

---

##  Deployment

The model was deployed using FastAPI, allowing users to send input data and receive stockout predictions in real time.

---

## Docker Support

The application was containerized using Docker to ensure consistent deployment across environments.

---

##  Limitations

- Dataset is synthetic and may not fully reflect real-world variability  
- Stockouts are inferred rather than directly observed  
- External factors such as weather or events are not included  

## 👩🏾‍💻 Author

Stephanie Adaku  
Machine Learning Capstone Project