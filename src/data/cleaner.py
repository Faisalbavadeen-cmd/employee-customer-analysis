from abc import ABC, abstractmethod
import pandas as pd


class BaseDataProcessor(ABC):

    @abstractmethod
    def process(self, df):
        pass


class DataCleaner(BaseDataProcessor):

    def process(self, df):
        df = df.copy()

        print("Missing values:")
        print(df.isna().sum())

        # Remove duplicate records
        df = df.drop_duplicates()

        # Remove rows with critical missing values
        df = df.dropna(
            subset=["employee_id", "department"]
        )

        # Convert salary to numeric
        if "salary" in df.columns:
            df["salary"] = pd.to_numeric(
                df["salary"],
                errors="coerce"
            )
            df["salary"] = df["salary"].fillna(
                df["salary"].median()
            )

        # Convert joining date
        if "joining_date" in df.columns:
            df["joining_date"] = pd.to_datetime(
                df["joining_date"],
                errors="coerce"
            )

        # Export processed dataset
        df.to_csv(
            "data/processed/cleaned_employees.csv",
            index=False
        )

        return df


class EmployeeDataProcessor(DataCleaner):

    def __init__(self):
        super().__init__()

    def process(self, df):
        return super().process(df)