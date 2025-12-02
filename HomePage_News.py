import streamlit as st
from PIL import Image
from streamlit_carousel import carousel
from Articles import season4_track_overview, season4_schedule_reveal, season4_trophy_reveal, season4_track_tier_list, \
                season4_track_rankings, season4_ROTY_award, season4_power_rankings_graph

def HomePageNews():
    st.header("The Alternative F1 League")
    # Your custom CSS for the divider
    st.markdown("""
    <style>
    .colored-divider {
        border-top: 3px solid #00b4da;
        border-radius: 3px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Use the custom divider
    st.markdown('<div class="colored-divider"></div>', unsafe_allow_html=True)

    if 'show_all_content' not in st.session_state:
        st.session_state.show_all_content = False

    #region latest article
    
    season4_power_rankings_graph.graph()
    season4_power_rankings_graph.spa_article()   

    #endregion

    # ----------------------------------------------------------------------------------------------------------
    # "Show More/Less" button 
    if not st.session_state.show_all_content:
        if st.button('Show More'):
            st.session_state.show_all_content = True
            st.rerun()  # Rerun the app to show everything
    else: 
        if st.button('Show Less'):
            st.session_state.show_all_content = False
            st.rerun()

    if st.session_state.show_all_content:

        season4_power_rankings_graph.austriaR_article()  

        season4_power_rankings_graph.baku_article()

        season4_power_rankings_graph.spain_article()   

        season4_power_rankings_graph.miami_article()  

        season4_power_rankings_graph.bahrain_article()

        season4_power_rankings_graph.preseason_article()

        newapp = Image.open('./Images/NewApp.png')
        st.subheader("New Season 4 App Live!")
        st.markdown('''Pop open the sidebar and head to the new app where in season articles, results, and rankings will be found!''')
        st.image(newapp)

        season4_ROTY_award.article()

        season4_track_rankings.article()
        
        season4_track_tier_list.article()

        season4_trophy_reveal.article()

        season4_schedule_reveal.article()

        season4_track_overview.article()

        #region Driver Announcements
        st.subheader("Season 4 Driver Lineup")
        driver_announcements = [
            {
                "title": "",
                "text": "",
                "img": "./Images/Driver_Lineup.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Alpine_Driver_Post.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/McLaren_Driver_Post.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Red_Bull_Driver_Post.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/VCARB_Driver_Post.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Intern_1.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Intern_2.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Aston_Martin_Driver_Post.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Ferrari_Driver_Post.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Mercedes_Driver_Post.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Tracks_1.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Tracks_2.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Tracks_3.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Tracks_4.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Tracks_5.png"
            },
            {
                "title": "",
                "text": "",
                "img": "./Images/Tracks_6.png"
        },
        ]

        carousel(items=driver_announcements, interval=20000)
        st.divider()
        #endregion