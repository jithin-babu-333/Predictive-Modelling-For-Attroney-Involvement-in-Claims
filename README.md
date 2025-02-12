Predictive Modelling for Attorney Analysis

Overview

This project leverages machine learning techniques to predict whether an attorney will be involved in an insurance claim based on various factors such as claim amount, accident severity, policy type, and claimant details. By analyzing historical data, the model provides insights that can help insurance companies optimize their claim-handling process and reduce unnecessary legal costs.

Features

Predicts attorney involvement in claims using machine learning models.

Interactive web-based interface powered by Streamlit.

Data preprocessing and feature selection for improved model performance.

Supports real-time predictions based on user input.

Deployable as a web application for ease of access.

Technical Stack

Programming Language: Python

Libraries & Frameworks: Streamlit, Scikit-learn, Pandas, NumPy, Joblib, Pillow

Modeling Techniques: Logistic Regression, Decision Trees, Random Forest, and Gradient Boosting

Deployment: Streamlit-based web application

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

Model Performance

Accuracy: ~85%

Precision: 82%

Recall: 78%

F1-Score: 80%

Feature Importance: Claim amount, accident severity, policy type were the most influential factors.

File Structure

deploy.py - Streamlit application for deployment

InsurancePrediction.ipynb - Jupyter notebook containing model training and evaluation

preprocessor.pkl - Preprocessing pipeline for feature transformation

feature_selector.pkl - Feature selection pipeline

best_model.pkl - Trained machine learning model

Future Enhancements

Incorporate deep learning techniques for improved accuracy.

Enhance dataset with additional claim-related features.

Deploy the model as an API for wider usability.

Improve UI/UX with more visual insights and explanations.

Dependencies

Refer to requirements.txt for the list of required Python packages.

Author

Jithin Babu
 LinkedIn Profile

License

This project is licensed under the MIT License.

