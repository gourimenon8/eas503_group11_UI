import streamlit as st
import json
import requests

st.title('Salary Prediction')

st.header("Group 11")

st.subheader("Members:")
st.subheader("Gouri Menon")
st.subheader("Valencia Dmello")

with open('input.json') as f:
  input_sample = json.load(f)

inputs = {}


for key in input_sample.keys():
  inputs[key] = st.text_input(key, input_sample[key])

if st.button('Predict Salary'):
    response = requests.post('http://174.138.82.208:8080/predict', json=inputs)
    prediction = response.json()
    
    st.write('The predicted salary is:', prediction['prediction'])  
