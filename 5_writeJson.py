"""
import json
employee = {
    "name": "Rohit",
    "department": "Data",
    "salary": 90000
}

with open("data/employeejson.json", "w") as file:
    json.dump(employee,file, indent=4)
"""
import json 
data = [
    {
        "name": "Rahul",
        "department": "Data",
        "salary": 70000
    },
    {
        "name": "Amit",
        "department": "Data",
        "salary": 80000
    },
    {
        "name": "Priya",
        "department": "HR",
        "salary": 60000
    }
]
with open("data/employee_output.json", "w") as file:
    json.dump(data, file, indent=4)