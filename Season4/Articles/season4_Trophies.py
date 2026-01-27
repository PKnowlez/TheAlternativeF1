import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

S4Trophy = Image.open("./Season4/Images/TrophyS4 Text.png")
Monaco = Image.open("./Season4/Images/Monaco Trophy Wide.png")

def article():
    date = "Monday 01/26/2026"
    author = "Patrick"

    st.subheader('''Race Week: Monaco''')
    st.markdown('''
                This week the league takes to the streets of Monte Carlo, where drivers will be tested around the tightest street circuit on the calendar. The ultimate racing challenge. A driver's skill, attention, and guts will be tesxted by this iconic circuit.

                Because this is a post-season race, there are no points. Only honor, glory, and bragging rights are on the line during this race. On top of the bragging rights, the winner will be awarded a replica Monaco trophy with some Alternative styling.

                With all this said, it is about time to dissect the championship trophies earned by our season champions as well as the special Monaco trophy.

                **WHAT'S IN THE CHAMPION'S TROPHY**
                ''')
    st.image(S4Trophy)
    st.markdown('''**MONACO TROPHY**''')
    st.image(Monaco)
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