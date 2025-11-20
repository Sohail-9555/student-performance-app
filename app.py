import streamlit as st
import joblib
import numpy as np
import pandas as pd

# ------------------------------------------------------------
# Load Model
# ------------------------------------------------------------
model = joblib.load("student_performance_xgboost.pkl")

# ------------------------------------------------------------
# UI
# ------------------------------------------------------------
st.set_page_config(page_title="Student Performance Predictor", page_icon="📘")

st.title("📘 Student Performance Predictor")
st.write("Enter student details to predict their total score.")

# Inputs
hours = st.number_input("Weekly Self-Study Hours", 0.0, 40.0, step=0.5)
attendance = st.slider("Attendance Percentage (%)", 0, 100, 75)
participation = st.slider("Class Participation (0–10)", 0, 10, 5)

# Predict Button
if st.button("Predict Score"):
    input_data = pd.DataFrame([{
        "weekly_self_study_hours": hours,
        "attendance_percentage": attendance,
        "class_participation": participation
    }])
    
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Total Score: **{prediction:.2f}**")
    



