import streamlit as st
import pandas as pd

def HomePageSettings():
    assist_restrictions = {
        "Assist Restriction":   [
                                    'Steering Assist',
                                    'Braking Assist',
                                    'Anti-Lock Brakes (ABS)',
                                    'Traction Control',
                                    'Dynamic Racing Line',
                                    'Gearbox',
                                    'Pit Assist',
                                    'Pit Release Assist',
                                    'ERS Assist',
                                    'DRS Assist',
                                    'Force Cockpit Camera'
        ],
        "Setting Allowed":      [
                                    'Off',
                                    'Off',
                                    'On',
                                    'Full',
                                    'Corners Only',
                                    'Automatic',
                                    'On',
                                    'On',
                                    'Off',
                                    'Off',
                                    'Off'
        ]
    }

    simulation_settings = {
        "Simulation Settings":  [
                                    'Equal Car Performance',
                                    'Recovery Mode',
                                    'Surface Type',
                                    'Low Fuel Mode',
                                    'Race Starts',
                                    'Unsafe Pit Release',
                                    'Car Damage',
                                    'Car Damage Rate',
                                    'Collisions',
                                    'Off for First Lap Only',
                                    'Off for Griefing',
                                    'Weather'
        ],
        "Setting":              [
                                    'On',
                                    'None',
                                    'Realistic',
                                    'Easy',
                                    'Manual',
                                    'Off',
                                    'Simulation',
                                    'Standard or Simulation*',
                                    'On',
                                    'Disabled',
                                    'Disabled',
                                    'Dynamic'
        ]
    }

    rules_flags = {
        "Rules & Flags":        [
                                    'Rules & Flags',
                                    'Corner Cutting Stringency',
                                    'Parc Ferme Rules',
                                    'Pit Stop Experience',
                                    'Safety Car',
                                    'Safet Car Experience',
                                    'Formation Lap',
                                    'Red Flags',
                                    'Affects Licence Level'
        ],
        "Setting":              [
                                    'On',
                                    'Strict**',
                                    'Off',
                                    'Immersive',
                                    'Increased',
                                    'Immersive',
                                    'Off',
                                    'Standard',
                                    'Off'
        ]
    }

    weekend_structure = {
        "Regular Weekend Structure":    [   
                                            'Weekend Structure',
                                            'Practice Format',
                                            'Qualifying Format',
                                            'Session Length',
                                            'Starting Grid'
        ],
        "Parameter":                    [   
                                            'Standard',
                                            'Off',
                                            'Full',
                                            'Long (50%)',
                                            'Qualifying'
        ]
    }

    sprint_weekend = {
        "Sprint Weekend Structure":     [
                                            'Weekend Structure',
                                            'Practice Format',
                                            'Sprint Qualifying Format',
                                            'Race Qualifying Format',
                                            'Sprint Session Length',
                                            'Race Session Length',
                                            'Sprint Starting Grid',
                                            'Race Starting Grid'
        ],
        "Setting":                      [
                                            'Sprint',
                                            'Off',
                                            'Short',
                                            'Off',
                                            'Long',
                                            'Long',
                                            'Qualifying',
                                            'Reverse Sprint Results'
        ]
    }

    col1, col2 = st.columns(2)
    with col1:
        html_table_setup(assist_restrictions)
    with col2:
        html_table_setup(simulation_settings)

    st.divider()    
    
    col3, col4, col5 = st.columns(3)
    with col3:
        html_table_setup(rules_flags)
    with col4:
        html_table_setup(weekend_structure)
    with col5:
        html_table_setup(sprint_weekend)

    st.markdown("*League officials are still determining best course of action for this setting.")
    st.markdown("**Depending on teh track this setting may be adjusted to ensure a competitive and enjoyable racing experience.")

def html_table_setup(list):
    df = pd.DataFrame(list)
    list_styled = df.style.set_properties(**{'text-align': 'left'}).set_table_styles([
        {'selector': 'th', 'props': [('text-align', 'left')]},
        {'selector': 'td', 'props': [('text-align', 'left')]}]).hide(axis="index")
    list_html_table = list_styled.to_html()
    st.markdown(list_html_table, unsafe_allow_html=True)
