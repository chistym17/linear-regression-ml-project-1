import pandas as pd

def read_csv_file(file_path):
    try:
        data = pd.read_csv(file_path)
        print("CSV file loaded successfully!")
        return data
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        return None

