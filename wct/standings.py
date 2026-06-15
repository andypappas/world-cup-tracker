import pandas as pd
from wct.data_loader import load_group_stage_standings
from wct.data_loader import save_group_standings
from wct.config import POINTS_FOR_WIN
from wct.config import POINTS_FOR_DRAW

def update_group_standings(team1, team2, score1, score2):
    df = load_group_stage_standings()

    df.loc[team1, "Played"] += 1
    df.loc[team2, "Played"] += 1
    df.loc[team1, "Goals For"] += score1
    df.loc[team1, "Goals Against"] += score2
    df.loc[team2, "Goals For"] += score2
    df.loc[team2, "Goals Against"] += score1
            
    if score1 > score2:
        df.loc[team1, "Wins"] += 1
        df.loc[team2, "Losses"] += 1
        df.loc[team1, "Points"] += POINTS_FOR_WIN
        df.loc[team1, "Goal Difference"] = score1 - score2
        df.loc[team2, "Goal Difference"] = score2 - score1
    elif score1 < score2:
        df.loc[team1, "Losses"] += 1
        df.loc[team2, "Wins"] += 1
        df.loc[team2, "Points"] += POINTS_FOR_WIN
        df.loc[team1, "Goal Difference"] = score1 - score2
        df.loc[team2, "Goal Difference"] = score2 - score1
    else:
        df.loc[team1, "Draws"] += 1
        df.loc[team2, "Draws"] += 1
        df.loc[team1, "Points"] += POINTS_FOR_DRAW
        df.loc[team2, "Points"] += POINTS_FOR_DRAW

    save_group_standings(df)


def sort_group_standings(df):

    df = df.sort_values(
        ["Group", "Points", "Goal Difference", "Goals For", "Goals Against"],
        ascending=[True, False, False, False, True]
        )
    df["Rank"] = df.groupby("Group").cumcount() + 1
    return df
