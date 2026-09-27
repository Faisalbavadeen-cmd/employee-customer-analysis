import pandas as pd
import matplotlib.pyplot as plt


class VisualizationManager:

    def __init__(self, df):
        self.df = df

    def salary_by_department(self):
        data = self.df.groupby("department")["salary"].mean()

        ax = data.plot(
            kind="bar",
            figsize=(10, 6)
        )

        ax.set_title("Average Salary by Department")
        ax.set_xlabel("Department")
        ax.set_ylabel("Average Salary")
        ax.grid(axis="y", linestyle="--", alpha=0.5)
        ax.legend(["Average Salary"])

        plt.tight_layout()
        plt.savefig(
            "outputs/charts/average_salary_by_department.png"
        )
        plt.close()

    def salary_distribution(self):
        ax = self.df["salary"].plot(
            kind="hist",
            bins=20,
            figsize=(10, 6)
        )

        ax.set_title("Salary Distribution")
        ax.set_xlabel("Salary")
        ax.set_ylabel("Number of Employees")
        ax.grid(axis="y", linestyle="--", alpha=0.5)
        ax.legend(["Salary"])

        plt.tight_layout()
        plt.savefig(
            "outputs/charts/salary_distribution.png"
        )
        plt.close()

    def experience_vs_salary(self):
        ax = self.df.plot(
            x="experience",
            y="salary",
            kind="scatter",
            figsize=(10, 6)
        )

        ax.set_title("Experience vs Salary")
        ax.set_xlabel("Years of Experience")
        ax.set_ylabel("Salary")
        ax.grid(True, linestyle="--", alpha=0.5)
        ax.legend(["Employees"])

        plt.tight_layout()
        plt.savefig(
            "outputs/charts/experience_vs_salary.png"
        )
        plt.close()

    def headcount_by_department(self):
        data = self.df["department"].value_counts()

        ax = data.plot(
            kind="pie",
            autopct="%1.1f%%",
            figsize=(8, 8)
        )

        ax.set_title("Department Headcount Share")
        ax.set_ylabel("")

        plt.tight_layout()
        plt.savefig(
            "outputs/charts/headcount_share.png"
        )
        plt.close()

    def cumulative_joining_trend(self):
        data = self.df.copy()

        data["joining_date"] = pd.to_datetime(
            data["joining_date"],
            errors="coerce"
        )

        data = data.dropna(
            subset=["joining_date"]
        )

        data = data.sort_values(
            "joining_date"
        )

        data["cumulative_count"] = range(
            1,
            len(data) + 1
        )

        plt.figure(figsize=(10, 6))

        plt.plot(
            data["joining_date"],
            data["cumulative_count"],
            label="Cumulative Employees"
        )

        plt.title(
            "Cumulative Employee Joining Trend"
        )
        plt.xlabel("Joining Date")
        plt.ylabel("Cumulative Employees")
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.legend()

        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.savefig(
            "outputs/charts/cumulative_joining_trend.png"
        )
        plt.close()


       