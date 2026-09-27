import pandas as pd
import matplotlib.pyplot as plt


class VisualizationManager:

    def __init__(self, df):
        self.df = df

    def salary_by_department(self):
        data = self.df.groupby("department")["salary"].mean()

        data.plot(kind="bar")
        plt.title("Average Salary by Department")
        plt.xlabel("Department")
        plt.ylabel("Average Salary")
        plt.tight_layout()
        plt.savefig("outputs/charts/average_salary_by_department.png")
        plt.close()

    def salary_distribution(self):
        self.df["salary"].plot(kind="hist")

        plt.title("Salary Distribution")
        plt.xlabel("Salary")
        plt.ylabel("Number of Employees")
        plt.tight_layout()
        plt.savefig("outputs/charts/salary_distribution.png")
        plt.close()

    def experience_vs_salary(self):
        self.df.plot(
            x="experience",
            y="salary",
            kind="scatter"
        )

        plt.title("Experience vs Salary")
        plt.xlabel("Experience")
        plt.ylabel("Salary")
        plt.tight_layout()
        plt.savefig("outputs/charts/experience_vs_salary.png")
        plt.close()

    def headcount_by_department(self):
        data = self.df["department"].value_counts()

        data.plot(kind="pie", autopct="%1.1f%%")
        plt.title("Headcount Share by Department")
        plt.ylabel("")
        plt.tight_layout()
        plt.savefig("outputs/charts/headcount_share.png")
        plt.close()

    def cumulative_joining_trend(self):
        data = self.df.copy()
        data["joining_date"] = pd.to_datetime(data["joining_date"])
        data = data.sort_values("joining_date")

        data["cumulative_count"] = range(1, len(data) + 1)

        plt.plot(data["joining_date"], data["cumulative_count"])
        plt.title("Cumulative Employee Joining Trend")
        plt.xlabel("Joining Date")
        plt.ylabel("Cumulative Employees")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("outputs/charts/cumulative_joining_trend.png")
        plt.close()


       