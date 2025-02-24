# This script will almagamte all of the previous season's results for a constructor to determine:
#   Total Wins
#   Total Podiums
#   Total Points
# It will provide a table for all of the constructors with all of this information

import streamlit as st
import pandas as pd
import Functions

def ConstructorStats(season):
    dfs = []
    for i in range(season):
        a, b, c, globals()[f'df{i}'], e, f = Functions.PointTotals(i+1)
        dfs.append(globals()[f'df{i}'])

    # Combine the dataframes
    combined_df = pd.concat(dfs)

    # Group by 'Team' and sum the 'Points'
    team_totals = combined_df.groupby('Team')['Points'].sum().reset_index()

    # Sort by 'Points' in descending order
    team_totals_sorted = team_totals.sort_values(by='Points', ascending=False).reset_index(drop=True)

    # Add 'Place' column
    team_totals_sorted['Place'] = team_totals_sorted.index + 1

    # Reorder columns
    team_totals_sorted = team_totals_sorted[['Place', 'Team', 'Points']]

    st.dataframe(team_totals_sorted, hide_index=True)