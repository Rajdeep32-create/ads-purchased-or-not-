import streamlit as st
import pandas as pd
import pickle 

# Load the saved model
# filename = 'log_model.pkl'
log = pickle.load(open('/content/log_model.pkl', 'rb'))

# Streamlit app
st.title("Social Media Ad Purchase Prediction")

age = st.number_input("Enter Age:", min_value=18, max_value=100, value=18)
estimated_salary = st.number_input("Enter Estimated Salary:", min_value=1000, max_value=200000, value=15000)

if st.button("Predict"):
  prediction = log.predict([[age, estimated_salary]])
  if prediction[0] == 1:
    st.success("The user is likely to purchase the product.")
  else:
    st.warning("The user is unlikely to purchase the product.")
