import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def run():
    st.title('Welcome to Explaration Data Analysis')

    df= pd.read_csv(r'House_Price_Predic.csv')

    st.table(df.head(5))

    st.title('Data Visualisasi')

    image = Image.open('EDA1.png')
    st.image(image, caption='Bagaimana Distribusi Harga Pada Data Penjualan?')
    with st.expander('Explanation'):
        st.caption('Kesimpulan, Terlihat harga penjualan rumah di Washington bersifat skewed.')

    image = Image.open('EDA2.png')
    st.image(image, caption='Apakah Rumah Yang Memiliki View Pantai, Memiliki Harga Yang Lebih Tinggi?')
    with st.expander('Explanation'):
        st.caption('Kesimpulan, Rumah dengan view pantai biasanya harganya jauh lebih tinggi dibanding yang tidak memiliki view pantai.')

    image = Image.open('EDA3.png')
    st.image(image, caption='Adakah Hubungan Antara Tingkat Rumah Dengan Harga?')
    with st.expander('Explanation'):
        st.caption('Kesimpulan. Terlihat dari ada rumah yang tingkatannya rendah hanya 1 laintai, namun harganya paling mahal , mungkin ini karena rumah tersebut mewah dan sangat luas. Sedangkan ada rumah yang tinggi , namun harganya rendah , mungkin ini karena rumah tersebut tinggi namun sempit dan tidak nyaman dihuni.')

    image = Image.open('EDA4.png')
    st.image(image, caption='3 Kota Teratas Yang Menjual Harga Rumah Dengan Harga Tinggi')
    with st.expander('Explanation'):
        st.caption('Kesimpulan, Bisa dibilang di daerah tersebut merupakan rumah-rumah mewah dan bagus.')

    image = Image.open('EDA5.png')
    st.image(image, caption='Apakah ada Pengaruh Usia Rumah dengan Harga?')
    with st.expander('Explanation'):
        st.caption('Kesimpulan, Usia rumah tidak menjamin harga rumah. Bisa saja rumah yang sudah tua, namun karena nilai keaslian dan vintage nya menjadi lebih mahal.')

    image = Image.open('EDA6.png')
    st.image(image, caption='Apakah Rumah Yang Pernah Direnovasi Memiliki Tingkat Kondisi Yang Lebih Baik?')
    with st.expander('Explanation'):
        st.caption('Kesimpulan, Rumah yang pernah direnovasi memiliki kondisi yang lebih baik. Namun begitu perbedaan kondisinya tidak terlalu jauh dengan yang tidak pernah direnovasi.')

    image = Image.open('EDA7.png')
    st.image(image, caption='Adakah Hubungan Antara Luas Ruang Tamu Dengan Harga?')
    with st.expander('Explanation'):
        st.caption('Kesimpulan, Dari scatter plot diatas dapat dilihat bahwa ada hubungan dengan trend positif antara harga rumah dengan luas ruang tamu, Artinya semakin besar luas ruang tamu , maka rumahnya juga akan semakin mahal.')
