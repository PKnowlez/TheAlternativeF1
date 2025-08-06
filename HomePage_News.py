import streamlit as st
from PIL import Image
from streamlit_carousel import carousel

st.markdown(
    """
    <style>
    /* Target the container of the entire carousel */
    .stCarousel {
        height: auto !important; /* Allow the container to adjust to the image height */
        overflow: visible !important; /* Ensure content is not cut off */
    }

    /* Target the image container within the carousel */
    .stCarousel img {
        width: 100%; /* Make image fill the container width */
        height: auto; /* Maintain the image's aspect ratio based on width */
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

    carousel(items=driver_announcements, interval=30000)
    st.divider()
    #endregion