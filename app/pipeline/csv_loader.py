import pandas as pd

def load_from_csv(filepath: str) -> pd.DataFrame:
    """Load stock data from a local CSV file."""
    df = pd.read_csv(filepath, parse_dates=["Date"])
    df.columns = df.columns.str.lower() # standardise column names
    return df