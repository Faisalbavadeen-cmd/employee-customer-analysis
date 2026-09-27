from src.data.loader import DataLoader
from src.data.cleaner import DataCleaner, EmployeeDataProcessor
from src.analysis.analyzer import DataAnalyzer
from src.visualization.charts import VisualizationManager
from src.reports.generator import ReportGenerator
from src.api.client import APIClient
from src.config.settings import API_URL


def main():

    loader = DataLoader()

    # Load employee data
    df = loader.load_csv("data/raw/employees.csv")

    # Clean employee data
    cleaner = DataCleaner()
    cleaned_df = cleaner.process(df)

    # Process using inheritance
    processor = EmployeeDataProcessor()
    cleaned_df = processor.process(cleaned_df)

    # Analyze data
    analyzer = DataAnalyzer(cleaned_df)

    summary = analyzer.summary()
    department_summary = analyzer.department_summary()

    # Load secondary department data
    departments_df = loader.load_csv(
        "data/raw/departments.csv",
        validate=False
    )

    # Merge employee and department data
    merged_df = analyzer.merge_departments(departments_df)

    # Generate visualizations
    visualizer = VisualizationManager(cleaned_df)

    visualizer.salary_by_department()
    visualizer.salary_distribution()
    visualizer.experience_vs_salary()
    visualizer.headcount_by_department()
    visualizer.cumulative_joining_trend()

    # REST API integration
    api_client = APIClient()
    api_result = api_client.get_data(API_URL)

    print("API Result:", api_result)

    # Generate reports
    reporter = ReportGenerator(
        summary,
        department_summary
    )

    reporter.generate()

    print("Project completed successfully!")
    print("Merged shape:", merged_df.shape)
    print("Summary:", summary)


if __name__ == "__main__":
    main()