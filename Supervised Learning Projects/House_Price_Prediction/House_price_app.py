import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model
model = joblib.load("/Users/anands/House_Price_Prediction/model/house_price_model.pkl")

st.set_page_config(page_title="House Price Prediction", layout="centered")

st.title("🏠 House Price Prediction App")


st.write("Enter house details:")

# ----------- INPUTS -----------
Area_sqft = st.number_input("Area (sqft)", min_value=300, max_value=10000, step=50)
Bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, step=1)
Bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, step=1)
Floors = st.number_input("Floors", min_value=1, max_value=5, step=1)
ParkingSpaces = st.number_input("Parking Spaces", min_value=0, max_value=5, step=1)
DistanceToCityCenter_km = st.number_input("Distance to City Center (km)", min_value=0.0, max_value=50.0, step=0.5)
CrimeRate = st.number_input("Crime Rate", min_value=0.0, max_value=100.0, step=0.1)
SchoolRating = st.number_input("School Rating (1-10)", min_value=1.0, max_value=10.0, step=0.1)
Age_years = st.number_input("House Age (years)", min_value=0, max_value=100, step=1)

# ----------- PREDICTION -----------
if st.button("Predict Price"):
    input_data = pd.DataFrame({
        "Area_sqft": [Area_sqft],
        "Bedrooms": [Bedrooms],
        "Bathrooms": [Bathrooms],
        "Floors": [Floors],
        "ParkingSpaces": [ParkingSpaces],
        "DistanceToCityCenter_km": [DistanceToCityCenter_km],
        "CrimeRate": [CrimeRate],
        "SchoolRating": [SchoolRating],
        "Age_years": [Age_years]
    })

    prediction = model.predict(input_data)

    st.success(f"🏠 Estimated House Price: ₹ {prediction[0]:,.2f}")

# streamlit run ./House_Price_Prediction/House_price_app.py