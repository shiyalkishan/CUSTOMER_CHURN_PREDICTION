# CUSTOMER_CHURN_PREDICTION

# Customer Churn Prediction using Machine Learning

## 📌 Project Overview

This project predicts whether a customer is likely to **churn (leave the service)** or **stay**, using a Machine Learning model trained on customer data. A simple **Streamlit web application** allows users to enter customer details and receive instant predictions.

---

## 🚀 Features

* Customer churn prediction using Machine Learning
* Interactive Streamlit web application
* Random Forest Classification model
* User-friendly interface
* Fast real-time predictions

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Pandas
* Scikit-learn
* Joblib

---

## 📂 Project Structure

```
Customer-Churn-Prediction/
│── app.py                # Streamlit web application
│── train_model.py        # Model training script
│── data.csv              # Dataset
│── churn_model.pkl       # Trained Machine Learning model
│── README.md
```

---

## 📊 Dataset

The dataset contains customer information such as:

* Tenure
* Monthly Charges
* Total Charges
* Contract Type
* Internet Service
* Churn Status (Target)

---

## 🤖 Machine Learning Model

The project uses the **Random Forest Classifier** for prediction.

### Workflow

1. Load dataset
2. Preprocess categorical data using Label Encoding
3. Split data into training and testing sets
4. Train Random Forest model
5. Save trained model using Joblib
6. Deploy model with Streamlit

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/shiyalkishan/CUSTOMER_CHURN_PREDICTION.git
```

Move into the project directory:

```bash
cd customer-churn-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📷 Application Inputs

Users provide:

* Tenure
* Monthly Charges
* Total Charges
* Contract Type
* Internet Service

The application predicts whether the customer:

* ✅ Will Stay
* ❌ Will Churn

---

## 📌 Future Improvements

* Improve model accuracy using hyperparameter tuning
* Add more customer features
* Deploy on Streamlit Cloud
* Display prediction probability
* Add data visualization dashboard

---

## 👨‍💻 Author

**Kishan Shiyal**

Computer Engineering Student | Aspiring Data Scientist

---

## 📜 License

This project is created for educational and learning purposes.
