import streamlit as st
import pandas as pd
import joblib

st.title("Customer Churn Prediction")

model = joblib.load("churn_model.pkl")

tenure = st.slider("Tenure", 1, 72, 12)
monthly = st.number_input("Monthly Charges", 0.0, 500.0, 50.0)
total = st.number_input("Total Charges", 0.0, 10000.0, 500.0)

contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
internet = st.selectbox("Internet", ["DSL", "Fiber optic", "No"])

contract_map = {"Month-to-month":0, "One year":1, "Two year":2}
internet_map = {"DSL":0, "Fiber optic":1, "No":2}

input_data = pd.DataFrame({
    "tenure":[tenure],
    "MonthlyCharges":[monthly],
    "TotalCharges":[total],
    "Contract":[contract_map[contract]],
    "InternetService":[internet_map[internet]]
})

if st.button("Predict"):
    pred = model.predict(input_data)
    if pred[0] == 1:
        st.error("Customer will churn")
    else:
        st.success("Customer will stay")