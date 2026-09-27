import numpy as np
import pandas as pd


class DataAnalyzer:

    def __init__(self, df):
        self.df = df

    def summary(self):
        salary = self.df["salary"].dropna()

        salary_array = np.array(salary)

        # NumPy reshape and broadcasting
        reshaped_salary = salary_array.reshape(-1, 1)
        broadcasted_salary = reshaped_salary + 1000

        # NumPy multidimensional dot product
        performance_matrix = self.df[
            ["performance_score", "experience"]
        ].to_numpy()

        weight_vector = np.array([0.7, 0.3])

        dot_result = np.dot(
            performance_matrix,
            weight_vector
        )

        return {
            "average_salary": float(np.mean(salary_array)),
            "total_salary": float(np.sum(salary_array)),
            "salary_std": float(np.std(salary_array)),
            "employee_count": int(len(self.df)),
            "dot_result": dot_result.tolist()
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
            on="department",
            how="left"
        )
    