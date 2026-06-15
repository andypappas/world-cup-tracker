from wct.standings import update_group_standings
from wct.data_loader import save_group_stage_matches
from wct.matches import update_finished_group_match
from wct.data_loader import load_group_stage_matches
import streamlit as st
import pandas as pd


def render_group_matches_page():

    st.title("Group Stage Matches")

    group_matches = load_group_stage_matches()

    team_filter = st.selectbox(
        "Filter by team",
        ["All"] + sorted(set(group_matches["Home Team"]) | set(group_matches["Away Team"]))
    )

    group_filter = st.selectbox(
        "Filter by group",
        ["All"] + sorted(set(group_matches["Group"]))
    )

    if team_filter != "All":
        group_matches = group_matches[
            (group_matches["Home Team"] == team_filter) |
            (group_matches["Away Team"] == team_filter)
        ]

    if group_filter != "All":
        group_matches = group_matches[
            (group_matches["Group"] == group_filter)
        ]

    upcoming = group_matches[group_matches["Status"] == "Upcoming"]
    finished = group_matches[group_matches["Status"] == "Finished"]

    tab1, tab2, = st.tabs(["Upcoming", "Finished"], width='stretch')

    with tab1:
        st.header("Upcoming Matches")
        st.dataframe(upcoming, width='stretch')

        with st.form("user_form"):
            match_select = st.number_input("Select match", min_value=1)
            home_points = st.number_input("Home team score", min_value=0)
            away_points = st.number_input("Away team score", min_value=0)
            submitted = st.form_submit_button("Submit")
            home_team = group_matches.loc[match_select, "Home Team"]
            away_team = group_matches.loc[match_select, "Away Team"]

            if submitted:
                group_matches = update_finished_group_match(group_matches, match_select, home_points, away_points)
                update_group_standings(home_team, away_team, home_points, away_points)
                save_group_stage_matches(group_matches)

                st.success(f"{home_team}: {home_points}\n{away_team}: {away_points}")

    with tab2:
        st.header("Finished Matches")
        st.dataframe(finished, width='stretch')
