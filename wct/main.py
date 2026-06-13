from wct.data_loader import *
from wct.constants import *
import argparse


def main():
    
    matches = import_data(PATH_TO_MATCH_SCHEDULE)
    print(matches)

    parser = argparse.ArgumentParser(
            prog="World Cup Tracker",
            description="Tracks the 2026 World Cup Standings",
            epilog="Text at bottom of help lol"
            )

    parser.add_argument("-t", "--home-team",
                        required=True,
                        )
    parser.add_argument("-a", "--away-team",
                        required=True,
                        )

    args = parser.parse_args()
    home_team = args.home_team
    away_team = args.away_team
    print(f"Home Team: {home_team}")
    print(f"Away Team: {away_team}")


if __name__ == "__main__":
    main()
