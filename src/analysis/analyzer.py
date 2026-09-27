import numpy as np
import pandas as pd


class DataAnalyzer:

    def __init__(self, df):
        self.df = df

    def summary(self):
        salary = self.df["salary"].dropna()

        # NumPy array conversion
        salary_array = np.array(salary)

        # 1D to 2D reshape
        reshaped_salary = salary_array.reshape(-1, 1)

        # Broadcasting
        broadcasted_salary = reshaped_salary + 1000

        # Performance and experience matrix
        performance_matrix = self.df[
            ["performance_score", "experience"]
        ].to_numpy()

        # Weight vector
        weight_vector = np.array([0.7, 0.3])

        # Dot product
        dot_result = np.dot(
            performance_matrix,
            weight_vector
        )

        return {
            "average_salary": float(np.mean(salary_array)),
            "total_salary": float(np.sum(salary_array)),
            "salary_std": float(np.std(salary_array)),
            "employee_count": int(len(self.df)),
            "dot_result": dot_result[:5].tolist()
        }

    def pandas_indexing_demo(self):
        # Column selection
        selected_columns = self.df[
            ["employee_id", "department", "salary"]
        ]

        # Label-based indexing using .loc[]
        loc_data = self.df.loc[
            self.df["salary"] > 50000,
            ["employee_id", "department", "salary"]
        ]

        # Integer position indexing using .iloc[]
        iloc_data = self.df.iloc[
            :5,
            :3
        ]

        # Boolean filtering
        high_salary = self.df[
            self.df["salary"] > 50000
        ]

        return {
            "selected_columns": selected_columns,
            "loc_data": loc_data,
            "iloc_data": iloc_data,
            "high_salary": high_salary
        }

    def department_summary(self):
        return self.df.groupby("department").agg(
            employee_count=("employee_id", "count"),
            avg_salary=("salary", "mean"),
            max_salary=("salary", "max")
        )

    def high_salary_employees(self):
        return self.df[
            self.df["salary"] > 50000
        ]

    def merge_departments(self, departments_df):
        return self.df.merge(
            departments_df,
            on="department_id",
            how="left"
        )