

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model=pickle.load(open('diabetes_model.sav','rb')) 
heart_model=pickle.load(open('heart_disease_model.sav','rb'))

# --- Stylish Background ---
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f6;
        background-image: linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%);
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        color: #3a3a3a;
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        padding: 20px 0;
    }
    .subtitle {
        color: #555;
        font-size: 20px;
        text-align: center;
        padding-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)
  

#Sde bar navigate
with st.sidebar:
    selected=option_menu('Heart & Diabetes Disease Predictive System',
                         ['Heart Disease Prediction',
                          'Diabetes Prediction'],
                         icons=['activity','bag-heart'],
                         default_index=0)
                         
    
if (selected=='Heart Disease Prediction'):
    st.title('Heart Disease Prediction')
    
    st.header("📝 Enter Your Medical Details:")
    col1,col2,col3=st.columns(3)
    with col1:
        age = int( st.text_input('Age'))
        

    with col2:
        sex = int(st.selectbox('Gender', ('Male', 'Female')))
    with col3:
        cp = int(st.selectbox('Chest Pain Type (0-3)', [0, 1, 2, 3]))
    with col1:
        trestbps = int(st.text_input('Resting Blood Pressure'))
    with col2:
        chol = int(st.text_input('Serum Cholesterol (mg/dl)'))
    with col3:
        fbs = int(st.selectbox('Fasting Blood Sugar > 120 mg/dl', [1, 0]))
    with col1:
        restecg = int(st.selectbox('Resting ECG Results (0-2)', [0, 1, 2]))
    with col2:
        thalach = int(st.text_input('Maximum Heart Rate Achieved'))
    with col3:
        exang = int(st.selectbox('Exercise Induced Angina', [1, 0]))
    with col1:
        oldpeak = int(st.text_input('ST Depression Induced by Exercise'))
    with col2:
        slope = int(st.selectbox('Slope of Peak Exercise ST Segment', [0, 1, 2]))
    with col3:
        ca = int(st.selectbox('Number of Major Vessels (0-3)', [0, 1, 2, 3]))
    with col1:
        thal = int(st.selectbox('Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect)', [1, 2, 3]))
    
    outcome=''
    if st.button('🔍 Predict'):
        diagnosis=heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,exang, oldpeak, slope, ca, thal]])
        if (diagnosis[0] == 0):
            outcome='✅ The person does NOT have Heart Disease.'
        else:
            outcome='⚠️ The person HAS Heart Disease!'
        
    if outcome:
        st.subheader('Prediction Result')
        st.success(outcome)
    
    
elif (selected=='Diabetes Prediction'):
    st.title('Diabetes Prediction')
    
    st.header("📝 Enter Your Medical Details:")
    						
    Pregnancies=st.text_input('Enter Number of Pregnancies ')
    Glucose=st.text_input('Glucose Level')
    BloodPressure=st.text_input('BloodPressure Value')
    SkinThickness=st.text_input('SkinThickness Value')
    Insulin=st.text_input('Insulin level')
    BMI=st.text_input('BMI value')
    DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction value')
    Age	=st.text_input('Age	of the person')
    
    outcome2=''
    if st.button('🔍 Predict'):
        diagnosis2=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if (diagnosis2[0] == 0):
            outcome2='✅ The person does NOT have Diabetes Disease.'
        else:
            outcome2='⚠️ The person HAS Dabetes Disease!'
    if outcome2:
        st.subheader('Prediction Result')
        st.success(outcome2)
#if __name__ == '__main__':
 #   main()
    
    

