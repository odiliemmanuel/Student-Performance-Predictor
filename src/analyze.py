import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    df = df.dropna()
    return df

def summarize(df: pd.DataFrame, target: str) -> None:
    print("Average target value:", df[target].mean())
    print("\nCorrelation with target:\n", df.corr(numeric_only=True)[target].sort_values(ascending=False))