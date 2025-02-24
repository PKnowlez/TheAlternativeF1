import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import plotly.express as px

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
        'Points': sorted_totals[last_col],  # Keep 'Points' as numeric
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