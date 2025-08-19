# This script will include the details of the sidebar to be displayed in the app

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

logo = Image.open("./Images/TheAlternativeBaseLogo.png")

def Sidebar():
    with st.sidebar:
        # Header
        st.image(logo)

        # Section Selector
        selection = st.selectbox("Select Section", ["Home Page", "Regulations & Settings", "Season 1", "Season 2", "Season 3", "All Time Driver Statistics", "All Time Constructor Statistics", "All Time Race Results"])

        # Detailed Page Links
        st.subheader("Detailed Season Pages")

        # Season 1 Link
        link_text = "Season 1"
        link_url = "https://thealternatives1.streamlit.app/"
        st.markdown(f'<a href="{link_url}" target="_blank">{link_text}</a>', unsafe_allow_html=True)

        # Season 2 Link
        link_text = "Season 2"
        link_url = "https://thealternatives2.streamlit.app/"
        st.markdown(f'<a href="{link_url}" target="_blank">{link_text}</a>', unsafe_allow_html=True)

        # Season 3 Link
        link_text = "Season 3"
        link_url = "https://thealternatives3.streamlit.app/"
        st.markdown(f'<a href="{link_url}" target="_blank">{link_text}</a>', unsafe_allow_html=True)

        # Season 4 Link
        link_text = "Season 4 (WIP)"
        link_url = "https://thealternatives4.streamlit.app/"
        st.markdown(f'<a href="{link_url}" target="_blank">{link_text}</a>', unsafe_allow_html=True)

    return selection