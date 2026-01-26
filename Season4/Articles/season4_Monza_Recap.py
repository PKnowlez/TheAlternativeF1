import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

monza = Image.open("./Season4/Images/Monza2026.png")
Ferrari = Image.open("./Season4/Images/Silly Season/FerrariS5.png")

def article():
    date = "Sunday 01/25/2026"
    author = "A Joint Patrick & The Intern Production"

    st.subheader('''Race Recap: Mama Mia, Here We Go One Last Time''')
    st.markdown('''
                So the league had one last race. One last race to determine who sucks the least out of these amateur "drivers." And honestly, it kind of delivered? Maybe? Well at least there were some memeable moments.

                I'll leave the recap and what it all means for Patrick later on in this post, but I've pulled out the original, the one and only, my true genesis, to recap this one.
                ''')
    st.image(monza)
    st.markdown('''
                Thank you to our illustrious intern for that lovely bit of memery. The plan here is to succinctly wrap up the race in a short paragraph or two. From there, the reader will be treated to some significant stats synopsis.

                The race got off to a bumpy start for the championship hopefully at Alpine. Joshua found himself starting 10th due to his self-caused, accident on track during qualifying. Beyond that mistake, there were very few issues during qualifying.

                With drivers lined up on the grid, league officials warned everyone to be cautious into the first turn. Unfortunately, the other Alpine driver seemed to have radio communication issues during those warnings and created a multi-car pileup in the chicane. This forced a race restart and an immediate penalty for Eddie who would start last, behind Boz and Erick.

                Once the restart occured, drivers were careful and began a DRS train of sorts with micro battles ensuing over the course of the first few laps. During these micro battles, Joshua made his way up the standings and essentailly secured his championship with a finish. The VCARB duo was chasing Jairo, with Jaden just behind them.

                To clinch the championship on the constructor side, the Mercedes duo simply held the line. Jairo's race win solidified the team's second ever championship and the rookie duo's first ever championship. 
                
                And so, Alpine's Joshua won his first ever Driver's Championship, the second driver in league history to achieve this feat. Mercedes snagged their second Constructor's Championship, becoming the first constructor to win multiple championships. This season had a number of other significant statistics which are listed below.
                
                - Lowest DNS percentage in league history (12.75%)
                - First Driver's Champion to not win the most races in the season (Joshua)
                - First Driver's and Constructor's Championship decisions both in the final race
                - First ever 1000 point driver (Nick)
                - First and Second 1000 point teams (McLaren and Mercedes)

                **SILLY SEASON**
                
                With the season closed out, some important silly season updates have come to light. The first, however, is not driver or team related. For Post-Season Testing, the teams will take to the streets of Monaco again. This time, they will run in cockpit view as well as with full Parc Ferme in effect.

                But maybe more importantly, Ferrari has confirmed their lineup with our intrepid beat reporter. Please see below for their formal driver lineup.
                ''')
    st.image(Ferrari)
    st.markdown(
        f'''
        <p style="color:lightgray;"> {date} - {author}</p>
        ''',
        unsafe_allow_html=True,)
    st.divider()

# ----- How to add a GIF: ----- #
# gif = open('./Images/surfer.gif','rb')
# contents = gif.read()
# data_url = base64.b64encode(contents).decode('utf-8')
# st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="Your GIF">', unsafe_allow_html=True)

# ----- How to add a Video: ----- #
# video = "./Images/VideoFile.mp4"
# st.video(video, format="video/mp4", loop=False, autoplay=False, muted=False, width="stretch")

# ----- How to add a Carousel ----- #
# carousel_images = [
#             {
#                 "title": "",
#                 "text": "",
#                 "img": "./Images/image.png"
#             },
#             {
#                 "title": "",
#                 "text": "",
#                 "img": "./Images/image.png"
#             },
#         ]

# carousel(items=carousel_images, interval=20000)