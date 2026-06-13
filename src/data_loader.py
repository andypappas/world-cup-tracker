import pandas as pd
    
def import_data(file_path):
    df = pd.read_csv(file_path)
    df = df.astype({
            "Home Score": "int8",
            "Away Score": "int8"
            })
    return df


