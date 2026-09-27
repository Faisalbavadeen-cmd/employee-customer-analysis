import json


class ReportGenerator:

    def __init__(self, summary, department_summary):
        self.summary = summary
        self.department_summary = department_summary

    def generate(self):

        report = {
            "summary": self.summary,
            "department_summary": self.department_summary.to_dict()
        }

        # Actual data-driven findings
        highest_headcount_dept = (
            self.department_summary["employee_count"].idxmax()
        )

        highest_avg_salary_dept = (
            self.department_summary["avg_salary"].idxmax()
        )

        lowest_avg_salary_dept = (
            self.department_summary["avg_salary"].idxmin()
        )

        highest_max_salary_dept = (
            self.department_summary["max_salary"].idxmax()
        )

        highest_headcount = int(
            self.department_summary.loc[
                highest_headcount_dept,
                "employee_count"
            ]
        )

        highest_avg_salary = float(
            self.department_summary.loc[
                highest_avg_salary_dept,
                "avg_salary"
            ]
        )

        lowest_avg_salary = float