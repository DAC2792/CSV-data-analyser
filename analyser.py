import pandas as pd
import os

#Load a CSV file from the given filepath, return as a Dataframe
def load_csv(filepath):
    if not os.path.exists(filepath):
        print("Error: file not found")
        return None
    df = pd.read_csv(filepath)
    return df

#Print key information and statistics about the dataframe
def analyse_csv(df):
    print(f"Rows and Columns: {df.shape}")
    print(f"Columns: {df.columns}")
    print(f"Summary Statistics: {df.describe()}")

#Call main block to begin running all code
if __name__ == "__main__":
    file = input("Enter CSV filename: ")
    df = load_csv(file)
    if df is not None:
        analyse_csv(df)

