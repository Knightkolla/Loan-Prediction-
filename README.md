# Loan Sanction Using Machine Learning

## 📌 Project Overview
The **Loan Sanction System** is a machine learning-based tool designed to **automate loan approval decisions**. It predicts whether a loan should be sanctioned based on various factors such as **income, credit history, employment status, and financial records**.

## 🚀 Features
- **Automated Loan Approval** – AI-driven decision-making for faster loan processing.
- **High Accuracy** – Uses multiple ML models to optimize prediction performance.
- **User Input for Prediction** – Users can enter details and check their loan eligibility.
- **Local Execution** – Runs seamlessly on your local machine.

## 🛠️ Tech Stack
- **Programming Language:** Python
- **Libraries:** Scikit-Learn, Pandas, NumPy, Matplotlib, Seaborn
- **ML Models Used:** Logistic Regression, Random Forest, XGBoost (Best-performing model selected)

## 📂 Installation & Setup (Run Locally)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/loan-sanction-ml.git
cd loan-sanction-ml
```

### 2️⃣ Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Script
```bash
python loan_sanction.py
```

## 📊 How It Works
1. **Upload Dataset (if applicable)** – The system reads the dataset for loan applicants.
2. **Preprocessing** – Handles missing values, encodes categorical data, and scales numerical features.
3. **Model Training** – Trains and evaluates models to determine the best one.
4. **Make Predictions** – Users can enter their details and get an instant loan approval decision.

## 🏆 Model Evaluation
- **Accuracy Score**: XX% (Depending on dataset and model tuning)
- **Performance Metrics**: Precision, Recall, F1-Score, Confusion Matrix

## 🎯 Future Enhancements
- Implement a **dashboard** to visualize loan approval trends.
- Improve model interpretability using **SHAP & LIME**.
- Deploy on **AWS/GCP for scalability**.

## 🤝 Contributors
- **Dhavala Kartikeya Somayaji** – [LinkedIn](www.linkedin.com/in/dhavalakartikeyasomayaji) | [GitHub](https://github.com/Knightkolla)

## 📜 License
This project is licensed under the MIT License. Contributions are welcome!

