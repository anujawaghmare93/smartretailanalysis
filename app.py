import streamlit as st
import pandas as pd
import joblib

# Load Data
df = pd.read_csv('data/cleaned/cleaned_superstore.csv')

# Load Model
model = joblib.load('models/sales_prediction_model.pkl')

st.title("Smart Retail Analytics Dashboard")

# Show Dataset
st.subheader("Dataset")
st.dataframe(df.head())

# User Inputs
quantity = st.number_input("Quantity", 1, 20)
discount = st.number_input("Discount", 0.0, 1.0)
profit = st.number_input("Profit", 0.0, 5000.0)


# Prediction
if st.button("Predict Sales"):
    
    prediction = model.predict(
        [[quantity, discount, profit]]
    )

    st.success(f"Predicted Sales: {prediction[0]:.2f}")