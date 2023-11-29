import streamlit as st
import pandas as pd
import pickle
import json
import numpy as np
import seaborn as sns
 
# Load trained model, scaler, and column information
with open('pipe_knn.pkl', 'rb') as file_1:
    pipe_knn = pickle.load(file_1)

def run():
    # Membuat form
    with st.form(key='LeaveOrNot'):
        Education = st.selectbox('Education', ('Bachelors', 'Masters', 'PHD'))
        JoiningYear = st.selectbox('joined the company on years', ('2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'), 5, help='The year you joined the company')
        City = st.selectbox('City', ('Bangalore', 'Pune', 'New Delhi'))
        PaymentTier = st.selectbox('PaymentTier', ('1', '2', '3'), help = 'PAYMENT TIER: 1: HIGHEST 2: MID LEVEL 3:LOWEST')
        Age = st.number_input('Age', min_value=18, max_value=60, value=25, step=1, help='Age in years')
        Gender = st.selectbox('Gender', ('male', 'female'))
        EverBenched = st.selectbox('EverBenched', ('No', 'Yes'), help='EVER KEPT OUT OF PROJECTS FOR 1 MONTH OR MORE')
        ExperienceInCurrentDomain = st.selectbox('ExperienceInCurrentDomain', ('0', '1', '2', '3', '4', '5', '6', '7'), 5, help='EXPERIENCE IN CURRENT FIELD')

        submitted = st.form_submit_button('Predict')

    # Buat dataframe dengan data yang dimasukkan oleh pengguna
    data_inf = {
        'Education': Education,
        'JoiningYear': JoiningYear,
        'City': City,
        'PaymentTier': PaymentTier,
        'Age': Age,
        'Gender': Gender,
        'EverBenched': EverBenched,
        'ExperienceInCurrentDomain': ExperienceInCurrentDomain,
         }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    y_pred_inf = None  # Initialize y_pred_inf with a default value

    if submitted:
        # Predict new data inference using knn model
        y_pred_inf = pipe_knn.predict(data_inf)

    # Display Result
    if y_pred_inf is not None:
        if y_pred_inf == 0:
            st.write(f'The prediction results of Employe Future Prediction are {y_pred_inf} which means continuing to work at the company')
        else:
            st.write(f'The prediction results of Employe Future Prediction are {y_pred_inf} which means leaving the company')
       

if __name__ == '__main__':
    run()

