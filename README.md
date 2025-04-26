# 🧠 Gender-Aware Diabetes Risk Prediction System

This is a professional Streamlit web application for predicting diabetes risk based on patient health indicators, with gender-aware inputs and clear medical explanations.

## 📋 Project Description
This project uses a Gradient Boosting Machine (GBM) model to predict whether a patient is at high or low risk of developing diabetes.  
The form dynamically adjusts based on selected gender to enhance user experience and realism.

## 🚀 Features
- Gender-aware dynamic input form (Pregnancies hidden for Males).
- Clean user interface with clear risk explanation.
- Honest output with medical disclaimers.
- Built using **Streamlit**, **scikit-learn**, and **pandas**.

## 🏗️ Project Structure
| File | Description |
|:----|:------------|
| `app.py` | Streamlit web application |
| `best_gb_model.pkl` | Pre-trained Gradient Boosting model |
| `diabetes.csv` | Dataset for training |
| `diabetes.ipynb` | Notebook for model building and tuning |

## 📦 Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/diabetes-risk-prediction-app.git
    cd diabetes-risk-prediction-app
    ```

2. Install required packages:
    ```bash
    pip install streamlit pandas scikit-learn joblib
    ```

3. Run the application:
    ```bash
    streamlit run app.py
    ```

## 🛡️ Disclaimer
> This prediction system is intended for informational purposes only.  
> It does not replace professional medical diagnosis or treatment.  
> Always consult healthcare professionals for medical concerns.

## 👨‍💻 Author
- [Abdullahi Bishar]

---
