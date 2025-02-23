# The functions within this file are universal for TheAlternativeF1.py
#   PointsTotals:   function that calculates and returns the sum of points
#                   for both drivers and constructors over the course of 
#                   one season
#   TotalsLineChart:    function generates a line chart based on driver
#                       or team points over time across a specific season
#   TotalsBarChart:     function generates a bar chart based on driver
#                       or team points totals from a specific season

import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import plotly.express as px

# Global variables for all of the functions
place_suffix = "Place"
qualifying_suffix = "Qualifying"
fastestlap_suffix = "FastestLap" 
points_suffix = "Points"
file = "The_Alternative_F1.xlsx"
team_colors = {
        'Alpine': 'hotpink', 
        'Aston Martin': 'teal',
        'Ferrari': 'red',
        'McLaren': 'darkorange',
        'Red Bull': 'darkblue',
        'VCARB': 'blue',
        'AlphaTauri': 'darkgray',
        'Alfa Romeo': 'darkred',
        'Mercedes': 'silver',
        'Haas': 'gray',
    }

def TotalsLineChart(totals,colors,chart_title,races):
    # Input Variables
    #   totals: the constructor or driver totals dataframe
    #   colors: the colors associated with the drivers or constructors
    #   chart_title: title of the chart
    #   races: list of races to be plotted against

    # Add a new column of zeros at the beginning
    totals.insert(0, 'Start', 0)  
    totals = totals.T
    races.insert(0, 'Start') 

    # Create Plotly figure
    fig1 = go.Figure()

    for team in totals.columns:
        fig1.add_trace(go.Scatter(x=races,
                                y=totals[team], 
                                mode='lines+markers',
                                name=team, 
                                line=dict(color=colors.get(team))))

    fig1.update_layout(
        xaxis_title="Race",
        yaxis_title="Total Points",
        title=chart_title,
        hovermode="x unified"
    )

    return fig1

def TotalsBarChart(totals, colors, chart_title, tORd):
    # Input Variables
    #   totals: the constructor or driver totals dataframe
    #   colors: the colors associated with the drivers or constructors
    #   chart_title: title of the chart
    #   tORd: Team or Driver string

    # Sort the data
    last_col = totals.columns[-1]
    sorted_totals = totals.sort_values(last_col, ascending=False)
    sorted_totals = sorted_totals.reset_index()

    totals_for_chart = pd.DataFrame({
        tORd: sorted_totals[tORd],
        'Points': [f"{points:.1f}" for points in sorted_totals[last_col]],
    })

    # Plot the chart
    fig = px.bar(
        x=totals_for_chart[tORd],
        y=totals_for_chart['Points'],
        title=chart_title,
    )

    # Assign colors to the chart
    if tORd == 'Team':
        fig.update_traces(marker_color=[colors.get(team) for team in totals_for_chart[tORd]])
        x_title = "Constructor"
    else:
        fig.update_traces(marker_color=[colors.get(driver) for driver in totals_for_chart[tORd]])
        x_title = "Driver"

    # Update the axis titles
    fig.update_xaxes(title_text=x_title)
    fig.update_yaxes(title_text="Points")

    df_sorted = totals_for_chart.sort_values('Points', ascending=False)
    df_sorted.reset_index(drop=True, inplace=True)
    df_sorted['Place'] = df_sorted.index + 1

    cols = ['Place'] + [col for col in df_sorted if col != 'Place'] # Create new column order
    df_sorted = df_sorted[cols] # Reindex

    return fig, df_sorted  

def PointTotals(season):
    # Input variables
    #   season: numeric value of the season to be calculated

    # Read in the appropriate sheet for the selected season
    sheet = "Season"+str(season)
    df = pd.read_excel(file,sheet_name=sheet)

    # Read in the list of races from the selected season
    sheet = "S"+str(season)+"Schedule"
    schedule = pd.read_excel(file,sheet_name=sheet)

    # Loop through the schedule and create lists for each global suffix
    races = []
    race_place = []
    race_qualifying = []
    race_fastestlap = []
    race_points = []
    for i in range(len(schedule)):
        race_name = schedule['Race'].iloc[i]
        races.append(race_name)
        race_place.append(race_name+place_suffix)
        race_qualifying.append(race_name+qualifying_suffix)
        race_fastestlap.append(race_name+fastestlap_suffix)
        race_points.append(race_name+points_suffix)

    team_race_totals = pd.DataFrame([]) 
    for i in range(len(race_points)):
        if i == 0:
            team_race_totals[race_points[i]] = df.groupby('Team')[race_points[i]].sum()
        else:
            team_race_totals[race_points[i]] = df.groupby('Team')[race_points[i]].sum() \
                                                    + team_race_totals[race_points[i-1]]

    driver_race_totals = pd.DataFrame([])
    for i in range(len(race_points)):
        if i == 0:
            driver_race_totals[race_points[i]] = df.groupby('Driver')[race_points[i]].sum()
        else:
            driver_race_totals[race_points[i]] = df.groupby('Driver')[race_points[i]].sum() \
                                                    + driver_race_totals[race_points[i-1]]


    # Create the driver_colors dictionary
    driver_colors = {}
    for index, row in df.iterrows():
        driver = row['Driver']
        team = row['Team']
        driver_colors[driver] = team_colors.get(team)

    # Create line chart plots      
    constructor_line = TotalsLineChart(team_race_totals,team_colors,"Constructor's Championship",races)
    driver_line = TotalsLineChart(driver_race_totals,driver_colors,"Driver's Championship",races)

    # Create bar chart plots
    constructor_bar, constructor_totals = TotalsBarChart(team_race_totals,team_colors,"Constructor's Championship",'Team')
    driver_bar, driver_totals = TotalsBarChart(driver_race_totals,driver_colors,"Driver's Championship",'Driver')

    # Set Display Layout
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


    return constructor_line, driver_line, constructor_bar, driver_bar