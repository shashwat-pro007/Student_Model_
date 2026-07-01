import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("marks_prediction_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Marks Prediction",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Marks Prediction")
st.write("Predict student marks based on study hours and attendance.")

# User Inputs
study_hours = st.number_input(
    "Study Hours per Day",
    min_value=0.0,
    max_value=24.0,
    value=5.0,
    step=0.5
)

attendance = st.slider(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=80
)

# Prediction
if st.button("Predict Marks"):

    features = np.array([[study_hours, attendance]])

    prediction = model.predict(features)

    st.success(f"Predicted Marks: {prediction[0]:.2f}")