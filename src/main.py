import pandas as pd
import read_csv_file from "./functions"

if __name__ == "__main__":
    file_path = "../data/dataset.csv"  
    data = read_csv_file(file_path)
    if data is not None:
        print(data.head()) 
