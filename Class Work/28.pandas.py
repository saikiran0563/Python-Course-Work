"""pandas fundamentals: Series, DataFrames, filtering, sorting, missing data, and groups.

Install the libraries if needed:
    python -m pip install numpy pandas

Run from the repository root:
    python "Class Work/28.pandas.py"

The sample CSV is generated in memory, so no external dataset is required.
"""
from io import StringIO

import pandas as pd


SAMPLE_CSV = """name,department,score,experience_years
Asha,Engineering,88,1
Ravi,Analytics,91,2
Mina,Engineering,missing,1
Dev,Analytics,76,3
Noor,Design,84,2
"""


def main() -> None:
    print("=== 1. Series ===")
    scores = pd.Series([88, 91, 76], index=["Asha", "Ravi", "Dev"], name="score")
    print(scores)
    print("Ravi's score:", scores.loc["Ravi"])
    print("Average score:", scores.mean())

    print("\n=== 2. Build and inspect a DataFrame ===")
    # na_values converts the word "missing" into a true missing value.
    data = pd.read_csv(StringIO(SAMPLE_CSV), na_values=["missing"])
    print("First five rows:\n", data.head())
    print("\nShape (rows, columns):", data.shape)
    print("Column names:", data.columns.tolist())
    print("\nData types:\n", data.dtypes)
    print("\nSummary statistics:\n", data.describe(numeric_only=True))

    print("\n=== 3. Select columns and filter rows ===")
    print("Names and scores:\n", data[["name", "score"]])
    high_scores = data.loc[data["score"] >= 85, ["name", "department", "score"]]
    print("People scoring 85 or more:\n", high_scores)

    print("\n=== 4. Sort data ===")
    sorted_data = data.sort_values("score", ascending=False, na_position="last")
    print(sorted_data[["name", "score"]])

    print("\n=== 5. Find and handle missing values ===")
    print("Missing values by column:\n", data.isna().sum())
    cleaned_data = data.copy()
    cleaned_data["score"] = cleaned_data["score"].fillna(cleaned_data["score"].mean())
    print("Scores after replacing a missing value with the mean:\n", cleaned_data[["name", "score"]])

    print("\n=== 6. Grouped summaries ===")
    department_summary = cleaned_data.groupby("department")["score"].agg(["count", "mean", "max"])
    print(department_summary.round(2))

    print("\n=== 7. Read a CSV file from disk ===")
    print('To load your own file, use: pd.read_csv("data.csv")')
    print("For this lesson, the example CSV was read from a StringIO object.")


if __name__ == "__main__":
    main()
