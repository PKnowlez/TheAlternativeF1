import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import math
from PIL import Image
from Season4.Tab0_LeagueNews import Tab0
from Season4.Tab1_Standings import Tab1
from Season4.Tab2_RaceResults import Tab2
from Season4.Tab3_ConstructorStatistics import Tab3
from Season4.Tab4_DriverStatistics import Tab4
from Season4.Tab5_DriverComparison import Tab5
from Season4.Tab6_RaceSchedule import Tab6
from Season4.Calculations import Calculations

def Season4():
    # Calculations
    team_race_totals,driver_race_totals,df,races,team_colors,fig1,fig2,fig3,race_place,race_points,index_x, \
    new_df,new_df_FL,new_df_DOTD,new_df_MOT,new_df_Q,new_df_Place,races_points_only,drivers_total_points,driver_colors,rookies,new_df_CD \
        = Calculations()

    ## ----- App Format ----- ##
    st.set_page_config(layout="wide") 

    # Header
    logo = Image.open("./Season4/Images/TheAlternativeLogo.png")
    st.image(logo)

    # Declare Tabs
    tabs = st.tabs([
        "League News",
        "Standings",
        "Race Results",
        "Constructor Statistics",
        "Driver Statistics",
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
        colors = Tab3(team_df,team_races_points_only,index_x,
                                                drivers_points_df,colors_driver_team,colors_driver_df)

    # Driver Statistics
    with tabs[4]:
        new_df,average_changed,average_qualifying,average_place \
            = Tab4(colors,index_x,new_df,new_df_FL,new_df_DOTD,new_df_MOT,new_df_Q,new_df_Place,races_points_only,new_df_CD)

    # Driver Comparisons
    with tabs[5]:
        Tab5(new_df,average_changed,drivers_total_points,average_qualifying,average_place,fig3,rookies)

    # Race Schedule  
    with tabs[6]:
        Tab6()