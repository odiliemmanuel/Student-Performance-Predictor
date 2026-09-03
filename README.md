# Student Performance Predictor

A modular machine learning pipeline that predicts a student's final grade (`G3`, 0–20 scale) from academic history, family background, and lifestyle factors, using the [UCI Student Performance dataset](https://archive.ics.uci.edu/dataset/320/student+performance).

Originally prototyped in a single Google Colab notebook, then rebuilt here as a proper layered pipeline — separate ingestion, cleaning, preprocessing, training, and evaluation stages — to mirror how a real ML project is structured rather than one long linear script.

## What it does

1. **Ingests** the raw Excel dataset, renames cryptic column codes (`G3`, `Walc`, `Mjob`) into readable names, and validates the incoming data for nulls and duplicates.
2. **Cleans** the data (drops duplicates/nulls if any exist) and prints a quick summary of the target variable and its correlations.
3. **Preprocesses** features — validates the target column, scales numeric features, one-hot encodes categorical features — using a `scikit-learn` `ColumnTransformer`.
4. **Trains** six regression models on an 80/20 train-test split, each wrapped in its own preprocessing + model pipeline.
5. **Evaluates** every model on held-out test data using MAE, RMSE, and R², and prints a comparison table sorted by performance.

## Results

| Model | RMSE | MAE | R² |
|---|---|---|---|
| Ridge | 1.214 | 0.764 | 0.849 |
| Linear Regression | 1.215 | 0.765 | 0.849 |
| Random Forest | 1.252 | 0.754 | 0.839 |
| LightGBM | 1.315 | 0.788 | 0.823 |
| Gradient Boosting | 1.330 | 0.780 | 0.819 |
| Decision Tree | 1.657 | 0.838 | 0.718 |
| Baseline (mean) | 3.173 | 2.395 | -0.032 |

All models comfortably beat the baseline. Ridge and Linear Regression perform best, since the strongest predictors of final grade (first and second period grades) are highly linearly correlated with it.

## Project structure

```
student-performance/
├── data/
│   └── raw/
│       └── student_data.xlsx      # raw dataset, untouched
├── model/
│   └── config/
│       └── config.py              # paths, target column, rename map, hyperparameters
├── src/
│   ├── ingest.py                  # load + rename + validate incoming data
│   ├── analyze.py                 # clean data, quick summary stats
│   ├── preprocess.py              # target validation, data quality checks, feature transformer
│   ├── train.py                   # trains all 6 models
│   └── evaluate.py                # scores and compares models
├── main.py                        # runs the full pipeline end to end
├── requirements.txt
└── README.md
```

## Technologies used

- **Python 3.12**
- **pandas** — data loading and manipulation
- **openpyxl** — reading `.xlsx` files
- **scikit-learn** — preprocessing (`ColumnTransformer`, `Pipeline`, `StandardScaler`, `OneHotEncoder`, `SimpleImputer`), models (Linear Regression, Ridge, Decision Tree, Random Forest, Gradient Boosting, Dummy baseline), train/test splitting, and evaluation metrics
- **LightGBM** — gradient-boosted tree model
- **PyCharm** — IDE, with an isolated virtual environment (`venv`) per project

## Setup

```bash
# clone the repo
git clone <your-repo-url>
cd student-performance-predictor

# create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt
```

Place `student_data.xlsx` inside `data/raw/`.

## Running

```bash
python main.py
```

This runs the entire pipeline and prints a results table comparing all six models on the test set.

## Possible next steps

- Retrain without `first_period_grade` / `second_period_grade` to see how well demographic and lifestyle features alone predict final grade.
- Save the best-performing model to disk with `joblib` for reuse without retraining.
- Add unit tests for each pipeline stage.
