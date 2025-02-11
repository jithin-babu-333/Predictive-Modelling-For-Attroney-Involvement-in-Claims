import streamlit as st
import joblib
import numpy as np
import pandas as pd
from PIL import Image

# Load preprocessor, feature selector, and model
preprocessor = joblib.load("preprocessor.pkl")
selector = joblib.load("feature_selector.pkl")
model = joblib.load("best_model.pkl")

# Set page configuration
st.set_page_config(page_title="Attorney Involvement Prediction", page_icon="⚖️", layout="centered")

# Add a header image
image = Image.open("law_image.jpg")  # Ensure you have an appropriate image in your working directory
st.image(image, use_container_width=True)

# Title and description
st.title("⚖️ Attorney Involvement Prediction")
st.markdown(
    "This tool predicts whether an attorney will be involved in a claim based on various factors. "
    "Fill in the details below and get an instant prediction."
)

# Sidebar for user input
st.sidebar.header("Input Claim Details")

clmage = st.sidebar.number_input("Claimant Age", min_value=0, max_value=120, value=30, step=1)
loss = st.sidebar.number_input("Loss (in currency units)", value=0.0, format="%.2f")
claim_amount = st.sidebar.number_input("Claim Amount Requested", value=0.0, format="%.2f")
settlement_amount = st.sidebar.number_input("Settlement Amount", value=0.0, format="%.2f")
accident_severity = st.sidebar.selectbox("Accident Severity", ["Minor", "Moderate", "Severe"])
policy_type = st.sidebar.selectbox("Policy Type", ["Comprehensive", "Third-Party"])
driving_record = st.sidebar.selectbox("Driving Record", ["Clean", "Minor Offenses", "Major Offenses"])
clmsex = st.sidebar.selectbox("Claimant Gender", ["Male", "Female"])
clminsured = st.sidebar.selectbox("Claimant Insured", ["Yes", "No"])
seatbelt = st.sidebar.selectbox("Seatbelt Worn", ["Yes", "No"])

# Map inputs to model features
input_data = pd.DataFrame({
    "CLMAGE": [clmage],
    "LOSS": [loss],
    "Claim_Amount_Requested": [claim_amount],
    "Settlement_Amount": [settlement_amount],
    "Accident_Severity": [accident_severity],
    "Policy_Type": [policy_type],
    "Driving_Record": [driving_record],
    "CLMSEX": [1 if clmsex == "Male" else 0],
    "CLMINSUR": [1 if clminsured == "Yes" else 0],
    "SEATBELT": [1 if seatbelt == "Yes" else 0]
})

# Prediction button
if st.sidebar.button("Predict"):  
    # Preprocess input
    input_data_transformed = preprocessor.transform(input_data)
    input_data_selected = selector.transform(input_data_transformed)
    
    # Predict
    prediction = model.predict(input_data_selected)
    result_text = "Attorney Involved" if prediction[0] == 1 else "No Attorney Involved"
    result_color = "#FF4B4B" if prediction[0] == 1 else "#4CAF50"
    
    # Display result
    st.markdown(
        f"<h2 style='text-align: center; color: {result_color};'>{result_text}</h2>",
        unsafe_allow_html=True
    )

    # Additional insights (optional)
    st.success("Prediction complete! Please review the result above.")
