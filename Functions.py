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
import Plotting

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
    constructor_line = Plotting.TotalsLineChart(team_race_totals,team_colors,"Constructor's Championship",races)
    driver_line = Plotting.TotalsLineChart(driver_race_totals,driver_colors,"Driver's Championship",races)

    # Create bar chart plots
    constructor_bar, constructor_totals = Plotting.TotalsBarChart(team_race_totals,team_colors,"Constructor's Championship",'Team')
    driver_bar, driver_totals = Plotting.TotalsBarChart(driver_race_totals,driver_colors,"Driver's Championship",'Driver')

    return constructor_line, driver_line, constructor_bar, constructor_totals, driver_bar, driver_totals