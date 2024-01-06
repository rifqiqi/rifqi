import pickle
import streamlit as st

# membaca model
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

#judul web
st.title ('Data Mining Prediksi Diabetes')
col1, col2, = st.columns(2)
with col1:
    Pregnancies = st.text_input('input nilain Pregnancies')
with col1:
    Glucose = st.text_input('input nilain Glucose')
with col1:
    BloodPressure = st.text_input('input nilain Blood Presure')
with col1:
    SkinThickness = st.text_input('input nilain Skin Thickness')
with col2:
    Insulin = st.text_input('input nilain Insulin')
with col2:
    BMI = st.text_input('input nilain BMI')
with col2:
    DiabetesPedigreeFunction = st.text_input('input nilain Diabetes Pedigree Function')
with col2:
    Age = st.text_input('input nilain Age')

#code untuk prediksi
diab_diagnosis =''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

    if(diab_prediction [0] == 1):
        diab_diagnosis = 'pasien terkena diabetes !!!'
    else:
        diab_diagnosis = 'pasien tidak terkena diabetes'
    st.success(diab_diagnosis)