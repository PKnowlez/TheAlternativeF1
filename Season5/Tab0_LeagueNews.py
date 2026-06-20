import streamlit as st
from streamlit_carousel import carousel
# from Season5.Articles import 

def Tab0():
    if 'show_all_content' not in st.session_state:
        st.session_state.show_all_content = False

    #region --

    st.markdown("No news just yet.")

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
        st.markdown("Under Construction")