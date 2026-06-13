from wct.data_loader import *
from wct.constants import *
from wct.standings import *


def main():

    group_matches = import_data(PATH_TO_GROUP_MATCHES)
    group_matches = group_matches.astype({
        "Home Score": "int8",
        "Away Score": "int8"
        })

    group_standings = import_data(PATH_TO_GROUP_STANDINGS)

    home_team = input("Enter home team: ")
    away_team = input("Enter away team: ")
    home_team_goals = int(input(f"{home_team} goals: "))
    away_team_goals = int(input(f"{away_team} goals: "))

    group_matches = update_match(group_matches, home_team, away_team, home_team_goals, away_team_goals)
    print(group_matches)

    for team in group_standings["Team"]:
        calculate_standings(group_standings)

if __name__ == "__main__":
    main()
