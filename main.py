from src.data_loader import *
from src.constants import *

def main():
    
    matches = import_data(PATH_TO_MATCH_SCHEDULE)
    print(matches)

if __name__ == "__main__":
    main()
