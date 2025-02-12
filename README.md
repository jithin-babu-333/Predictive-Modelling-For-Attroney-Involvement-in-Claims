Predictive Modelling for Attorney Analysis

Overview

This project predicts whether an attorney will be involved in an insurance claim based on various factors. The model is deployed using Streamlit, allowing users to input claim details and receive instant predictions.

Features

Predicts attorney involvement in claims

Interactive user input via a web interface

Uses machine learning models for accurate predictions

Deployed using Streamlit

Installation

1. Clone the Repository

git clone https://github.com/jithin-babu-gif/Predictive-Modelling-for-Attorney-Analysis.git
cd Predictive-Modelling-for-Attorney-Analysis

2. Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows

3. Install Dependencies

pip install -r requirements.txt

Running the Application

streamlit run deploy.py

File Structure

deploy.py - Streamlit application for deployment

InsurancePrediction.ipynb - Jupyter notebook containing model training

preprocessor.pkl - Preprocessing pipeline

feature_selector.pkl - Feature selection pipeline

best_model.pkl - Trained machine learning model

Dependencies

Refer to requirements.txt for the list of required Python packages.

Author

Jithin Babu
LinkedIn Profile

License
This project is licensed under the MIT License.

