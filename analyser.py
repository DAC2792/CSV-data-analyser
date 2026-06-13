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
def analyse_csv(df,columns):
    print(f"Rows and Columns: {df.shape}")
    print(f"Columns: {df.columns}")
    print(f"Summary Statistics: {df.describe()}")
    for column in columns:
        try:
            print(f"Max value: {df[column].max()}")
            print(f"Minimum value: {df[column].min()}")
        except KeyError:
            print(f"Error: '{column}' is not a valid column.")

    with open("outputs/results.txt", "w") as f:
        f.write(f"Rows and Columns: {df.shape}\n")
        f.write(f"Columns: {df.columns}\n")
        f.write(f"Summary Statistics: {df.describe()}\n")
        for column in columns:
            try:
                f.write(f"Max value: {df[column].max()}\n")
                f.write(f"Minimum value: {df[column].min()}\n")
            except KeyError:
                print(f"Error: '{column}' is not a valid column.")

#Call main block to begin running all code
if __name__ == "__main__":
    file = input("Enter CSV filename: ")
    df = load_csv(file)
    if df is not None:
        column = input("Enter column name(s), separated by commas: ")
        raw_columns = column.split(",")
        columns = []

        for item in raw_columns:
            cleaned = item.strip()
            columns.append(cleaned)

        analyse_csv(df,columns)
