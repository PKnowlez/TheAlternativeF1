# This function will create the layout for each Season's historical record page

import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import plotly.express as px
import Functions

def SeasonPage(season):

    constructor_line, driver_line, constructor_bar, constructor_totals, driver_bar, driver_totals = \
        Functions.PointTotals(season)

    # Page Title
    season_title = 'Season '+ str(season)
    st.title(season_title)

    # Constructor and Driver Champion callouts
    constructor_name = constructor_totals['Team'].iloc[0]
    st.subheader("Constructor's Champion: " + constructor_name)
    driver_name = driver_totals['Driver'].iloc[0]
    st.subheader("Driver's Champion: " + driver_name)

    # Set display layout for plots
    col1, col2 = st.columns(2)
    with col1:
        with st.popover("Full Constructor's Championship Standings"):
            st.markdown(constructor_totals.to_html(index=False), unsafe_allow_html=True)
    with col2:
        with st.popover("Full Driver's Championship Standings"):
            st.markdown(driver_totals.to_html(index=False), unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        # Display the Team Plot in Streamlit
        st.plotly_chart(constructor_line)
        # Display the Team Bar plot
        st.plotly_chart(constructor_bar)
    with col4:
        # Display the Driver Plot in Streamlit
        st.plotly_chart(driver_line)
        # Display the Driver Bar plot
        st.plotly_chart(driver_bar)