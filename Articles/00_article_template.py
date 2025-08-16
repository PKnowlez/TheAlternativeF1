import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

image = Image.open("./Article_Images/image.png")

def article():
    date = "DAY 00/00/0000"
    author = "NAME"

    st.subheader('''Title''')
    st.markdown('''Article''')
    st.image(image)
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date} - {author}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()