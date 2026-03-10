import pytest
import pandas as pd
from app.pipeline.transformer import clean_stock_data

def test_clean_removes_null_rows():
    raw = pd.DataFrame({
        "Close": [100, None, 102], "Volume": [1000, 2000, 3000],
        "Open": [99, 99, 101], "High": [101, 100, 103],
        "Low": [98, 97, 100],
        "Date": ["2024-01-01", "2024-01-02", "2024-01-03"],
        "ticker": ["AAPL", "AAPL", "AAPL"]
    })
    result = clean_stock_data(raw)
    assert len(result) == 2   # null row should be removed

# Run tests locally:
pytest tests/ -v
