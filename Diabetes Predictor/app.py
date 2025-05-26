import streamlit as st
import numpy as np
import joblib

# Load the saved model and scaler
model = joblib.load('diabetes_model.sav')
scaler = joblib.load('scaler.sav')

st.title('🩺 Diabetes Prediction Web App')

st.write("### Enter the following health details:")

# Input fields with pre-filled realistic average values
Pregnancies = st.number_input('Number of Pregnancies', min_value=0, value=2)
Glucose = st.number_input('Glucose Level', min_value=0, value=120)
BloodPressure = st.number_input('Blood Pressure value', min_value=0, value=70)
SkinThickness = st.number_input('Skin Thickness value', min_value=0, value=20)
Insulin = st.number_input('Insulin Level', min_value=0, value=79)
BMI = st.number_input('BMI value', min_value=0.0, format="%.2f", value=32.0)
DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0, format="%.3f", value=0.47)
Age = st.number_input('Age of the Person', min_value=1, value=33)

# Prediction button
if st.button('🔍 Diabetes Test Result'):
    input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                            Insulin, BMI, DiabetesPedigreeFunction, Age]])

    std_data = scaler.transform(input_data)
    prediction = model.predict(std_data)

    if prediction[0] == 0:
        st.success('✅ The person is **not diabetic**.')
    else:
        st.error('⚠️ The person **is diabetic**.')
