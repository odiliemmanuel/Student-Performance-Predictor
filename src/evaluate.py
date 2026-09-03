import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def evaluate_models(trained_models: dict, X_test, y_test) -> pd.DataFrame:
    rows = []

    for name, model in trained_models.items():
        predictions = model.predict(X_test)
        rows.append({
            "model": name,
            "mae": mean_absolute_error(y_test, predictions),
            "rmse": mean_squared_error(y_test, predictions) ** 0.5,
            "r2": r2_score(y_test, predictions),
        })

    return pd.DataFrame(rows).set_index("rmse")