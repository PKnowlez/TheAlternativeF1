import streamlit as st
from PIL import Image

cinema = Image.open("./Season4/Images/Monaco/cinema.png")
erick_bodies = Image.open("./Season4/Images/Monaco/erick_bodies.png")
bodies = "./Season4/Images/Monaco/erick_clip.mp4"
erick_pk = Image.open("./Season4/Images/Monaco/erick_pk.png")
erick_dive = Image.open("./Season4/Images/Monaco/erick_dive.png")
erick_crash = Image.open("./Season4/Images/Monaco/erick_crash.png")
jairo_joshua = Image.open("./Season4/Images/Monaco/jairo_joshua.png")
jaden_leo = Image.open("./Season4/Images/Monaco/jaden_leo.png")
everyone_liked = Image.open("./Season4/Images/Monaco/everyone_liked.png")
pk_jairo = Image.open("./Season4/Images/Monaco/pk_jairo.png")
settings = Image.open("./Season4/Images/Monaco/settings.png")
pk_crash = Image.open("./Season4/Images/Monaco/pk_crash.png")
brentuar = Image.open("./Season4/Images/Monaco/brentuar.png")
josh_newman = Image.open("./Season4/Images/Monaco/josh_newman.png")
team_usa = Image.open("./Season4/Images/Monaco/team_usa.png")
eddie_texting = Image.open("./Season4/Images/Monaco/eddie_texting.png")

def article():
    date = "Friday 01/30/2026"
    author = "The Intern"

    st.subheader('''Race Recap: Monaco Mayhem 2 Electric-Boo-Ga-Loo''')
    st.markdown('''What's more iconic the wine and cheese? Nick and Monaco crash outs. No cap this was the wildest race, potentially, in league history. A truly incredible, monumental, and movie worthy post-season debacle.''')
    st.image(cinema)
    st.markdown('''The craziest part of this whole race was simply Erick. This man was a loose cannon from start to finish. Dude was dive bombing, rage racing, and providing some incredibly questionable small talk... To commemorate all of this, please enjoy the reaction from league pundit Brentuar as well as some commemorative memes.''')
    st.image(erick_bodies)
    st.video(bodies, format="video/mp4", loop=False, autoplay=False, muted=False, width="stretch")
    st.image(erick_pk)
    st.image(erick_dive)
    st.image(erick_crash)
    st.markdown('''
                A true masterpiece from the now McLaren driver. His first outing in papaya and he has gone loco. Erick wasn't the only idiot to crash out though. Only two of these so called "drivers" even finised the race. But how we got to that point was nothing less than miraculous. Like I could not have paid these guys to provide this much content. Mostly because they still don't pay me, but also because this was true entropy in motion.
                
                The Mercedes duo decided it was their sole purpose in life to cause absolute carnage.
                ''')
    st.image(jairo_joshua)
    st.image(jaden_leo)
    st.markdown('''And guess what...''')
    st.image(everyone_liked)
    st.markdown('''But Jairo didn't accomplish his great feat alone. No, he had some help from his fellow Driver's Championship podium-mate.''')
    st.image(pk_jairo)
    st.markdown('''Now no one would say my boss Patrick is all that put together. But this guy was goofing, goofing, especailly with the settings...''')
    st.image(settings)
    st.markdown('''He and Brently also just straight drove their cars into walls. So much for the senior drivers of the Red Bull squad.''')
    st.image(pk_crash)
    st.image(brentuar)
    st.image(team_usa)
    st.markdown('''
                I mentioned that only 2 drivers finished, and yes it was somehow the two Red Bull rookies Joshua and Newman. True heroes of the league. A first win for Joshua and a first podium for Newman.
                
                Now, because of the magnitude of this moment, the league determined that not just a Monaco winner's trophy was due, but also a second place trophy to ensure drivers understand how huge it was to simply survive this race. There was literally a red flag restart with only four drivers...truly INSANE.

                This might have backfired though and reports are surfacing that the duo of finishers are ego-maxing in their team group chat.
                ''')
    st.image(josh_newman)
    st.markdown('''Some of you may be wondering, how has Eddie survived being roasted this entire article? Well, we saved the best for last. This guy straight up crashed texting and driving. How is that even possible? Bro was driving an imaginary car that he can put into autopilot and he still managed to wreck. It is truly a talent that he possesses.''')
    st.image(eddie_texting)
    st.markdown('''
                **SILLY SEASON**

                Don't worry, the reporting on silly season continues friends. Mercedes has locked in half their lineup. Jairo has committed to another season with the Brackley outfit.

                Rumor has it, he has even begun contract negotiations with a rookie teammate to attempt to run it back. 
                
                In response to Mercedes running it back, the McLaren duo responded, "We'll see about that."
                
                Until the next one.
                ''')
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