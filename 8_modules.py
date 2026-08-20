from employee_utils import get_data_employees

employees = [
    {"name": "Rahul", "department": "Data"},
    {"name": "Priya", "department": "HR"},
    {"name": "Amit", "department": "Data"}
]

result = get_data_employees(employees)

print(result)