import numpy as np
from scipy.stats import pearsonr


def correlation_test(df):
    """
    Domain-agnostic statistical test.
    Automatically selects numeric columns instead of assuming a 'value' column.
    """

    # Select only numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    # We need at least two numeric columns to run correlation
    if len(numeric_cols) < 2:
        return {
            "status": "failed",
            "reason": "Not enough numeric columns for correlation analysis",
            "available_columns": list(df.columns)
        }

    x_col = numeric_cols[0]
    y_col = numeric_cols[1]

    x = df[x_col].values
    y = df[y_col].values

    corr, p_value = pearsonr(x, y)

    return {
        "test": "Pearson Correlation",
        "x_column": x_col,
        "y_column": y_col,
        "correlation": float(corr),
        "p_value": float(p_value)
    }
