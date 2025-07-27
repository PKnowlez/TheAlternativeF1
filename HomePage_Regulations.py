import streamlit as st
from PIL import Image
import pandas as pd

def HomePageRegulations():
    rules = {
        "":['1','2','3','4','5','6','7','8','9'],
        "Regulation":   [
                            'Points Elgibility',
                            'Finishing Points',
                            'Fastest Lap Award',
                            'Driver of the Day Award',
                            'Most Overtakes Award',
                            'VSC or Safety Car Delta Glitch',
                            "Endangering or Ruining Another Driver's Race",
                            'Right to Protest',
                            'Sprint Day Format'
                        ],
        "Definition":   [
                            'Points are only awarded to drivers that complete the race. No points are awarded to those who DNS or DNF.',
                            'Points are awarded based on finishing postion in each race and follow the following pattern: 1st - 25, 2nd - 18, 3rd - 15, 4th - 12, 5th - 10, 6th - 8, 7th - 6, 8th - 4, 9th - 3, 10th - 2, 11th to 20th - 1.',
                            'One (1) point will be awarded to the driver with the Fastest Lap at the end of the race.',
                            'One (1) point will be awarded to the driver who earns Driver of the Day at the end of the race.',
                            'One (1) point will be awarded to the driver with the Most Overtakes at the end of the race.',
                            'If a driver wrongfully receives a Drive Through Penalty due to a VSC or Safety Car delta glitch, the driver will have their finsihing time improved by 20 seconds. This remedy will only be applied if no VSC, Safety Car, or Red Flag occurs after the glitch occurred.',
                            "If a driver's race is ruined (DNF) or endangered (more than 3 lost places) due to reckless driving actions of another driver, the reckelss driver will be awared a 5 place penalty to their finishing position. If the reckelss driving is deemed intentional, the driver will be disqualified.",
                            'Any driver that disagrees with a ruling, has the right to protes the ruling within one day of the final ruling. This protest will be reviewed by the league and require a 2/3rds majority vote to overturn.',
                            'Sprint Qualifying > Sprint > Race Qualifying = Reverse Grid set by Sprint Results (All AI will be placed in front of ALL drivers, regardless of finishing position)'
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