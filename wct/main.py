from pathlib import Path
import streamlit as st
import pandas as pd


def main():

    DATA_DIR = Path.home() / "data" / "wct-data"

    # Points earned
    POINTS_FOR_WIN  = 3
    POINTS_FOR_DRAW = 1

    # File paths
    PATH_TO_GROUP_MATCHES       = DATA_DIR / "group-stage-matches.csv"
    PATH_TO_GROUP_STANDINGS     = DATA_DIR / "group-stage-standings.csv"
    # PATH_TO_KNOCKOUT_MATCHES    = DATA_DIR / "knockout-stage-matches.csv"
    # PATH_TO_KNOCKOUT_STANDINGS  = DATA_DIR / "knockout-stage-standings.csv"

    group_matches = pd.read_csv(PATH_TO_GROUP_MATCHES, index_col="Match ID")
    group_matches = group_matches.astype({
        "Home Score": "int8",
        "Away Score": "int8"
        })
    group_standings = pd.read_csv(PATH_TO_GROUP_STANDINGS, index_col="Team")
    group_standings = group_standings.astype({
        "Played": "int8",
        "Points": "int8",
        "Wins": "int8",
        "Losses": "int8",
        "Draws": "int8",
        "Goal Difference": "int8"
        })

    st.set_page_config(page_title="World Cup Tracker", layout="centered")
    st.title("World Cup Tracker")

    home_team = ""
    away_team = ""

    match_select = 1
    home_points = 0
    away_points = 0

    upcoming = group_matches[group_matches["Status"] == "Upcoming"]
    finished = group_matches[group_matches["Status"] == "Finished"]

    tab1, tab2, = st.tabs(["Upcoming", "Finished"], width='stretch')

    with tab1:
        st.header("Upcoming Matches")
        st.dataframe(upcoming, width='stretch')


        with st.form("user_form"):
            match_select = st.number_input("Select match", min_value=0)
            home_points = st.number_input("Home team score", min_value=0)
            away_points = st.number_input("Away team score", min_value=0)
            submitted = st.form_submit_button("Submit")

        if submitted:

            home_team = group_matches.loc[match_select, "Home Team"]
            away_team = group_matches.loc[match_select, "Away Team"]

            group_matches.loc[match_select, "Home Score"] += home_points
            group_matches.loc[match_select, "Away Score"] += away_points
            group_matches.loc[match_select, "Status"] = "Finished"

            group_standings.loc[home_team, "Played"] += 1
            group_standings.loc[away_team, "Played"] += 1
            group_standings.loc[home_team, "Goals For"] += home_points
            group_standings.loc[home_team, "Goals Against"] += away_points
            group_standings.loc[away_team, "Goals For"] += away_points
            group_standings.loc[away_team, "Goals Against"] += home_points

            if home_points > away_points:
                group_standings.loc[home_team, "Wins"] += 1
                group_standings.loc[away_team, "Losses"] += 1
                group_standings.loc[home_team, "Points"] += POINTS_FOR_WIN
                group_standings.loc[home_team, "Goal Difference"] = home_points - away_points
                group_standings.loc[away_team, "Goal Difference"] = away_points - home_points
            elif home_points < away_points:
                group_standings.loc[home_team, "Losses"] += 1
                group_standings.loc[away_team, "Wins"] += 1
                group_standings.loc[away_team, "Points"] += POINTS_FOR_WIN
                group_standings.loc[home_team, "Goal Difference"] = home_points - away_points
                group_standings.loc[away_team, "Goal Difference"] = away_points - home_points
            else:
                group_standings.loc[home_team, "Draws"] += 1
                group_standings.loc[away_team, "Draws"] += 1
                group_standings.loc[home_team, "Points"] += POINTS_FOR_DRAW
                group_standings.loc[away_team, "Points"] += POINTS_FOR_DRAW

            group_standings = group_standings.sort_values(
                    ["Group", "Points", "Goal Difference", "Goals For", "Goals Against"],
                    ascending=[True, False, False, False, True]
                    )
            group_standings["Rank"] = group_standings.groupby("Group").cumcount() + 1

            st.success(f"{home_team}: {home_points}\n{away_team}: {away_points}")

    with tab2:
        st.header("Finished Matches")
        st.dataframe(finished, width='stretch')


if __name__ == "__main__":
    main()
