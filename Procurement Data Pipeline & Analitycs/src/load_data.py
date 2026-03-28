import pandas as pd

def load_data(file_paths):
    dataframes = [pd.read_csv(path) for path in file_paths]
    df = pd.concat(dataframes, ignore_index=True)
    return df


