import streamlit as st
import pickle
import numpy as np


with open('rf_model.pkl', 'rb') as file:
    model = pickle.load(file)



st.title("Loan Approval Prediction")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income")
coapplicant_income = st.number_input("Coapplicant Income")
loan_amount = st.number_input("Loan Amount")
loan_term = st.number_input("Loan Amount Term", value=360)
credit_history = st.selectbox("Credit History", ["Good (1.0)", "Bad (0.0)"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])







gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
education = 0 if education == "Graduate" else 1
self_employed = 1 if self_employed == "Yes" else 0
credit_history = 1.0 if credit_history == "Good (1.0)" else 0.0
property_area = {'Urban': 2, 'Semiurban': 1, 'Rural': 0}[property_area]




input_features = np.array([[gender, married, education, self_employed,
                            applicant_income, loan_amount,
                            loan_term, credit_history]])

if st.button("Predict"):
    prediction = model.predict(input_features)
    if prediction[0] == 1:
        st.success("Loan Approved!")
    else:
        st.error("Loan Not Approved.")
