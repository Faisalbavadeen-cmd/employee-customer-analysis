import pandas as pd
from src.data.loader import DataLoader
from src.data.cleaner import DataCleaner, EmployeeDataProcessor

loader = DataLoader()
df = loader.load_csv("data/raw/employees.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

cleaner=DataCleaner()
cleaned_df=cleaner.process(df)
print(cleaned_df)
cleaned_df.to_csv("data/processed/cleaned_employees.csv", index=False)

processor = EmployeeDataProcessor()
processed_df = processor.process(df)
print(processed_df)

from src.analysis.analyzer import DataAnalyzer

analyzer = DataAnalyzer(cleaned_df)
print(analyzer.department_summary())
print(analyzer.summary())
print(analyzer.high_salary_employees())

departments_df = pd.read_csv("data/raw/departments.csv")
merged_df = analyzer.merge_departments(departments_df)
print(merged_df)

from src.visualization.charts import VisualizationManager

visualizer = VisualizationManager(cleaned_df)

visualizer.salary_by_department()
visualizer.salary_distribution()
visualizer.experience_vs_salary()
visualizer.headcount_by_department()
visualizer.cumulative_joining_trend()