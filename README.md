# Predictive Modelling for Attorney Analysis

## 📌 Overview
Predictive Modelling for Attorney Analysis is a machine learning-powered tool designed to predict whether an attorney will be involved in an insurance claim based on various factors like claim amount, accident severity, and policy type. The goal is to help insurance companies streamline claims handling and reduce unnecessary legal costs.

## 🚀 Features
- AI-powered attorney involvement prediction
- Interactive web-based interface (Streamlit)
- Real-time input and instant predictions
- Preprocessing and feature selection for better model accuracy
- Deployable as a web application

## 🔧 Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/jithin-babu-gif/Predictive-Modelling-for-Attorney-Analysis.git
cd Predictive-Modelling-for-Attorney-Analysis
```
### 2️⃣ Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Running the Application
```bash
streamlit run deploy.py
```
This will launch the Streamlit application in your browser.

## 📊 Model Performance
| Metric       | Score |
|-------------|-------|
| Accuracy    | 85%   |
| Precision   | 82%   |
| Recall      | 78%   |
| F1-Score    | 80%   |

**Key Features Influencing Prediction:**
- Claim Amount
- Accident Severity
- Policy Type

## 📂 Project Structure
```
📁 Predictive-Modelling-for-Attorney-Analysis
│── 📄 deploy.py              # Streamlit app for model deployment
│── 📄 InsurancePrediction.ipynb  # Model training and evaluation notebook
│── 📄 preprocessor.pkl       # Preprocessing pipeline
│── 📄 feature_selector.pkl   # Feature selection pipeline
│── 📄 best_model.pkl         # Trained machine learning model
│── 📄 requirements.txt       # Dependencies list
```

## 🔮 Future Enhancements
- Improve model performance with deep learning
- Expand dataset with additional claim-related features
- API deployment for broader usability
- Enhanced UI with better visualization insights

## 👨‍💻 Author
[Jithin Babu](https://github.com/jithin-babu-gif)  
[LinkedIn Profile](https://www.linkedin.com/in/jithin-babu-a34287246)

## 📜 License
This project is licensed under the **MIT License**.

