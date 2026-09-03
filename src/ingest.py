import pandas as pd

from config.config import RAW_DATA_PATH, COLUMN_RENAME_MAP


def validate_incoming(df: pd.DataFrame) -> None:
    if df.empty:
        raise ValueError("Raw data file is empty")

    null_values = df.isnull().sum()
    if null_values.sum() > 0:
        print("Nulls found on ingest:\n", null_values[null_values > 0])

    duplicate_values = df.duplicated().sum()
    if duplicate_values > 0:
        print(f"{duplicate_values} duplicate rows found on ingest")

def load_data(path=RAW_DATA_PATH) -> pd.DataFrame:
    df = pd.read_excel(path)
    df = df.rename(columns=COLUMN_RENAME_MAP)
    validate_incoming(df)
    return df.copy()