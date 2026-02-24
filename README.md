# 📉 Customer Churn Prediction System

An end-to-end **production-grade machine learning system** that predicts telecom customer churn using Logistic Regression, FastAPI, Streamlit, and Explainable AI (SHAP).

This project demonstrates the complete ML lifecycle — from data preprocessing and model optimization to cloud deployment and model interpretability.

---
---

## 📌 Project Overview

Customer churn is one of the most critical challenges in the telecom industry. Acquiring new customers is significantly more expensive than retaining existing ones. This project builds a production-ready machine learning system to proactively identify customers who are likely to discontinue the service.

The solution combines **predictive modeling, real-time inference, and explainable AI** to help businesses take timely retention actions and reduce revenue loss.

---

## 🎯 Project Objective

The primary objectives of this project are:

* Predict the probability of customer churn using historical behavioral data
* Improve churn detection through class imbalance handling
* Optimize decision threshold for business-aligned recall
* Provide real-time predictions via FastAPI and Streamlit
* Enhance model transparency using SHAP explainability
* Deliver an end-to-end deployable ML system suitable for production environments

---

## 🌍 Real-World Applications

This system can be directly applied in:

* 📡 Telecom customer retention programs
* 💳 Subscription-based businesses (OTT, SaaS, fintech)
* 🏦 Banking and insurance customer attrition analysis
* 🛒 E-commerce customer loyalty monitoring
* 🎯 Targeted marketing and retention campaigns

Organizations can integrate this pipeline to **identify high-risk customers early and trigger personalized retention strategies**.

---

## 💼 Business Insights & Impact

From a business perspective, the model is optimized to prioritize **high churn recall**, ensuring that most at-risk customers are identified.

**Key business considerations:**

* ✅ Threshold tuned from 0.50 → **0.45** to improve churn capture
* ✅ Class imbalance handled to avoid majority-class bias
* ✅ Model achieves ~0.83 ROC-AUC indicating strong separation
* ✅ SHAP explanations provide actionable feature-level insights
* ✅ System enables proactive retention instead of reactive loss handling

**Business value:**

* Reduce customer acquisition costs
* Improve customer lifetime value (CLV)
* Enable data-driven retention campaigns
* Increase revenue protection
* Build trust through explainable predictions

---


## 🌐 Live Demo

### 🔗 Streamlit Dashboard

👉 https://customer-churn-prediction-n6fkpnzogb7ahp9waffxvk.streamlit.app/

### 🔗 FastAPI Swagger

👉 https://churn-fastapi-0h53.onrender.com/docs

### 🧠 Health Check

👉 https://churn-fastapi-0h53.onrender.com/

---

## 🎯 Key Highlights

* 📊 End-to-end churn prediction pipeline
* ⚖️ Class imbalance handling using `class_weight='balanced'`
* 🎯 Decision threshold optimization (0.45) for business alignment
* 🔍 SHAP-based Explainable AI integration
* ⚡ Real-time inference via FastAPI
* 🎨 Interactive Streamlit dashboard
* ☁️ Cloud deployment on Render & Streamlit Cloud
* 🧩 Modular and production-ready architecture

---

## 🏗️ System Architecture

```id="arch1"
User Input → Streamlit UI → FastAPI → Preprocessing → Scaler → ML Model → Prediction + SHAP Explanation
```

---

## 📊 Model Performance

**Model:** Logistic Regression
**ROC-AUC:** ~0.83

### 🎯 Business-Focused Optimization

* Improved churn recall through class balancing
* Tuned probability threshold from **0.50 → 0.45**
* Better alignment with customer retention strategy

---

## 🔍 Explainable AI

Integrated **SHAP (SHapley Additive exPlanations)** to improve model transparency.

**Capabilities:**

* Local prediction explanations
* Feature contribution visualization
* Business interpretability support
* Trustworthy AI predictions

---

## 📡 API Usage

### Endpoint

```id="arch2"
POST /predict
```

### 🧾 Sample Request

```json id="arch3"
{
  "SeniorCitizen": 0,
  "tenure": 12,
  "MonthlyCharges": 70,
  "TotalCharges": 1500,
  "gender": "Male",
  "Partner": "Yes",
  "Dependents": "No",
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "Yes"
}
```

### ✅ Sample Response

```json id="arch4"
{
  "churn_probability": 0.81,
  "risk_level": "High",
  "prediction": 1
}
```

---

## 🧠 Tech Stack

**Core ML**

* Python
* Scikit-learn
* Pandas & NumPy

**Deployment & Apps**

* FastAPI
* Uvicorn
* Streamlit
* Render (Cloud Hosting)
* Streamlit Community Cloud

**Explainability**

* SHAP

---

## 📂 Project Structure

```id="arch5"
customer-churn-project/
│
├── app/                 # Streamlit application
├── fastapi_app/         # FastAPI service
├── models/              # Saved model artifacts
├── data/                # Dataset
├── notebooks/           # EDA & training
├── reports/             # Screenshots & outputs
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run Locally

### 1️⃣ Install dependencies

```bash id="arch6"
pip install -r requirements.txt
```

### 2️⃣ Run FastAPI

```bash id="arch7"
python -m uvicorn fastapi_app.main:app --reload
```

Open:

```id="arch8"
http://127.0.0.1:8000/docs
```

### 3️⃣ Run Streamlit

```bash id="arch9"
streamlit run app/app.py
```

---

## 🔮 Future Improvements

* AutoML model comparison
* Advanced hyperparameter tuning
* Docker containerization
* Full AWS production deployment
* Model monitoring & drift detection
* Batch prediction pipeline

---

## 👨‍💻 Author

**Nachiketh S Shetty**
Aspiring Data Scientist | ML Engineer | AI Systems Builder

---

⭐ *If you found this project useful, consider starring the repository!*
