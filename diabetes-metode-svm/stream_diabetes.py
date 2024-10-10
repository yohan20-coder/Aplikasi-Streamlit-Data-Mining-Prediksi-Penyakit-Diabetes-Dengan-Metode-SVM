import pickle
import streamlit as st

#membaca Model

diabetes_model = pickle.load(open('dieb_model.sav', 'rb'))

#judul web

st.title('Data Mining Prediksi Diabetes')

col1, col2 = st.columns(2)

with col1 :
    Pregnancies = st.text_input('Input Nilai Pregnancies')

with col2 :
    Glucose = st.text_input('Input Nilai Glucose')
    
with col1 :
    BloodPressure = st.text_input('Input Nilai BloodPressure')

with col2 :
    SkinThickness = st.text_input('Input Nilai SkinThickness')

with col1 :
    Insulin = st.text_input('Input Nilai Insulin')

with col2 :
    BMI = st.text_input('Input Nilai BMI')

with col1 :
    DiabetesPedigreeFunction = st.text_input('Input Nilai DiabetesPedigreeFunction')

with col2 :
    Age = st.text_input('Input Nilai Age')

#code prediksi
diab_diagnosis = ''

#membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_prediction[0] == 1):
        diab_diagnosis = 'Pasien terkena Diabetes'
    else:
        diab_diagnosis = 'Pasien tidak terkena Diabetes'
st.success(diab_diagnosis)
