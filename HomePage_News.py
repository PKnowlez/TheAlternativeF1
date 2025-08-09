import streamlit as st
from PIL import Image
from streamlit_carousel import carousel

def HomePageNews():
    #region Latest News
    latest_news = [
        {
            "title": "",
            "text": "",
            "img": "./Images/Driver_Lineup.png"
        },
    ]
    
    carousel(items=latest_news, interval=20000)
    st.divider()
    #endregion

    # ----------------------------------------------------------------------------------------------------------
    # "Show More/Less" button 
    if not st.session_state.show_all_content:
        if st.button('Show More'):
            st.session_state.show_all_content = True
            st.rerun()  # Rerun the app to show everything
    else: 
        if st.button('Show Less'):
            st.session_state.show_all_content = False
            st.rerun()

    if st.session_state.show_all_content:
    #region Driver Announcements
        driver_announcements = [
            {
                "title": "",
                "text": "",
                "img": "./Images/Driver_Lineup.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Alpine_Driver_Post.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/McLaren_Driver_Post.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Red_Bull_Driver_Post.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/VCARB_Driver_Post.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Intern_1.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Intern_2.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Aston_Martin_Driver_Post.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Ferrari_Driver_Post.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Mercedes_Driver_Post.png"
            },
        ]

        carousel(items=driver_announcements, interval=20000)
        st.divider()
        #endregion