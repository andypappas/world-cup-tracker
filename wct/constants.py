from pathlib import Path

DATA_DIR = Path.home() / "data" / "wct-data"

# Points earned
POINTS_FOR_WIN  = 3
POINTS_FOR_DRAW = 1

# File paths
PATH_TO_GROUP_MATCHES       = DATA_DIR / "group-stage-matches.csv"
PATH_TO_GROUP_STANDINGS     = DATA_DIR / "group-stage-standings.csv"
PATH_TO_KNOCKOUT_MATCHES    = DATA_DIR / "knockout-stage-matches.csv"
PATH_TO_KNOCKOUT_STANDINGS  = DATA_DIR / "knockout-stage-standings.csv"

