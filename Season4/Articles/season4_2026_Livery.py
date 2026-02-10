import streamlit as st
import base64
from streamlit_carousel import carousel
from PIL import Image

wakeup = Image.open("./Season4/Images/Livery/Babe Wakeup.png")
ranking = Image.open("./Season4/Images/Livery/Intern Ranking.png")

def article():
    date = "Monday 02/09/2026"
    author = "The Intern"

    st.subheader('''2026 F1 Livery Ranking''')
    st.image(wakeup)
    st.markdown('''
                It is time. Go crazy nerds and rank to your heart's content.

                If any of you disrespect the Hot Wheels car, let's just say, your points will simply disappear.

                Click [here](https://live.tiermaker.com/41582090) to rank.
                ''')
    st.image(ranking)
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