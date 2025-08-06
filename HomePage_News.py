import streamlit as st
from PIL import Image
from streamlit_carousel import carousel

st.markdown(
    """
    <style>
    /* Target the image container within the carousel */
    .stCarousel img {
        width: 100%; /* Make image fill the container width */
        height: auto; /* Maintain the image's aspect ratio */
        object-fit: contain; /* Ensure the image is fully visible without cropping */
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

    carousel(items=driver_announcements, autoplay=True, interval=30000)
    st.divider()
    #endregion