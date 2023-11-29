import streamlit as st
import eda
import prediction
import seaborn as sns

navigation = st.sidebar.selectbox('Pilih Halaman :', ('EDA', 'Predict Default Payment Next Month'))

if navigation == 'EDA':
    eda.run()
else:
    prediction.run()