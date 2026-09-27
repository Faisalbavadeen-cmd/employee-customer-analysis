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

        with open("outputs/analysis_summary.json", "w") as file:
            json.dump(report, file, indent=4)

        with open("outputs/analysis_summary.txt", "w") as file:
            file.write("EMPLOYEE ANALYSIS SUMMARY\n")
            file.write("=========================\n")
            file.write(str(self.summary))
            file.write("\n\nDEPARTMENT SUMMARY\n")
            file.write(str(self.department_summary))

        with open("outputs/reports/analysis_report.md", "w") as file:
            file.write("# Employee Analysis Report\n\n")

            file.write("## Executive Summary\n")
            file.write(
                "This report summarizes employee salary, headcount and "
                "department-level analysis.\n\n"
            )

            file.write("## Dataset Overview\n")
            file.write(
                f"- Employee Count: {self.summary['employee_count']}\n"
                f"- Average Salary: {self.summary['average_salary']:.2f}\n"
                f"- Total Salary: {self.summary['total_salary']:.2f}\n"
                f"- Salary Standard Deviation: {self.summary['salary_std']:.2f}\n\n"
            )

            file.write("## Statistical Findings\n")
            file.write(str(self.department_summary))

            file.write("\n\n## Key Findings\n")
            file.write("- Salary and employee counts were analyzed by department.\n")
            file.write("- Overall salary statistics were calculated using NumPy.\n")
            file.write("- Department-level aggregations were calculated using Pandas GroupBy.\n")
            file.write("- Five visualizations were generated from the employee dataset.\n")
            file.write("- Department data was merged using a left join.\n\n")

            file.write("## Actionable Recommendations\n")
            file.write(
                "- Review salary differences between departments.\n"
                "- Monitor department headcount distribution.\n"
                "- Use salary and experience analysis for workforce planning.\n"
            )

        return report