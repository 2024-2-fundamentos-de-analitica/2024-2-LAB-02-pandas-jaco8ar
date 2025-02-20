import pandas as pd

def load_data(file_number):
    return pd.read_table(f"files/input/tbl{file_number}.tsv")
