import streamlit as st
import plotly.express as px
from PIL import Image
import pandas as pd
import base64
from pathlib import Path

# Helper function to encode local images to base64
def image_to_base64(image_path):
    """Reads an image file and returns a base64 encoded string."""
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{encoded_string}"

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

    logos_folder = Path("Images")
    team_images = {
        'Alpine': logos_folder / 'Alpine.png',
        'Aston Martin': logos_folder / 'Aston_Martin.png',
        'Ferrari': logos_folder / 'Ferrari.png',
        'McLaren': logos_folder / 'McLaren.png',
        'Red Bull': logos_folder / 'Red_Bull.png',
        'VCARB': logos_folder / 'VCARB.png',
        'AlphaTauri': logos_folder / 'AlphaTauri.png',
        'Alfa Romeo': logos_folder / 'Alfa_Romeo.png',
        'Mercedes': logos_folder / 'Mercedes.png',
        'Haas': logos_folder / 'Haas.png',
    }

    # Create the Plotly figure with markers DISABLED
    fig = px.line(df_for_plotting, 
                  x=df_for_plotting.index, 
                  y=df_for_plotting.columns,
                  markers=False, # UPDATE 1: Set to False to disable markers
                  color_discrete_map=team_colors,
                  labels={'variable': 'Team', 'value': 'Place'})
    
    value=30
    fig.update_traces(line=dict(width=value))

    # Loop to add encoded logos
    for trace in fig.data:
        # UPDATE 2: Removed all code for marker sizing and coloring
        
        team_name = trace.name
        image_path = team_images.get(team_name)

        if image_path and Path(image_path).is_file():
            encoded_image = image_to_base64(image_path)
            last_x = trace.x[-1]
            last_y = trace.y[-1]

            fig.add_layout_image(
                dict(
                    source=encoded_image,
                    xref="x", yref="y",
                    x=last_x, y=last_y,
                    sizex=0.9, sizey=0.9,
                    xanchor="center", yanchor="middle",
                    layer="above"
                )
            )

    # Axis formatting
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

    fig.update_yaxes(title_text="Ranking", autorange="reversed", tickvals=tick_values, ticktext=tick_labels)
    
    num_races = len(df_for_plotting.index)
    fig.update_xaxes(
        title_text="Race",
        range=[0, num_races-0.9] 
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