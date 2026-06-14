import pandas as pd
from wct.constants import *


def main():

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

    while True:

        print(group_standings[group_standings["Group"] == "C"])
        print(group_matches[group_matches["Status"] != "Finished"])
        match_select = int(input("Choose a match number to update: "))
        home_team = group_matches.loc[match_select, "Home Team"]
        away_team = group_matches.loc[match_select, "Away Team"]
        print(f"You have chosen to update the match between {home_team} and {away_team}.")
        home_points = int(input(f"How many goals did {home_team} score? "))
        away_points = int(input(f"How many goals did {away_team} score? "))

        group_matches.loc[match_select, "Home Score"] += home_points
        group_matches.loc[match_select, "Away Score"] += away_points
        group_matches.loc[match_select, "Status"] = "Finished"

        print("Successfully updated match")
        print(group_matches[group_matches.index == match_select])

        group = group_standings.loc[home_team, "Group"]
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

        print("Successfully updated group standings")
        print(group_standings[group_standings["Group"] == group])

        choice = input("Would you like to update the next match? (y/n)")

        if choice.lower() == 'y':
            continue
        elif choice.lower() == 'n':
            break
        else:
            break

if __name__ == "__main__":
    main()
