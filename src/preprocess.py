import pandas as pd
from sklearn.compose import ColumnTransformer, make_column_selector
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from config.config import TARGET_COLUMN


def validate_target(df: pd.DataFrame, target: str = TARGET_COLUMN) -> None:
    if target not in df.columns:
        raise ValueError(f"Target column '{target}' not found")
    if df[target].isnull().any():
        raise ValueError(f"Target column '{target}' has missing values")


def check_data_quality(df: pd.DataFrame) -> None:
    print("Shape:", df.shape)
    print("Missing values:", df.isnull().sum().sum())
    print("Duplicate rows:", df.duplicated().sum())


def split_features_target(df: pd.DataFrame, target: str = TARGET_COLUMN) -> tuple[pd.DataFrame, pd.Series]:
    return df.drop(target, axis=1), df[target]


def build_preprocessor() -> ColumnTransformer:
    numerical_columns = make_column_selector(dtype_exclude="object")
    categorical_columns = make_column_selector(dtype_include="object")

    numerical_pipeline = Pipeline(steps=[
        ("impute", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])

    categorical_pipeline = Pipeline(steps=[
        ("impute", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ])

    return ColumnTransformer(transformers=[
        ("numerical", numerical_pipeline, numerical_columns),
        ("categorical", categorical_pipeline, categorical_columns),
    ])
