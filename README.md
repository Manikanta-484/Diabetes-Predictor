# 🩺 Diabetes Prediction Web App

A simple web application built with **Streamlit** and **Scikit-learn** that predicts whether a person is diabetic based on medical input data. The model uses the **PIMA Indians Diabetes Dataset**.

---

## 🚀 Features

- Interactive UI using Streamlit
- Real-time predictions
- Trained using Support Vector Machine (SVM)
- Scaled using StandardScaler
- Model and Scaler are saved using Joblib
- Ready to deploy

---

## 📊 Dataset

The dataset used is the [PIMA Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database), which contains the following features:

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age
- Outcome (0 = Non-diabetic, 1 = Diabetic)

---

## 🛠️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

### 2. Install the required libraries
```bash
pip install -r requirements.txt

### 3. Add the model files
Make sure the following files are present in the same directory:

diabetes_model.sav

scaler.sav

(These files are generated and downloaded from the training notebook in Google Colab.)

### 4. Run the app
```bash
streamlit run app.py
