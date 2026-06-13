import pandas as pd
from wct.constants import *


def import_data(file_path):
    df = pd.read_csv(file_path)
    return df

def update_match(df, team1, team2, score1, score2):
    df.loc[
            (df["Home Team"] == team1) &
            (df["Away Team"] == team2),
            ["Home Score", "Away Score", "Status"]
        ] = [score1, score2, "Finished"]
    df.to_csv(PATH_TO_GROUP_MATCHES, index=False)
    return df
