# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 22:31:39 2020

@author: ayand
"""

import pickle
import streamlit as st

model=pickle.load(open('random_forest_classifier_model.pkl','rb'))

def welcome():
    return "Welcome All"

def predict_note_authentication(variance,skewness,curtosis,entropy):
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    prediction=model.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction

def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator Machine Learning App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Type Here")
    skewness = st.text_input("Skewness","Type Here")
    curtosis = st.text_input("Curtosis","Type Here")
    entropy = st.text_input("Entropy","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success("The output is {}".format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()