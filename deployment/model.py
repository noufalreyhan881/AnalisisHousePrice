import streamlit as st
import pickle
import pandas as pd

def run():
    st.header('Welcome to Model Section')
    with open('final_pipe1.pkl', 'rb') as file_1:
        all_process = pickle.load(file_1)

    view = st.number_input('Please enter view value', min_value=1, max_value=4,step=1)
    bedrooms = st.number_input('Please enter bedroom count', min_value=1, max_value=9,step=1)
    bathrooms = st.number_input('Please enter number of bathrooms in the house', min_value=1, max_value=8,step=1)
    sqft_living =st.number_input('Please enter number of bathrooms in the house', min_value=1, max_value=12,step=1)
    floors = st.number_input('Please enter view floor count', min_value=1, max_value=4,step=1)
    sqft_above = st.number_input('Please enter number of sqft_above', min_value=0, max_value=5000,step=1000)
    sqft_basement = st.number_input('Please enter number of sqft_basement', min_value=0, max_value=5000,step=1000)
    condition = st.number_input('Please enter condition value', min_value=1, max_value=5,step=1)
    area =st.number_input('Please area number', min_value=1, max_value=8,step=1)
    
    data_inf = pd.DataFrame({
        'view' : view,
        'bedrooms': bedrooms,
        'bathrooms' : bathrooms,
        'sqft_living': sqft_living,
        'floors': floors,
        'sqft_above': sqft_above,
        'sqft_basement': sqft_basement,
        'condition' : condition,
        'area': area        
    }, index =[0])

    st.table(data_inf)

    if st.button(label='predict'):
        y_pred_inf = all_process.predict(data_inf)
        st.write("Hasil Prediksi:", y_pred_inf)