import streamlit as st
from PIL import Image
from streamlit_carousel import carousel
from Articles import season4_track_overview, season4_schedule_reveal, season4_trophy_reveal, season4_track_tier_list, \
                season4_track_rankings, season4_ROTY_award, season4_power_rankings_graph
from Season4.Articles import season4_Monza_Recap, season4_Trophies, season4_Monaco_Recap

def HomePageNews():

    if 'show_all_content' not in st.session_state:
        st.session_state.show_all_content = False

    #region latest article
    
    st.markdown("... New Season Loading ...")

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

        st.markdown("Nothing to see here, yet.")