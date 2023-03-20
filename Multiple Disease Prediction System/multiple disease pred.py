# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 13:06:16 2023

@author: Ankit
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


diabetes_model = pickle.load(open('D:/Multiple Disease Prediction System/saved models/diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('D:/Multiple Disease Prediction System/saved models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('D:/Multiple Disease Prediction System/saved models/parkinsons_model.sav','rb'))

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System using ML',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           
                           icons = ['activity','heart','person'],
                           
                           default_index = 0)
    
#diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
        
    with col2:
        Insulin = st.text_input('Insulin Level')
        
    with col3:
        BMI = st.text_input('BMI value')
   
    with col1:
        DiabetesPredigreeFunction = st.text_input('Diabetes Predigree Finction value')
    
    with col2:
        Age = st.text_input('Age of the person')
    
    
    #code for prediction 
    diab_dignosis = ''
    
    #creeting a button for prediction 
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPredigreeFunction, Age]])
        
        if (diab_prediction[0]==1):
            diab_dignosis = 'The Person is Diabetic'
            
        else:
            diab_dignosis = 'The person is Not Diabetes'
            
    st.success(diab_dignosis)
if (selected == 'Heart Disease Prediction'):

    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
    
    with col3:
        cp = st.text_input('Chest Pain Type')
        
    with col1:
        testbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestrol in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
   
    with col1:
        restcg = st.text_input('Resting Electrocardiographic results')
    
    with col2:
        Age = st.text_input('Age of the person')
    
    
    #code for prediction 
    diab_dignosis = ''
    
    #creeting a button for prediction 
    
    if st.button('Heart Disease Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPredigreeFunction, Age]])
        
        if (diab_prediction[0]==1):
            diab_dignosis = 'The Person is Heart Disease'
            
        else:
            diab_dignosis = 'The person is Not Heart Diabetes'
            
    st.success(diab_dignosis)
    
        

if (selected == 'Parkinsons Prediction'):
    
        st.title('Parkinsons Prediction using ML')
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            fo = st.text_input('MDVP:Fo(Hz)')
            
        with col2:
            fhi = st.text_input('MDVP:Fhi(Hz)')
        
        with col3:
            flo = st.text_input('MDVP:Flo(Hz)')
            
        with col4:
            Jitter_percent = st.text_input('MDVP:Jitter(%)')
            
        with col5:
            Jitter_Abs = st.text_input('MDVP:Jitter(Abs')
            
   
        
    
        
        #code for prediction 
        diab_dignosis = ''
        
        #creeting a button for prediction 
        
        if st.button('Heart Disease Test Result'):
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPredigreeFunction, Age]])
            
            if (diab_prediction[0]==1):
                diab_dignosis = 'The Person is Heart Disease'
                
            else:
                diab_dignosis = 'The person is Not Heart Diabetes'
                
        st.success(diab_dignosis)
        
           
 