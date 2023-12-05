import streamlit as st
from PIL import Image
import eda
import model

st.sidebar.title("Menu")
page = st.sidebar.selectbox(label='Select Page', options=['Home Page', 'EDA', 'Model'])

if page == 'Home Page':
    st.header('House Price Prediction')
    img = Image.open('RumahM2.jpg')
    st.image(img)
    st.write('')
    st.write('Project House Price Predict')
    st.write("Objective : Project ini dibuat guna mengevaluasi konsep Machine Learning")
    st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        <ul> 
            <li>Mampu memahami konsep Machine Learning secara keseluruhan.</li>
            <li>Mampu mempersiapkan data untuk digunakan dalam model Supervised Learning (Classification atau Regression).</li>
            <li>Mampu mengimplementasikan Supervised Learning (Classification atau Regression) dengan data yang dipilih.</li>
            <li>Mampu melakukan Hyperparameter Tuning dan Model Improvement.</li>
            <li>Mampu melakukan Model Deployment.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True)
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('Pertumbuhan ekonomi yang pesat, urbanisasi, dan peningkatan pendapatan masyarakat telah memberikan dorongan signifikan bagi industri properti di berbagai belahan dunia. Bisnis properti mencakup segala aspek, mulai dari pembangunan perumahan, komersial, hingga properti industri, yang semuanya memiliki dampak signifikan terhadap ekonomi, masyarakat, dan lingkungan.')

    with st.expander("Problem Statement"):
            st.caption('Pasar properti, memberikan peluang menarik bagi analis data untuk menganalisis dan memprediksi ke mana arah harga properti. Memprediksi harga properti menjadi semakin penting dan berguna. Harga properti merupakan indikator yang baik untuk kondisi pasar secara keseluruhan dan kesehatan ekonomi suatu negara. Semoga saja model ini dapat membantu agen properti dan pembeli untuk mendapat perkiraan harga yang akurat.')

elif page == 'EDA':
    eda.run()
else:
    model.run()