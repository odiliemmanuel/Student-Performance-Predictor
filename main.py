from config.config import TARGET_COLUMN
from src.analyze import clean_data, summarize
from src.evaluate import evaluate_models
from src.ingest import load_data
from src.preprocess import validate_target, check_data_quality, split_features_target
from src.train import train_all_models


def main():
    df = load_data()
    df = clean_data(df)
    summarize(df, TARGET_COLUMN)

    validate_target(df)
    check_data_quality(df)

    X, y = split_features_target(df)
    trained_models, X_test, y_test = train_all_models(X, y)

    results = evaluate_models(trained_models, X_test, y_test)
    print("\n", results)




if __name__ == "__main__":
    main()