import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path, sep=',', quotechar='"', on_bad_lines='skip')
        return df
    except FileNotFoundError:
        print(f"File not found at path {file_path}")
        return None
    except pd.errors.ParserError as e:
        print(f"Error parsing file at {file_path}: {e}")
        return None



