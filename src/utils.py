import numpy as np
import pandas as pd


def content_type_percentage(df: pd.DataFrame) -> tuple:
    """
    Calculate percentage distribution of Movies and TV Shows.

    Parameters
    ----------
    df : pd.DataFrame
        Netflix dataset containing a 'type' column.

    Returns
    -------
    tuple
        (movie_percentage, tv_show_percentage)

    Notes
    -----
    - Handles empty DataFrames safely
    - Percentages are rounded to 2 decimal places
    """

    # If DataFrame is empty, avoid division by zero
    if df.empty or "type" not in df.columns:
        return 0.0, 0.0

    total_titles = len(df)

    movie_count = (df["type"] == "Movie").sum()
    tv_show_count = (df["type"] == "TV Show").sum()

    movie_pct = np.round((movie_count / total_titles) * 100, 2)
    tv_pct = np.round((tv_show_count / total_titles) * 100, 2)

    return movie_pct, tv_pct


def yearly_stats(df: pd.DataFrame) -> dict:
    """
    Compute summary statistics for content addition years.

    Parameters
    ----------
    df : pd.DataFrame
        Netflix dataset containing a 'year_added' column.

    Returns
    -------
    dict
        {
            "min_year": int,
            "max_year": int,
            "avg_year": int
        }

    Notes
    -----
    - Ignores missing (NaN) values
    - Returns 0 for all values if data is unavailable
    """

    if df.empty or "year_added" not in df.columns:
        return {
            "min_year": 0,
            "max_year": 0,
            "avg_year": 0
        }

    # Drop NaN values before calculations
    years = df["year_added"].dropna().astype(int).values

    # Handle case where all values are NaN
    if len(years) == 0:
        return {
            "min_year": 0,
            "max_year": 0,
            "avg_year": 0
        }

    return {
        "min_year": int(np.min(years)),
        "max_year": int(np.max(years)),
        "avg_year": int(np.mean(years))
    }
