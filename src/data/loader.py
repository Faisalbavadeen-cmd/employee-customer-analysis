import pandas as pd
from src.utils.exceptions import InvalidDatasetError


class DataLoader:

    def load_csv(self, file_path, validate=True):

        df = pd.read_csv(file_path)

        # Clean column names
        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        # Standard column names
        column_mapping = {
            "employee_id": "employee_id",
            "employeeid": "employee_id",
            "first_name": "first_name",
            "firstname": "first_name",
            "last_name": "last_name",
            "lastname": "last_name",
            "position": "designation",
            "designation": "designation",
            "joining_date": "joining_date",
            "performance_score": "performance_score",
            "performance": "performance_score",
            "salary": "salary",
            "age": "age",
            "gender": "gender",
            "department": "department",
            "city": "city"
        }

        df = df.rename(
            columns={
                col: column_mapping[col]
                for col in df.columns
                if col in column_mapping
            }
        )

        # Create experience from joining date if not available
        if "experience" not in df.columns and "joining_date" in df.columns:
            df["joining_date"] = pd.to_datetime(
                df["joining_date"],
                errors="coerce"
            )

            current_year = pd.Timestamp.now().year

            df["experience"] = (
                current_year - df["joining_date"].dt.year
            )

            df["experience"] = df["experience"].clip(lower=0)

        if validate:

            required_columns = {
                "employee_id",
                "first_name",
                "last_name",
                "age",
                "gender",
                "department",
                "designation",
                "salary",
                "joining_date",
                "performance_score",
                "city",
                "experience"
            }

            missing_columns = required_columns - set(df.columns)

            if missing_columns:
                raise InvalidDatasetError(
                    f"Missing required columns: {missing_columns}"
                )

        return df