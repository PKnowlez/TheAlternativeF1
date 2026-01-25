# This script will include the details of the sidebar to be displayed in the app

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

logo = Image.open("./Images/The Alternative F1 NEW Logo.png")

def Sidebar():
    with st.sidebar:
        # Header
        st.image(logo)

        # Section Selector
        selection = st.selectbox("Page Selection", ["Home Page", "Regulations & Settings", "Season 1", "Season 2", "Season 3", "Season 4", "All Time Driver Statistics", "All Time Constructor Statistics", "All Time Race Results"])

    return selection