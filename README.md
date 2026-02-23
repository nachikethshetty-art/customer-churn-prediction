# 📉 Customer Churn Prediction System

An end-to-end Machine Learning project that predicts customer churn using behavioral and subscription data. The system includes data analysis, model training, and a production-ready Streamlit web application.

---

## 🚀 Project Overview

Customer churn is a critical problem in the telecom industry. Retaining existing customers is significantly cheaper than acquiring new ones. This project builds a predictive system to identify customers at high risk of churn so that proactive retention strategies can be applied.

---

## 🎯 Objectives

* Perform exploratory data analysis on telecom customer data
* Build and compare multiple ML models
* Identify key drivers of churn
* Deploy an interactive Streamlit web application
* Provide business recommendations for customer retention

---

## 🗂️ Project Structure

Customer-Churn-Prediction/
├── app/  (Streamlit application)
├── models/  (Saved model artifacts)
├── notebooks/  (Jupyter analysis)
├── reports/  (Screenshots and outputs)
├── requirements.txt
└── README.md

---

## 📊 Dataset

* Telecom Customer Churn Dataset
* ~7,000 customers
* Binary classification problem

**Target Variable:** `Churn`

---

## 🔧 Tech Stack

**Languages & Libraries**

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* Matplotlib

**Deployment**

* Streamlit
* Joblib

---

## 🧠 Machine Learning Approach

### Models Trained

* Logistic Regression (Baseline)
* Random Forest
* XGBoost

### ✅ Best Model

**Logistic Regression** achieved the best performance on this dataset, indicating strong linear separability in customer churn behavior.

---

## 📈 Model Performance

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | ~0.80    |
| Random Forest       | ~0.78    |
| XGBoost             | ~0.77    |

*(Your exact values may vary slightly)*

---

## 🔍 Key Business Insights

* Month-to-month customers show higher churn risk
* Customers with shorter tenure are more likely to leave
* Higher monthly charges correlate with increased churn
* Electronic check payment users exhibit higher churn

---

## 💡 Business Recommendations

* Target early-tenure customers with onboarding offers
* Provide loyalty discounts for month-to-month users
* Monitor high monthly charge customers closely
* Encourage automatic payment methods

---

## 🖥️ Streamlit Web App

The project includes a production-style interactive dashboard where users can:

* Input customer details
* View churn probability
* See risk level classification
* Get real-time predictions

---

## 📸 Application Screenshots

screenshots are in reports 
---

## ⚙️ How to Run Locally

### 1️⃣ Clone the repository

git clone <your-repo-link>
cd Customer-Churn-Prediction

### 2️⃣ Install dependencies

pip install -r requirements.txt

### 3️⃣ Run the Streamlit app

streamlit run app/app.py

---

## 👨‍💻 Author

**Nachiketh S Shetty**

* MSc Physics
* MBA in Data Science & Analytics
* Aspiring Data Scientist

---

## ⭐ Future Improvements

* Hyperparameter tuning
* AWS deployment
* FastAPI inference endpoint
* Advanced class imbalance handling

---

⭐ If you found this project useful, consider giving it a star!
