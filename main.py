import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title="World Cup Tracker", layout="wide")

    st.title("World Cup Tracker")

    matches = pd.read_csv("data/matches.csv")

    team_filter = st.selectbox(
        "Filter by team",
        ["All"] + sorted(set(matches["home_team"]) | set(matches["away_team"]))
        )

    if team_filter != "All":
        matches = matches[
            (matches["home_team"] == team_filter) |
            (matches["away_team"] == team_filter)
            ]

    st.dataframe(matches, width='stretch')


if __name__ == "__main__":
    main()
