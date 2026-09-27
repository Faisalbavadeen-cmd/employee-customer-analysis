from typing import Any
import pandas as pd


def filter_high_salary(
    df: pd.DataFrame,
    limit: float = 50000
) -> list[float]:
    return [
        float(salary)
        for salary in df["salary"]
        if salary > limit
    ]


def clean_names(
    names: list[str]
) -> list[str]:
    return list(
        map(
            lambda name: name.strip().title(),
            names
        )
    )


def active_employees(
    records: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    return list(
        filter(
            lambda row: row.get("status") == "Active",
            records
        )
    )


def select_columns(
    df: pd.DataFrame,
    *columns: str
) -> pd.DataFrame:
    return df[list(columns)]


def filter_data(
    df: pd.DataFrame,
    **filters: Any
) -> pd.DataFrame:
    result = df.copy()

    for column, value in filters.items():
        result = result[
            result[column] == value
        ]

    return result


def sort_data(
    df: pd.DataFrame,
    column: str
) -> pd.DataFrame:
    return df.sort_values(
        by=column,
        key=lambda values: values
    )