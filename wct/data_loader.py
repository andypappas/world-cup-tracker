from wct.config import PATH_TO_GROUP_MATCHES
from wct.config import PATH_TO_GROUP_STANDINGS
from wct.config import PATH_TO_KNOCKOUT_STANDINGS
from wct.config import PATH_TO_KNOCKOUT_MATCHES
import pandas as pd


def load_group_stage_matches():
    group_matches = (
        pd.read_csv(PATH_TO_GROUP_MATCHES, index_col="Match ID")
        .astype({
            "Home Score": "int8",
            "Away Score": "int8"
        })
    )
    return group_matches

def load_group_stage_standings():
    group_standings = (
        pd.read_csv(PATH_TO_GROUP_STANDINGS, index_col="Team")
        .astype({
            "Played": "int8",
            "Points": "int8",
            "Wins": "int8",
            "Losses": "int8",
            "Draws": "int8",
            "Goal Difference": "int8"
        })
    )
    return group_standings

def load_knockout_stage_matches():
    knockout_matches = pd.read_csv(PATH_TO_KNOCKOUT_MATCHES)
    return knockout_matches

def load_knockout_bracket():
    knockout_bracket = pd.read_csv(PATH_TO_KNOCKOUT_STANDINGS)

def save_group_stage_matches(df):
    df.to_csv(PATH_TO_GROUP_MATCHES)

def save_group_standings(df):
    df.to_csv(PATH_TO_GROUP_STANDINGS)

def save_knockout_matches():
    pass

def save_knockout_bracket():
    pass
