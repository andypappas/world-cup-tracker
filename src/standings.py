import streamlit as st
import pandas as pd

POINTS_FOR_WIN = 3
POINTS_FOR_DRAW = 1

def main():
    st.set_page_config(page_title="World Cup Tracker", layout="wide")

    st.title("World Cup Tracker")

    matches = pd.read_csv("data/matches.csv")

    games_played = 0
    wins = 0
    draws = 0
    losses = 0
    goals_for = 0
    goals_against = 0
    goal_difference = goals_for - goals_against
    points = 0

    for row in matches.iterrows():
        row.to_csv("data/group_stage_standings")

    team_filter = st.selectbox(
    "Filter by team",
    ["All"] + sorted(set(matches["home_team"]) | set(matches["away_team"]))
    )

    group_filter = st.selectbox(
    "Filter by group",
    ["All"] + sorted(matches["group"].unique())
    )

    if team_filter != "All":
        matches = matches[
            (matches["home_team"] == team_filter) |
            (matches["away_team"] == team_filter)
            ]

    if group_filter != "All":
        matches = matches[
            (matches["group"] == group_filter)
            ]

    upcoming = matches[matches["status"] == "Upcoming"]
    finished = matches[matches["status"] == "Finished"]

    

    tab1, tab2, = st.tabs(["Upcoming", "Finished"], width='stretch')

    with tab1:
        st.header("Upcoming Matches")
        st.dataframe(upcoming, width='stretch')

    with tab2:

        st.header("Finished Matches")
        st.dataframe(finished, width='stretch')



if __name__ == "__main__":
    main()
