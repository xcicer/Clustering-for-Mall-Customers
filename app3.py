import streamlit as st
import pickle
import pandas as pd
import numpy as np
pickled_model = pickle.load(open('modell.pkl', 'rb'))
t = pickled_model
st.title("Clustering for Mall Customers")
Annual_Income = st.text_input("Input your annual income in k($)") 
spendings = st.slider("choose your spending score in 0_100 range" ,0,100)

prediction = st.button('Predict')
if prediction:
    X = np.array([Annual_Income, spendings])
    y = pd.DataFrame([X])
    prediction = t.predict(y)
    if prediction == 0: 
         st.subheader('This person belongs to  group where maximum annual income 76K dollars and minimum is 39K dollars and maximum spending score is 61 and minimum is 34 between 1-100 range')
    elif prediction == 1: 
         st.subheader('This person belongs to  group where maximum annual income 137K dollars and minimum is 70K dollars and maximum spending score is 39 and minimum is 1 between 1-100 range')
    elif prediction == 2: 
         st.subheader('This person belongs to  group where maximum annual income 39K dollars and minimum is 15K dollars and maximum spending score is 40 and minimum is 3 between 1-100 range')    
    elif prediction == 3: 
         st.subheader('This person belongs to  group where maximum annual income 39K dollars and minimum is 15K dollars and maximum spending score is 99 and minimum is 61 between 1-100 range')
    else:
         st.subheader('This person belongs to  group where maximum annual income 137K dollars and minimum is 69K dollars and maximum spending score is 97 and minimum is 63 between 1-100 range')  