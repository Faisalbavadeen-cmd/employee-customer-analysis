from src.data.loader import DataLoader
from src.data.cleaner import DataCleaner, EmployeeDataProcessor
from src.analysis.analyzer import DataAnalyzer
from src.visualization.charts import VisualizationManager
from src.reports.generator import ReportGenerator
from src.api.client import APIClient
from src.config.settings import API_URL


def main():

    # 1. Load employee dataset
    loader = DataLoader()

    df = loader.load_csv(
        "data/raw/employees.csv"
    )

    print("Original Shape:", df.shape)

    # 2. Clean employee data
    cleaner = DataCleaner()

    cleaned_df = cleaner.process(df)

    # 3. Employee processor using inheritance
    processor = EmployeeDataProcessor()

    cleaned_df = processor.process(
        cleaned_df
    )

    # 4. Load department relational dataset
    departments_df = loader.load_csv(
        "data/raw/departments.csv",
        validate=False
    )

    # 5. Create department_id mapping
    department_mapping = departments_df[
        ["department_id", "department"]
    ].drop_duplicates()

    # 6. Add department_id to employee data
    cleaned_df = cleaned_df.merge(
        department_mapping,
        on="department",
        how="left"
    )

    # 7. Analyze employee data
    analyzer = DataAnalyzer(
        cleaned_df
    )

    summary = analyzer.summary()

    department_summary = (
        analyzer.department_summary()
    )

    # 8. Pandas indexing demonstration
    indexing_results = (
        analyzer.pandas_indexing_demo()
    )

    print(
        "High Salary Employees:",
        len(indexing_results["high_salary"])
    )

    # 9. Relational merge using department_id
    merged_df = analyzer.merge_departments(
        departments_df
    )

    print(
        "Merged Shape:",
        merged_df.shape
    )

    # 10. Generate five visualizations
    visualizer = VisualizationManager(
        cleaned_df
    )

    visualizer.salary_by_department()

    visualizer.salary_distribution()

    visualizer.experience_vs_salary()

    visualizer.headcount_by_department()

    visualizer.cumulative_joining_trend()

    # 11. REST API integration
    api_client = APIClient()

    api_result = api_client.get_data(
        API_URL
    )

    print(
        "API Result:",
        api_result
    )

    # 12. Generate reports
    reporter = ReportGenerator(
        summary,
        department_summary
    )

    reporter.generate()

    # 13. Final output
    print(
        "Project completed successfully!"
    )

    print(
        "Employee Count:",
        summary["employee_count"]
    )

    print(
        "Average Salary:",
        summary["average_salary"]
    )


if __name__ == "__main__":
    main()