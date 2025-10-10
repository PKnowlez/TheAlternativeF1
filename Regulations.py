import streamlit as st
import HomePage_Regulations, HomePage_Settings

def RegulationsSettings():
    st.header('League Regulations and Settings')

    tabs = st.tabs([
        "Current League Regulations",
        "Current League Settings"
    ])

    with tabs[0]:
        HomePage_Regulations.HomePageRegulations()

    with tabs[1]:
        HomePage_Settings.HomePageSettings()