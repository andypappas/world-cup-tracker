import pandas as pd
import streamlit as st
from wct.config import *
from wct.pages.group_matches import *
from wct.pages.group_standings import *
from wct.pages.knockout_bracket import *
from wct.pages.knockout_matches import *


def main():

    st.set_page_config(page_title="World Cup Tracker", layout="centered")
    st.title("World Cup Tracker")

    page = st.sidebar.radio(
            "Menu",
            [
                "Group Stage Matches",
                "Group Stage Standings",
                "Knockout Stage Matches",
                "Knockout Bracket",
                ],
            )

    if page == "Group Stage Matches":
        render_group_matches_page()
    elif page == "Group Stage Standings":
        render_group_standings_page()
    elif page == "Knockout Stage Matches":
        render_knockout_matches_page()
    elif page == "Knockout Bracket":
        render_knockout_bracket_page()


if __name__ == "__main__":
    main()
