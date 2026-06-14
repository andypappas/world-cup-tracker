from wct.constants import *
from wct.standings import *


def main():

    group_matches = pd.read_csv(PATH_TO_GROUP_MATCHES, index_col="Match Number")
    group_matches = group_matches.astype({
        "Home Score": "int8",
        "Away Score": "int8"
        })
    print(group_matches[group_matches["Status"] != "Finished"])
    match_select = int(input("Choose a match number to update: "))
    home_team = group_matches.loc[match_select, "Home Team"]
    away_team = group_matches.loc[match_select, "Away Team"]
    print(f"You have chosen to update the match between {home_team} and {away_team}.")
    home_points = int(input(f"How many goals did {home_team} score? "))
    away_points = int(input(f"How many goals did {away_team} score? "))

    group_matches.loc[match_select, home_team] += home_points
    group_matches.loc[match_select, away_team] += away_points
    group_matches.loc[match_select, "Status"] = "Finished"

    print("Successfully updated match")
    print(group_matches[group_matches["Match Number"] == match_select])
    #group_matches = update_match(match_select)
    #print(group_matches)


if __name__ == "__main__":
    main()
