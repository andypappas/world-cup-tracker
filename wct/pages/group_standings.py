from wct.standings import sort_group_standings
from requests.models import stream_decode_response_unicode
from wct.data_loader import load_group_stage_standings
import streamlit as st

def render_group_standings_page():

    st.title("Group Stage Standings")

    group_standings = load_group_stage_standings()
    group_standings = sort_group_standings(group_standings)

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12 = (
        st.tabs(["Group A", "Group B", "Group C", "Group D", "Group E", "Group F",
        "Group G", "Group H", "Group I", "Group J", "Group K", "Group L"], width='stretch')
    )

    with tab1:
        st.header("Group A")
        st.dataframe(
            group_standings[group_standings["Group"] == "A"],
            width='stretch'
        )

    with tab2:
        st.header("Group B")
        st.dataframe(
            group_standings[group_standings["Group"] == "B"],
            width='stretch'
        )

    with tab3:
        st.header("Group C")
        st.dataframe(
            group_standings[group_standings["Group"] == "C"],
            width='stretch'
        )

    with tab4:
        st.header("Group D")
        st.dataframe(
            group_standings[group_standings["Group"] == "D"],
            width='stretch'
        )

    with tab5:
        st.header("Group E")
        st.dataframe(
            group_standings[group_standings["Group"] == "E"],
            width='stretch'
        )

    with tab6:
        st.header("Group F")
        st.dataframe(
            group_standings[group_standings["Group"] == "F"],
            width='stretch'
        )

    with tab7:
        st.header("Group G")
        st.dataframe(
            group_standings[group_standings["Group"] == "G"],
            width='stretch'
        )

    with tab8:
        st.header("Group H")
        st.dataframe(
            group_standings[group_standings["Group"] == "H"],
            width='stretch'
        )

    with tab9:
        st.header("Group I")
        st.dataframe(
            group_standings[group_standings["Group"] == "I"],
            width='stretch'
        )

    with tab10:
        st.header("Group J")
        st.dataframe(
            group_standings[group_standings["Group"] == "J"],
            width='stretch'
        )

    with tab11:
        st.header("Group K")
        st.dataframe(
            group_standings[group_standings["Group"] == "K"],
            width='stretch'
        )

    with tab12:
        st.header("Group L")
        st.dataframe(
            group_standings[group_standings["Group"] == "L"],
            width='stretch'
        )
