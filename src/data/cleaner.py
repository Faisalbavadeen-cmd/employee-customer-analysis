import pandas as pd

from abc import ABC, abstractmethod


class BaseDataProcessor(ABC):

    @abstractmethod
    def process(self, df):
        pass


class DataCleaner(BaseDataProcessor):


    def process(self, df):
        df = df.copy()
        missing_values = df.isna().sum()
        print("Missing values:")
        print(missing_values)

        df = df.drop_duplicates()
        df = df.dropna(subset=["employee_id", "department"])

        if "salary" in df.columns:
            df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
            df["salary"] = df["salary"].fillna(df["salary"].median())

        if "joining_date" in df.columns:
            df["joining_date"] = pd.to_datetime(
                df["joining_date"], errors="coerce"
            )

        return df
class EmployeeDataProcessor(DataCleaner):

    def __init__(self):
        super().__init__()

    def process(self, df):
        return super().process(df)    