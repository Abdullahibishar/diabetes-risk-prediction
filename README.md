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

Hyperparameter tuning was performed using GridSearchCV over a wide parameter space, optimizing for F1-score. However, after evaluation, the original Gradient Boosting model exhibited superior overall performance with higher accuracy and F1-Score. Therefore, the original model was retained for deployment to ensure more reliable predictions.

### 📚 SHAP Explainability Note

During model evaluation, SHAP (SHapley Additive exPlanations) was used to interpret the Gradient Boosting model’s behavior. The SHAP analysis revealed that features like Glucose, BMI, and Age were the most influential in driving diabetes predictions, while Gender and Skin Thickness had relatively lower impacts.

However, SHAP visualizations were not integrated into the final deployed app to maintain simplicity and accessibility for general users. Instead, health indicator summaries were provided in natural language to ensure transparency without overwhelming non-technical users.

This approach ensures that while the model remains technically explainable, the deployed interface stays user-friendly and aligned with best practices in healthcare AI communication.


## 📦 Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Abdullahibishar/diabetes-risk-prediction-app.git
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
- Abdullahi Bishar

---
