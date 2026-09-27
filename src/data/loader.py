import pandas as pd
from src.utils.exceptions import InvalidDatasetError


class DataLoader:

    def load_csv(self, file_path, validate=True):

        df = pd.read_csv(file_path)

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
                "experience",
                "performance_score",
                "city",
                "status"
            }

            missing_columns = required_columns - set(df.columns)

            if missing_columns:
                raise InvalidDatasetError(
                    f"Missing required columns: {missing_columns}"
                )

        return df