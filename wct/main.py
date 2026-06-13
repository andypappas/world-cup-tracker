from wct.data_loader import *
from wct.constants import *


def main():

    home_team = input("Enter home team: ")
    away_team = input("Enter away team: ")
    home_team_goals = int(input(f"{home_team} goals: "))
    away_team_goals = int(input(f"{away_team} goals: "))

    matches = import_data(PATH_TO_MATCH_SCHEDULE)

    print(matches)
    print(f"Home Team: {home_team}")
    print(f"Away Team: {away_team}")
    print(f"{home_team} goals: {home_team_goals}")
    print(f"{away_team} goals: {away_team_goals}")


if __name__ == "__main__":
    main()
