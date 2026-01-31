import streamlit as st
from PIL import Image

def Sidebar():
    with st.sidebar:
        logo = Image.open("./Images/The Alternative F1 NEW Logo.png")
        st.image(logo)
        selection = st.selectbox("Page Selection", [
            "Home Page", "Season 1", "Season 2", "Season 3", "Season 4"
        ])

    return selection