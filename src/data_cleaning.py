"""
data_cleaning.py
-----------------
Purpose:
This script loads a messy sales dataset, cleans it using several steps,
and outputs a cleaned CSV. The goal is to demonstrate basic data cleaning
and responsible use of AI tools like GitHub Copilot.
"""

import pandas as pd

# ---------------------------------------------------------
# Function 1 — Load raw data
# (COPILOT-GENERATED STARTER — modify it after Copilot suggests code)
# ---------------------------------------------------------
# What this function should do:
# Load the raw CSV file into a pandas DataFrame.
# Why: Creating a reusable function keeps the pipeline organized.
def load_data(file_path: str):
    df = pd.read_csv(file_path)
    return df


# ---------------------------------------------------------
# Function 2 — Clean column names
# (COPILOT-GENERATED STARTER — modify it after Copilot suggests code)
# ---------------------------------------------------------
# What this function should do:
# Standardize column names (lowercase, underscores, strip spaces).
# Why: Messy column names cause errors in processing and analysis.
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
    )
    return df


# ---------------------------------------------------------
# Function 3 — Handle missing values
# ---------------------------------------------------------
# What this function should do:
# Fill or drop missing values consistently.
# Why: Missing prices/quantities cause calculation errors.
def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    # Example strategy: drop rows missing price OR quantity
    df = df.dropna(subset=["price", "quantity"])
    return df


# ---------------------------------------------------------
# Function 4 — Remove clearly invalid values
# ---------------------------------------------------------
# What this function should do:
# Remove rows with negative prices or quantities.
# Why: Negative values are data-entry mistakes.
def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    df = df[(df["price"] >= 0) & (df["quantity"] >= 0)]
    return df


# ---------------------------------------------------------
# Main pipeline for running the full cleaning process
# ---------------------------------------------------------
if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)

    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())
