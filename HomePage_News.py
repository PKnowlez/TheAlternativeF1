import streamlit as st
from PIL import Image
from streamlit_carousel import carousel

st.markdown(
    """
    <style>
    /* Target the image container within the carousel */
    .st-emotion-cache-1pxn4x7 img {
        width: 100%; 
        height: auto; 
        object-fit: contain; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

def HomePageNews():
    #region Driver Announcements
    driver_announcements = [
        {
            "title": "",
            "text": "",
            "img": "./Images/Alpine_Driver_Post.png"
        },
        {
            "title": "",
            "text": "",
            "img": "./Images/Alpine_Driver_Post.png"
        },
    ]

    carousel(items=driver_announcements, interval=30000)
    st.divider()
    #endregion