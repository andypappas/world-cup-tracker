import streamlit as st
import pandas as pd


def main():
    st.set_page_config(page_title="World Cup Tracker", layout="wide")

    st.title("World Cup Tracker")

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

