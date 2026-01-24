import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import math
from PIL import Image
from Season3.Tab0_LeagueNews import Tab0
from Season3.Tab1_Standings import Tab1
from Season3.Tab2_RaceResults import Tab2
from Season3.Tab3_ConstructorStatistics import Tab3
from Season3.Tab4_DriverStatistics import Tab4
from Season3.Tab5_DriverComparison import Tab5
from Season3.Tab6_RaceSchedule import Tab6
from Season3.Calculations import Calculations
from Season3.Tab7_DriverBios import Tab7

def Season3():
    # Calculations
    team_race_totals,driver_race_totals,df,races,team_colors,fig1,fig2,race_place,race_points,index_x, \
    new_df,new_df_FL,new_df_Q,new_df_Place,races_points_only,drivers_total_points,driver_colors \
        = Calculations()

    ## ----- App Format ----- ##
    st.set_page_config(layout="wide") 

    # Header
    logo = Image.open("./Season3/Images/TheAlternativeLogo.png")
    st.image(logo)

    # Declare Tabs
    tabs = st.tabs([
        "League News",
        "Standings",
        "Race Results",
        "Constructor Statistics",
        "Driver Statistics",
        "Driver Bios",
        "Driver Comparisons",
        "Race Schedule",
        ])

    # League News
    with tabs[0]:
        Tab0()

    # Standings
    with tabs[1]:
        team_df,team_races_points_only,drivers_points_df,colors_driver_team,colors_driver_df \
            = Tab1(team_race_totals,driver_race_totals,df,races,team_colors,fig1,fig2,new_df,
                                drivers_total_points,driver_colors)

    # Race Results
    with tabs[2]:
        Tab2(races,df,race_place,race_points)

    # Constructor Statistics    
    with tabs[3]:
        colors = Tab3(team_df,team_races_points_only,index_x,drivers_points_df,colors_driver_team,colors_driver_df)

    # Driver Statistics
    with tabs[4]:
        new_df,average_changed,average_qualifying,average_place \
            = Tab4(colors,index_x,new_df,new_df_FL,new_df_Q,new_df_Place,races_points_only)
        
    # Driver Bios
    with tabs[5]:
        Tab7(team_df,drivers_points_df)

    # Driver Comparisons
    with tabs[6]:
        Tab5(new_df,average_changed,drivers_total_points,average_qualifying,average_place)

    # Race Schedule  
    with tabs[7]:
        Tab6()