import json
with open("data/employee.json", "r") as file:
# help(json.load) 
# print(dir(json)) 
    data = json.load(file)
    for key, value in data.items():
        print(f"{key} : {value}")