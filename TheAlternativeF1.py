# This is the main script for this streamlit site which will include calls
# for each tab, section, or other portion of the app. This app will serve
# as the main landing site for The Alternative's F1 seasons.

import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import plotly.express as px
import Sidebar, Functions, HomePage, Regulations, Season, ConstructorAllTime, DriverAllTime, RacesAllTime
from Season1.F1Season1 import Season1
from Season2.F1Season2 import Season2
from Season3.F1Season3 import Season3
from Season4.F1Season4 import Season4

## ----- App Format ----- ##
st.set_page_config(page_title="The Alternative F1", initial_sidebar_state="expanded", layout="wide")

APP_NAME = "The Alternative F1"

st.markdown(
    f"""
    <meta name="application-name" content="{APP_NAME}">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="{APP_NAME}">
    <meta name="mobile-web-app-capable" content="yes">
    """,
    unsafe_allow_html=True
)

selection = Sidebar.Sidebar()
NumSeasons = 4

if selection == "Home Page":
    HomePage.HomePage()
# elif selection == "Regulations & Settings":
#     Regulations.RegulationsSettings()
elif selection == "Season 1":
    Season1()
elif selection == "Season 2":
    Season2()
elif selection == "Season 3":
    Season3()
elif selection == "Season 4":
    Season4()
# elif selection == "All Time Driver Statistics":
#     DriverAllTime.DriverStats(NumSeasons,'Driver')
# elif selection == "All Time Constructor Statistics":
#     ConstructorAllTime.ConstructorStats(NumSeasons,'Team')
# elif selection == "All Time Race Results":
#     RacesAllTime.RaceStats(NumSeasons)    
else:
    st.subheader("Welcome to The Alternative's F1 League")

