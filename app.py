import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("dengue_predictor.pkl")

st.set_page_config(page_title="DenguePredict AI", layout="centered")

st.title("🦟 DenguePredict AI")
st.write("Predict dengue using blood test parameters")

st.header("Enter Patient Details")

age = st.number_input("Age", min_value=0.0)
gender = st.selectbox("Gender", ["Female", "Male"])
hb = st.number_input("Hemoglobin")
wbc = st.number_input("WBC Count")
diff = st.number_input("Differential Count")
rbc = st.number_input("RBC Count")
platelet = st.number_input("Platelet Count")
pdw = st.number_input("PDW")

# Gender convert
gender_val = 1 if gender == "Male" else 0

if st.button("Predict"):

    input_data = np.array([[age, gender_val, hb, wbc, diff, rbc, platelet, pdw]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Dengue Positive")
    else:
        st.success("✅ Dengue Negative")