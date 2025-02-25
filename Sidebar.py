# This script will include the details of the sidebar to be displayed in the app

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

logo = Image.open("./Images/TheAlternativeBaseLogo.png")

def Sidebar():
    st.set_page_config(initial_sidebar_state="expanded")
    with st.sidebar:
        # Header
        st.image(logo)

        # Section Selector
        st.subheader("Historical Results")
        selection = st.selectbox("Select Section", ["Home Page", "Season 1", "Season 2", "Season 3", "All Time Driver Statistics", "All Time Constructor Statistics"])

        # Detailed Page Links
        st.subheader("Detailed Season Pages")

        # Season 3 Link
        link_text = "Season 3"
        link_url = "https://thealternativef124.streamlit.app/"
        st.markdown(f'<a href="{link_url}" target="_blank">{link_text}</a>', unsafe_allow_html=True)

        # Season 4 Link
        link_text = "Season 4 (Coming Soon)"
        link_url = "https://thealternativef1.streamlit.app/"
        st.markdown(f'<a href="{link_url}" target="_blank">{link_text}</a>', unsafe_allow_html=True)

    return selection