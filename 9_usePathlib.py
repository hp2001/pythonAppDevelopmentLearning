from pathlib import Path
file_path = Path("data/employees.csv")
print(file_path)
print(file_path.exists())
print(file_path.is_file())