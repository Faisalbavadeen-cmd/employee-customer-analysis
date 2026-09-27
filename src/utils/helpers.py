def filter_high_salary(df, limit=50000):
    return [salary for salary in df["salary"] if salary > limit]


def clean_names(names):
    return list(map(lambda name: name.strip().title(), names))


def active_employees(df):
    return list(filter(lambda row: row["status"] == "Active", df.to_dict("records")))


def select_columns(df, *columns):
    return df[list(columns)]


def filter_data(df, **filters):
    result = df.copy()

    for column, value in filters.items():
        result = result[result[column] == value]

    return result