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

        # JSON summary
        with open("outputs/analysis_summary.json", "w") as file:
            json.dump(report, file, indent=4)

        # TXT summary
        with open("outputs/analysis_summary.txt", "w") as file:
            file.write("EMPLOYEE ANALYSIS SUMMARY\n")
            file.write("=========================\n\n")

            file.write(
                f"Employee Count: {self.summary['employee_count']}\n"
            )
            file.write(
                f"Average Salary: {self.summary['average_salary']:.2f}\n"
            )
            file.write(
                f"Total Salary: {self.summary['total_salary']:.2f}\n"
            )
            file.write(
                f"Salary Standard Deviation: {self.summary['salary_std']:.2f}\n"
            )

            file.write("\nDEPARTMENT SUMMARY\n")
            file.write("==================\n")
            file.write(str(self.department_summary))

        # Markdown report
        with open(
            "outputs/reports/analysis_report.md",
            "w"
        ) as file:

            file.write("# Employee Analysis Report\n\n")

            file.write("## Executive Summary\n\n")
            file.write(
                "This report presents employee data analysis covering "
                "salary, headcount, department-level statistics and "
                "data quality.\n\n"
            )