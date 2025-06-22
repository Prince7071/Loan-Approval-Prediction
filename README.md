# Loan Approval Prediction

A machine learning project to predict loan approvals based on applicant details using classification algorithms.

## Problem Statement

Financial institutions receive thousands of loan applications. Automating loan approval prediction can help save time, reduce bias, and assist in decision-making.

## Dataset

- Source: [Kaggle Loan Prediction Dataset](https://www.kaggle.com/datasets)
- Files used: `train.csv`, `test.csv`
- Contains features like:
  - Gender, Married, Education, Self_Employed
  - ApplicantIncome, CoapplicantIncome
  - LoanAmount, Loan_Amount_Term
  - Credit_History, Property_Area

## Features

- Data cleaning & preprocessing
- Feature engineering
- Exploratory Data Analysis (EDA)
- Multiple ML models: 
  - Random Forest
  - Naive Bayes
  - Decision Tree
  - KNN
- Model evaluation: accuracy, confusion matrix, classification report
- Hyperparameter tuning using GridSearchCV
- Streamlit app for live prediction

## Model Performance

| Model            | Accuracy |
|------------------|----------|
| Random Forest    | 84%      |
| Naive Bayes      | ~79%     |
| Decision Tree    | ~81%     |
| KNN              | ~77%     |

## Streamlit App

Use the interactive web app to predict loan approval in real-time.

To run:

```bash
streamlit run loan_app.py
