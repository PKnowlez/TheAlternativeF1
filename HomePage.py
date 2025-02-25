# This script will define the Home Page section of the new application

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

wip = Image.open("./Images/WIP.jpeg")

def HomePage():
    st.subheader("The Alternative F1 League")
    st.image(wip)
