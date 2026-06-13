from pathlib import Path

DATA_DIR = Path.home() / "data" / "wct-data"

# Points earned
POINTS_FOR_WIN  = 3
POINTS_FOR_DRAW = 1

# File paths
PATH_TO_MATCH_SCHEDULE  = DATA_DIR / "matches.csv"
PATH_TO_STANDINGS       = DATA_DIR / "group-stage-standings.csv"
PATH_TO_TEAMS_LIST      = DATA_DIR / "teams.csv"
