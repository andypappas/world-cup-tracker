from wct.data_loader import *
from wct.constants import *
from wct.standings import *


def main():

    matches = import_data(PATH_TO_MATCH_SCHEDULE)
    teams = import_data(PATH_TO_TEAMS_LIST)
    standings = import_data(PATH_TO_STANDINGS) 

    home_team = input("Enter home team: ")
    away_team = input("Enter away team: ")
    home_team_goals = int(input(f"{home_team} goals: "))
    away_team_goals = int(input(f"{away_team} goals: "))

    matches = update_match(matches, home_team, away_team, home_team_goals, away_team_goals)
    print(matches)

    for team in teams["Team"]:
        calculate_standings(standings)

if __name__ == "__main__":
    main()
