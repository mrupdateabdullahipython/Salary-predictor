import streamlit as st
import numpy as np
import joblib

model = joblib.load("model.pkl")

st.title("💼 Salary Prediction App")

experience = st.number_input("Years of Experience", 0.0, 50.0, step=0.5)

if st.button("Predict Salary"):
    prediction = model.predict(np.array([[experience]]))
    st.success(f"Estimated Salary: {prediction[0]:.2f}")