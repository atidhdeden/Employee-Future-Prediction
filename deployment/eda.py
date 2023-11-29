import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
 
 
st.set_page_config(
    page_title = 'Employe Future Prediction - EDA',
    layout = 'wide',
    initial_sidebar_state = 'expanded'
)

def run():
    # Membuat Title
    st.title('Employe Future Prediction')
    st.title('This project aims to predict the tendency of employees to decide to quit or continue working at the company')

    # Membuat sub Header
    st.subheader('Data Exploration')

    # Menambahkan Image
    st.image('https://elearn.id/wp-content/uploads/2020/12/wfo.jpg',
             caption='Employe Future Prediction')
    
    # Menambahkan Deskripsi
    st.write('This page was created by Nurdin Atid H')
    st.write('# Welcome to the Employe Future Prediction page')


    # Membuat garis lurus 
    st.write('---')

    # Magic syntax
    '''
    On this page, the author will carry out a simple exploration,
    The dataset used is the credit_card_default dataset.
    This dataset comes from [kaagle]('https://www.kaggle.com/datasets/tejashvi14/employee-future-prediction')
    '''

    # Show Dataframe
    df_1 = pd.read_csv('employee_clear.csv')
    st.dataframe(df_1)
    # Fungsi untuk mengatur palet warna Seaborn
    def set_seaborn_palette():
        sns.set_palette("muted")
        sns.set_style("darkgrid")

    # Visualisasi untuk setiap kolom
    st.write('### LeaveOrNot (1 = leave and 0 = Not)')
    set_seaborn_palette()
    fig = plt.figure(figsize=(10, 5))
    sns.countplot(x='LeaveOrNot', data=df_1, palette="Set3")
    st.pyplot(fig)

    st.write('### JoiningYear')
    set_seaborn_palette()
    fig = plt.figure(figsize=(10, 5))
    sns.countplot(x='JoiningYear', data=df_1, palette="Set3")
    st.pyplot(fig)

        #Membuat Histogram berdasarkan input user
    st.write('### Histogram based on User Input')
    pilihan = st.selectbox('select column :', ('Education', 'JoiningYear', 'City', 'PaymentTier', 'Age', 'Gender',
       'EverBenched', 'ExperienceInCurrentDomain', 'LeaveOrNot'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(df_1[pilihan],bins=30,kde=True)
    st.pyplot(fig)

    #membuat plotly plot
    st.write('### Plotly LeaveOrNot vs Gender')
    fig=px.scatter(df_1,x='LeaveOrNot', y='JoiningYear', hover_data=['LeaveOrNot', 'JoiningYear'])
    st.plotly_chart(fig)

if __name__== '__main__': 
    run()

