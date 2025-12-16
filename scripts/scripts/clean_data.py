"""
clean_data.py

Data loading, cleaning, and feature engineering
for the Sales Analysis Final Project.
"""

import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """
    Load sales dataset from a CSV file.
    """
    return pd.read_csv(path)


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names: lowercase and underscores.
    """
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
    )
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic cleaning:
    - Remove duplicates
    - Drop rows with missing values
    """
    df = df.copy()
    df = df.drop_duplicates()
    df = df.dropna()
    return df


def create_high_sales_label(df: pd.DataFrame, target_col: str = "total_sales") -> pd.DataFrame:
    """
    Create a binary classification label:
    high_sales = 1 if total_sales >= median(total_sales), else 0
    """
    df = df.copy()
    median_sales = df[target_col].median()
    df["high_sales"] = (df[target_col] >= median_sales).astype(int)
    return df
