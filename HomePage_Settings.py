import streamlit as st
import pandas as pd

def HomePageSettings():
    rules = {
        "Setting":  [   
                        'Race Length',
                        'Qualifying Length',
                        'Sprint Length',
                        'Sprint Qualifying Length',
                        'Traction Control',
                        'Racing Line',
                        'Gearbox',
                        'Custom Setups',
                        'Damage',
                        'Safety Car & Flags',
                        'Weather',
                        'Corner Cutting'
                    ],
        "Parameter":[   
                        '50%',
                        'Full',
                        'SPRINT LENGTH',
                        'Short',
                        'Full Allowed',
                        'Corners Only',
                        'Automatic Allowed',
                        'Allowed',
                        'Simulation',
                        'Increased',
                        'Accurate',
                        'Strict'
                    ]
    }
    df = pd.DataFrame(rules)
    
    # Use Pandas Styler to apply CSS directly to headers and hide the index
    styled_df = df.style.set_properties(**{'text-align': 'left'}) \
                      .set_table_styles([
                          {'selector': 'th', 'props': [('text-align', 'left')]},
                          # Add 'td' selector if you want data cells also left-justified
                          {'selector': 'td', 'props': [('text-align', 'left')]}
                      ]) \
                      .hide(axis="index") # This is the key to hide the index

    # Convert the styled DataFrame to HTML
    html_table = styled_df.to_html() # No need for index=False here, as hide(axis="index") does the job

    st.markdown(html_table, unsafe_allow_html=True)