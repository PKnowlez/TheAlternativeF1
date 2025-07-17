# This script will define the Home Page section of the new application

import streamlit as st
import HomePage_News, HomePage_Regulations, HomePage_Settings

def HomePage():
    st.subheader("The Alternative F1 League")
    tabs = st.tabs([
        "General League News",
        "Current League Rules",
        "Current League Settings"
    ])

    with tabs[0]:
        HomePage_News.HomePageNews()

    with tabs[1]:
        HomePage_Regulations.HomePageRegulations()
        
    with tabs[2]:
        HomePage_Settings.HomePageSettings()