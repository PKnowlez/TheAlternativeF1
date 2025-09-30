import streamlit as st
import plotly.express as px
from PIL import Image
import pandas as pd

def graph():
    st.subheader('''Season 4 Constructor's Power Rankings''')
    df = pd.read_excel("The Alternative F1 Season 4 Power Rankings (Responses).xlsx", sheet_name="Final Ranking")
    df_for_plotting = df.set_index('Race')

    team_colors = {
        'Alpine': 'hotpink', 
        'Aston Martin': 'teal',
        'Ferrari': 'red',
        'McLaren': 'darkorange',
        'Red Bull': 'darkblue',
        'VCARB': 'blue',
        'AlphaTauri': 'LightSlateGray',
        'Alfa Romeo': 'Maroon',
        'Mercedes': 'black',
        'Haas': 'gray',
    } 

    # --- Create the Plotly figure ---
    fig = px.line(df_for_plotting, 
                  x=df_for_plotting.index, 
                  y=df_for_plotting.columns,
                  markers=True,
                  color_discrete_map=team_colors,
                  labels={'variable': 'Team', 'value': 'Place'}) # <-- ADD THIS LINE

    min_rank = int(df_for_plotting.min().min())
    max_rank = int(df_for_plotting.max().max())
    
    tick_values = list(range(min_rank, max_rank + 1))
    tick_labels = []
    for rank in tick_values:
        if 11 <= rank % 100 <= 13:
            suffix = 'th'
        else:
            suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(rank % 10, 'th')
        tick_labels.append(f"{rank}{suffix}")

    fig.update_yaxes(
        title_text="Ranking",
        autorange="reversed", # Inverts the axis
        tickvals=tick_values, # Sets the position of the ticks
        ticktext=tick_labels  # Sets the text for the ticks
    )

    fig.update_xaxes(
        title_text="Race",
        range=[df_for_plotting.index[0], df_for_plotting.index[-1]]
    )

    fig.update_layout(legend_title_text='')
    
    st.plotly_chart(fig, use_container_width=True)

def preseason_article():
    date = "Tuesday 09/30/2025"
    author = "Patrick"

    st.markdown('''**Preseason Power Rankings**''')
    st.markdown('''
                While the standings are useful, they do not tell the whole story of which teams are trending up throughout the season even without big wins or flashy moments.
                
                To kick off the season, the FIA and the race stewards have ranked each team. Initial rankings positioned teams where they finished last season. From there, the results of the preseason race and a few other factors shuffled the order a bit. Not much changed for our top three teams from last season, however Mercedes and Aston Martin both had strong performances, leading to minor shifts in the lower power rankings.
                
                As the season progresses, check back here for more updates on the power rankings.
                ''')
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date} - {author}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()