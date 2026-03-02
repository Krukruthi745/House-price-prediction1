import pandas as pd
import streamlit as st
import joblib

# Load trained model
model = joblib.load('Dragon.joblib')

st.title("🏠 House Price Prediction (Boston Housing)")
st.write("Enter the house details below to predict the price")

# Correct input features (NO MEDV, NO CentralAir)
inputs = [
    'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM',
    'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'
]

input_data = {}

for feature in inputs:
    if feature == 'CHAS':
        # Binary feature (0 or 1)
        input_data[feature] = st.selectbox(
            "CHAS (Near Charles River)",
            options=[0, 1]
        )
    else:
        input_data[feature] = st.number_input(
            f"{feature}",
            value=0.0,
            step=0.1
        )

if st.button("Predict Price"):
    input_df = pd.DataFrame([input_data], columns=inputs)
    prediction = model.predict(input_df)

    st.success(f"🏡 Predicted House Price: ${prediction[0] * 1000:,.2f}")
