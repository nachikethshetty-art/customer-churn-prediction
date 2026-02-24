import streamlit as st
import pandas as pd
import joblib
import os

# ----------------------
# Page Config
# ----------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📉",
    layout="wide"
)

# ----------------------
# Load artifacts
# ----------------------
@st.cache_resource
def load_artifacts():
    model_path = os.path.join("models", "churn_logistic_model.pkl")
    scaler_path = os.path.join("models", "scaler.pkl")
    columns_path = os.path.join("models", "feature_columns.pkl")

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    feature_columns = joblib.load(columns_path)

    return model, scaler, feature_columns

model, scaler, FEATURE_COLUMNS = load_artifacts()

# ----------------------
# Header
# ----------------------
st.title("📉 Customer Churn Prediction Dashboard")
st.markdown(
    "Predict whether a telecom customer is likely to churn using a trained ML model."
)
st.divider()

# ======================
# SIDEBAR INPUTS ⭐
# ======================
st.sidebar.header("🧾 Customer Inputs")

tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.sidebar.number_input(
    "Monthly Charges", min_value=0.0, max_value=200.0, value=70.0
)
total_charges = st.sidebar.number_input(
    "Total Charges", min_value=0.0, max_value=10000.0, value=1000.0
)

contract = st.sidebar.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

internet_service = st.sidebar.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

payment_method = st.sidebar.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

predict_btn = st.sidebar.button("🔍 Predict Churn")

# ----------------------
# Create input dataframe
# ----------------------
def create_input_dataframe():
    input_dict = {
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
    }

    input_df = pd.DataFrame([input_dict])
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=FEATURE_COLUMNS, fill_value=0)

    return input_df

# ======================
# MAIN PANEL
# ======================
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📊 Prediction Status")

    if predict_btn:

        if monthly_charges <= 0:
            st.warning("⚠️ Monthly charges should be greater than 0.")
        else:
            input_df = create_input_dataframe()
            input_scaled = scaler.transform(input_df)
            probability = model.predict_proba(input_scaled)[0][1]
            THRESHOLD = 0.45
            prediction = int(probability >= THRESHOLD)

            # Risk level
            if probability < 0.3:
                risk_level = "🟢 Low Risk"
            elif probability < 0.6:
                risk_level = "🟡 Medium Risk"
            else:
                risk_level = "🔴 High Risk"

            st.metric(
                label="Churn Probability",
                value=f"{probability:.2%}"
            )

            st.progress(float(probability))

            st.subheader(f"Risk Level: {risk_level}")

            if prediction == 1:
                st.error("⚠️ Customer is likely to churn")
            else:
                st.success("✅ Customer is likely to stay")

with col2:
    st.subheader("ℹ️ Model Information")
    st.info(
        """
        **Model:** Logistic Regression  
        **Problem Type:** Binary Classification  
        **Use Case:** Customer Retention Analytics  

        This tool helps identify customers at risk of leaving so that
        businesses can take proactive retention actions.
        """
    )

# ----------------------
# Footer
# ----------------------
st.divider()
st.caption("Built by Nachiketh S Shetty • End-to-End Customer Churn ML Project")