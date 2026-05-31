# 📊 Credit Risk Modelling App (Machine Learning)

A **production-style Machine Learning web app** built with **Streamlit**, which predicts **loan default probability**, generates a **credit score**, and assigns a **risk rating** based on user financial and behavioral data.

---

## 🚀 Live Demo

[](https://ml-project-credit-risk-modeling-app.streamlit.app/)

---

## 🧠 Project Overview

This project uses a **supervised Machine Learning model** trained on credit behavior data to evaluate borrower risk.

The system predicts:

- 📉 Probability of default
- 💳 Credit score (300 – 900 scale)
- ⭐ Risk rating (Poor / Average / Good / Excellent)

---

## 🏗️ Features

- Interactive **Streamlit UI**
- Real-time credit risk prediction
- Loan-to-income ratio feature engineering
- One-hot encoding for categorical variables
- Scaled numerical features using **MinMaxScaler**
- Model serialization using **Joblib**
- Clean, SaaS-style UI design

---

## 🧾 Input Features

The model uses the following inputs:

### Financial Inputs
- Age  
- Income  
- Loan Amount  
- Loan Tenure  
- Number of Open Accounts  
- Credit Utilization Ratio  
- Delinquency Ratio  
- Avg DPD per delinquency  

### Categorical Inputs
- Residence Type (Owned / Rented / Mortgage)  
- Loan Purpose (Education / Home / Personal / Auto)  
- Loan Type (Secured / Unsecured)

---

## ⚙️ Tech Stack

- Python 🐍
- Streamlit 🎈
- Pandas & NumPy
- Scikit-learn
- Joblib
- Machine Learning (Regression + Logistic Transformation)

---

## 🧠 Model Workflow

1. User inputs data via Streamlit UI  
2. Feature engineering (e.g., Loan-to-Income ratio)  
3. Data scaling using saved `MinMaxScaler`  
4. Model prediction using trained ML model  
5. Conversion to:
   - Default Probability  
   - Credit Score (300–900)  
   - Risk Rating  

---

## 📊 Output Explanation

| Metric | Description |
|--------|-------------|
| Default Probability | Chance of loan default |
| Credit Score | Scaled score (300–900) |
| Rating | Risk category (Poor → Excellent) |

---

## 📁 Project Structure
health-insurance-cost-predictor/
│
├── main.py # Streamlit UI
├── prediction_helper.py # ML pipeline & prediction logic
├── artifacts/ # Saved model + scaler
├── requirements.txt # Dependencies
└── README.md

---

## 🧪 How to Run Locally

```bash
# Clone repository
git clone https://github.com/your-username/credit-risk-modeling.git

# Navigate to project
cd credit-risk-modeling

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run main.py


## 📦 Requirements

```txt
streamlit
pandas
numpy
scikit-learn
joblib
```

---

## 📈 Model Formula (Concept)

The model uses logistic transformation:

```math
P(default) = 1 / (1 + e^{-x})
```

Credit Score scaling:

```math
Credit Score = 300 + (Non-default Probability × 600)
```

---

## 🎯 Future Improvements

- Add SHAP explainability  
- Deploy with Docker  
- Add user authentication  
- Store predictions in database  
- Add dashboard analytics  

---

## 👩‍💻 Author

**Ayesha Rajput**  
Machine Learning & Full Stack Developer  

📌 Built with ❤️ using Python & Streamlit
