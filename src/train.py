import pandas as pd
from lightgbm import LGBMRegressor
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeRegressor
from config.config import RANDOM_STATE, TEST_SIZE
from src.preprocess import build_preprocessor


def get_models() -> dict:
    return {
        "baseline": DummyRegressor(strategy="mean"),
        "linear_regression": LinearRegression(),
        "ridge": Ridge(),
        "decision_tree": DecisionTreeRegressor(random_state=RANDOM_STATE),
        "random_forest": RandomForestRegressor(random_state=RANDOM_STATE),
        "gradient_boosting": GradientBoostingRegressor(random_state=RANDOM_STATE),
        "lightgbm": LGBMRegressor(random_state=RANDOM_STATE),
    }


def train_all_models(X, y, test_size: float = TEST_SIZE, random_state: int = RANDOM_STATE) -> tuple[dict[str, Pipeline], pd.DataFrame, pd.Series]:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    preprocessor = build_preprocessor()
    trained_models = {}

    for name, model in get_models().items():
        pipeline = Pipeline(steps=[
            ("preprocessor", preprocessor),
            (name, model),
        ])

        pipeline.fit(X_train, y_train)
        trained_models[name] = pipeline
        print(f"{name} trained successfully")

    return trained_models, X_test, y_test