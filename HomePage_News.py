import streamlit as st
from PIL import Image
from streamlit_carousel import carousel

def HomePageNews():
    #region Driver Announcements
    driver_announcements = [
        {
            "title": "",
            "text": "",
            "img": "./Images/Alpine_Driver_Post.png"
        },
    ]

    carousel(driver_announcements)
    st.divider()
    #endregion