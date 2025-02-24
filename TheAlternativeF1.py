# This is the main script for this streamlit site which will include calls
# for each tab, section, or other portion of the app. This app will serve
# as the main landing site for The Alternative's F1 seasons.

import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import plotly.express as px
import Sidebar, Functions, HomePage, Season

## ----- App Format ----- ##
st.set_page_config(layout="wide") 

selection = Sidebar.Sidebar()

if selection == "Home Page":
    HomePage.HomePage()
elif selection == "Season 1":
    season = 1
    Season.SeasonPage(season)
elif selection == "Season 2":
    season = 2
    Season.SeasonPage(season)
elif selection == "Season 3":
    season = 3
    Season.SeasonPage(season)
else:
    st.subheader("Welcome to The Alternative's F1 League")

