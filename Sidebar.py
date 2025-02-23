# This script will include the details of the sidebar to be displayed in the app

import streamlit as st
from PIL import Image

logo = Image.open("./Images/TheAlternativeLogo.png")

def Sidebar():
    with st.sidebar:
        st.image(logo)
        selection = st.selectbox("Select Section", ["Home Page", "Season 1", "Season 2", "Season 3"])

    return selection