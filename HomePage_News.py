import streamlit as st
from PIL import Image
from streamlit_carousel import carousel

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    /* Target the image container within the carousel with a higher specificity */
    .stCarousel > div > div > div > a > img {
        width: 100%;
        height: 100%;
        object-fit: contain; /* Ensures the entire image is visible */
        object-position: center; /* Centers the image within the container */
    }
    /* Ensure the carousel container has a defined height to allow object-fit to work */
    .stCarousel > div > div {
        height: 400px; /* Adjust this height as needed */
        max-height: 400px; /* Prevents container from growing too large */
        display: flex;
        align-items: center;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def HomePageNews():
    # Load and resize images to a consistent size for better carousel display
    # This is a good practice to ensure all images have the same dimensions
    # and prevent layout shifts.
    img1 = Image.open("./Images/Alpine_Driver_Post.png")
    img1 = img1.resize((800, 400)) # Example resize, adjust as needed

    driver_announcements = [
        {
            "title": "Alpine Driver Announcement",
            "text": "Alpine Driver Announcement",
            "img": img1
        },
        {
            "title": "",
            "text": "",
            "img": img1
        },
    ]

    carousel(items=driver_announcements, interval=30000)
    st.divider()