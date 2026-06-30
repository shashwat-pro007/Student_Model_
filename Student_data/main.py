from src.load_data import load_dataset
from src.clean_data import clean_data
from src.transform import transform_data
from src.analyze import analyze_data
from src.report import generate_report

file_path = "data/student_dataset_v2.csv"
print("Student Performance Data Analysis System")
data = load_dataset(file_path)
data = clean_data(data)
data = transform_data(data)
analyze_data(data)
generate_report(data)
print("\nProject Completed Successfully")