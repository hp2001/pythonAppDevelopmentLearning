from pathlib import Path
folder_path = Path("data")
for i in folder_path.iterdir():
    if i.suffix == ".csv":
        print(i.name)
folder_path = Path("data/input")
folder_path.mkdir(exist_ok=True)
folder_path = Path("data/output")
folder_path.mkdir(exist_ok=True)
folder_path = Path("data/archive")
folder_path.mkdir(exist_ok=True)