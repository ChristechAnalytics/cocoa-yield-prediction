import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("🌱 Cocoa Yield Prediction - Ikom, Nigeria")
model = joblib.load('src/cocoa_model.pkl')
scaler = joblib.load('src/scaler.pkl')

st.sidebar.header("Enter Climate Data")
rainfall = st.sidebar.slider("Rainfall (mm)", 2200, 2900, 2500)
min_temp = st.sidebar.slider("Min Temperature (°C)", 23.0, 25.0, 23.8)
max_temp = st.sidebar.slider("Max Temperature (°C)", 30.0, 32.0, 30.9)
solar = st.sidebar.slider("Solar Radiation (kw/m2)", 1.8e6, 2.1e6, 2e6)
wind = st.sidebar.slider("Wind Speed (m/s)", 38.0, 45.0, 40.0)
min_rh = st.sidebar.slider("Min RH (%)", 55, 65, 60)
max_rh = st.sidebar.slider("Max RH (%)", 90, 96, 93)

input_df = pd.DataFrame([[rainfall, min_temp, max_temp, solar, wind, min_rh, max_rh]],
                         columns=["Rainfall_mm", "Min_Temp_C", "Max_Temp_C", "Solar_Radiation_kwm2",
                                  "Wind_Speed_ms", "Min_RH", "Max_RH"])
input_scaled = scaler.transform(input_df)

if st.button("Predict Cocoa Yield"):
    prediction = model.predict(input_scaled)
    st.success(f"📈 Estimated Cocoa Yield: {prediction[0]:,.2f} metric tons")