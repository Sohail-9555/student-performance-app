# 📘 Student Performance Prediction (XGBoost + Streamlit)

A machine learning web application that predicts a student's **total performance score** using study hours, attendance, and class participation. The model is powered by **XGBoost Regression** and deployed with **Streamlit Cloud** for a smooth, interactive user experience.

---

## 🔗 Live Demo

👉 **Try the App:** [https://student-performance-app-464.streamlit.app/](https://student-performance-app-464.streamlit.app/)

## 🚀 Features

* **XGBoost Regression Model**
* **Optuna Hyperparameter Tuning**
* **Interactive Streamlit Web App**
* **Real-time Student Score Prediction**
* **Fully Deployable on Streamlit Cloud**

---

## 📁 Project Structure

```
├── app.py                               # Streamlit UI application
├── student_performance_xgboost.pkl       # Trained ML model
├── requirements.txt                      # Dependencies
└── README.md                             # Documentation
```

---

## 🧠 Model Overview

### **Model Inputs**

| Feature                 | Description                    |
| ----------------------- | ------------------------------ |
| weekly_self_study_hours | Weekly hours spent studying    |
| attendance_percentage   | Attendance percentage (0–100%) |
| class_participation     | Participation score (0–10)     |

### **Target Variable**

* Total Student Performance Score

### **Model Performance**

* **R² Score:** 0.7177
* **RMSE:** 8.19

---

## 🖥 Deployment (Streamlit Cloud)

1. Upload your repo to GitHub
2. Open [https://share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Select `app.py` as the entry file
5. Choose Python version: 3.11
6. Confirm `requirements.txt` is detected
7. Deploy 🚀

---

## 🛠 Local Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🧰 Tech Stack

* Python
* XGBoost
* Optuna
* Scikit-Learn
* Streamlit
* Pandas / NumPy

---

## 🙌 Acknowledgements

This project demonstrates a complete ML lifecycle: training, tuning, serialization, and cloud deployment.
