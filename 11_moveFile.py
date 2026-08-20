from pathlib import Path
import shutil

file_path = Path("data/input/employees.csv")
shutil.move(file_path, "data/archive/employees.csv")