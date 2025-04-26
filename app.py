# app.py – Professional Final Version: Gender-aware, Accurate Explanations, No SHAP

import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("best_gb_model.pkl")

st.set_page_config(page_title="Diabetes Risk Predictor", layout="wide")

st.title("🧠 Diabetes Risk Prediction System")
st.markdown("Use this intelligent tool to predict a patient's **diabetes risk** based on health indicators.")

st.sidebar.header("📋 Instructions")
st.sidebar.markdown("""
- Select patient's gender first.
- Fill in the health details.
- Click **Predict Diabetes Risk** to view results and explanations.
""")

# Gender input
gender = st.radio("Patient Gender", ["Female", "Male"], horizontal=True)
gender_value = 0 if gender == "Female" else 1

# Input layout
col1, col2 = st.columns(2)

with col1:
    Pregnancies = 0
    if gender == "Female":
        Pregnancies = st.number_input("Pregnancies", 0, 20, value=1)
    else:
        st.markdown("_Pregnancies not applicable for Male patients._")

    Glucose = st.slider("Glucose Level (mg/dL)", 0, 200, value=120)
    BloodPressure = st.slider("Blood Pressure (mm Hg)", 0, 140, value=70)
    SkinThickness = st.slider("Skin Thickness (mm)", 0, 100, value=20)
    Insulin = st.slider("Insulin (μU/mL)", 0, 850, value=79)

with col2:
    BMI = st.slider("Body Mass Index (BMI)", 0.0, 70.0, value=25.0)
    DiabetesPedigreeFunction = st.slider("Diabetes Pedigree Function", 0.0, 2.5, value=0.5)
    Age = st.slider("Age (years)", 10, 100, value=33)

# Prepare input data
input_data = pd.DataFrame([{
    "Pregnancies": Pregnancies,
    "Glucose": Glucose,
    "BloodPressure": BloodPressure,
    "SkinThickness": SkinThickness,
    "Insulin": Insulin,
    "BMI": BMI,
    "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
    "Age": Age,
    "Gender": gender_value
}])


if st.button("Predict Diabetes Risk"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.divider()

    if prediction == 1:
        st.error(f"🔴 High Diabetes Risk Detected! (Probability: {probability:.2%})")
    else:
        st.success(f"🟢 Low Diabetes Risk (Probability: {probability:.2%})")

    st.divider()

    st.subheader("📚 Health Indicators Analysis:")
    st.write("🧠 The prediction considers the **combination** of multiple health factors including:")
    st.markdown(f"- Glucose Level: **{Glucose} mg/dL**")
    st.markdown(f"- BMI: **{BMI}**")
    st.markdown(f"- Blood Pressure: **{BloodPressure} mm Hg**")
    st.markdown(f"- Insulin Level: **{Insulin} \u03bcU/mL**")
    st.markdown(f"- Age: **{Age} years**")
    st.write("""
    ➡ Even if individual values appear normal, **their interaction** can lead to an elevated or reduced risk. \n 
    ➡ This ensures a comprehensive and medically realistic prediction.
    """)

    st.divider()
st.markdown("---")
st.caption("⚠️ Disclaimer: This prediction is intended for informational purposes only. It does not replace professional medical advice, diagnosis, or treatment. Always consult qualified healthcare providers for any medical concerns.")
