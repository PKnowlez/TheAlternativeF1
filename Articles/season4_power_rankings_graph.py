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

    fig.update_yaxes(
        title_text="Ranking", 
        tickvals=tick_values, 
        ticktext=tick_labels,
        range=[max_rank + 0.5, min_rank - 0.5] 
    )
    
    num_races = len(df_for_plotting.index)
    fig.update_xaxes(
        title_text="Race",
        range=[0.25, num_races-0.7] 
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

def bahrain_article():
    date = "Thursday 10/02/2025"
    author = "Patrick"

    st.markdown('''**Bahrain Power Rankings**''')
    st.markdown('''
                Red Bull & Mercedes have decided to tango a bit in the mid-field. The teams have swapped back and forth yet again due to the performances from last night's race.

                Red Bull primarily benefitted from the FIA removing Brently's penalty and the league reinstating Matthew's finishing point.

                Additionally, with strong qualifying and from winning the race, the VCARB team promoted themselves up the rankings. However, this is likely more due to McLaren's lack of a second #1 driver during the race with Travis disqualified by the FIA.
                
                Alpine remains the top contender at this stage even though they are in second overall in the Constructor Standings.
                ''')
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date} - {author}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()

def miami_article():
    date = "Friday 10/10/2025"
    author = "Patrick"

    st.markdown('''**Miami Power Rankings**''')
    st.markdown('''
                After an incredible performance during the sprint, Mercedes had a lack luster outing in the main race. This keeps them low in the power rankings.

                Red Bull and Ferrari made a swap due to the incredible performance by Brently who is solidifying himself as the team's number one early in the season.

                After the preseason and Bahrain, it seemed the VCARB team had things sorted out and were rocketing towards the top. However, there is a chance they were just a shooting star.

                Due to this, as well as having a full line up, McLaren overtakes into second place and nearly dislodges Alpine from their perch atop the rankings.
                ''')
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date} - {author}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()

def spain_article():
    date = "Monday 10/27/2025"
    author = "Patrick"

    st.markdown('''**Spain Power Rankings**''')
    st.markdown('''
                With the first break of the season over, the drivers took Spain's high speed circuit, where tire wear, dirty air, and a whole lot of flare occurred.

                Mercedes took home its first full length race win of the season helping them move up in the power rankings. Alpine stays top dog though as McLaren falters and VCARB takes second place back.

                In the midfield, Aston Martin and Ferrari stocks plummet as the teams faced minor setbacks during the race, while Red Bull seemed to have started to get things figured out.

                All in all this was a turbulent race and the power rankings reflect that. In Mexico, expect to see more position swapping here as tire wear is again a major concern going into the race.
                ''')
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date} - {author}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()

def spain_article():
    date = "Thursday 10/30/2025"
    author = "The Intern"

    st.markdown('''**Mexico Power Rankings**''')
    st.markdown('''
                There was nearly nothing to meme this week, so I decided to take the week off just like the Taveras. My boss told me I couldn't simply do nothing this week so I told him I would write something for this power ranking.

                But like, honestly, this is the most dry thing on the planet. Who actually cares? Whatever. Alpine sucks so they dropped down. Eddie not being around is a joke, and I keep hearing Joshua yell, "LOCK IN JUNIOR," but then it's just echos because Eddie ain't locking in.

                Mercedes is obviously on the rise, but the boss said something about how the math doesn't let them leap frog a bunch of positions. Math sucks. Anyway, enjoy the rankings, at least its colorful.
                ''')
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date} - {author}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()

def baku_article():
    date = "Sunday 11/9/2025"
    author = "Patrick"

    st.markdown('''**Baku Power Rankings**''')
    st.markdown('''
                Mercedes is on the rise! Back-to-back wins, both drivers in the Top 5, and some staggering consistency over the last few races has them unanimoulsy voted up another rank from our power rankers.

                Alpine jumps back to the top slot as they overtake a slowing VCARB. McLaren began receiving more upward votes this week as well as their top driver began to pursue the podium again.

                Further down the field, Red Bull is a casualty of the streaking Mercedes duo. In reality they earned strong votes this week but simply were snuffed out by the rising rookies. 
                
                Aston Martin and Ferrari remain where they are at in the rankings, but there are rumblings to have Ferrari overtake Aston Martin if they continue their current trajectory.
                ''')
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date} - {author}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()