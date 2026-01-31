# This script will define the Home Page section of the new application

import streamlit as st
import HomePage_Regulations, HomePage_Settings, ConstructorAllTime, DriverAllTime, RacesAllTime
from Season4 import Tab0_LeagueNews, Tab1_Standings
from PIL import Image

logo = Image.open("./Images/The Alternative F1 NEW Logo.png")
NumSeasons = 4

def HomePage():
    st.image(logo)

    tabs = st.tabs([
        "News",
        "Regulations",
        "Settings",
        "All Time Driver Stats",
        "All Time Constructor Stats",
        "All Time Race Results"
    ])

    with tabs[0]:
        Tab0_LeagueNews.Tab0()

    with tabs[1]:
        HomePage_Regulations.HomePageRegulations()
        
    with tabs[2]:
        HomePage_Settings.HomePageSettings()

    with tabs[3]:
        DriverAllTime.DriverStats(NumSeasons,'Driver')
    
    with tabs[4]:
        ConstructorAllTime.ConstructorStats(NumSeasons,'Team')

    with tabs[5]:
        RacesAllTime.RaceStats(NumSeasons)